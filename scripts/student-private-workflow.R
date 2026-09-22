# Shared safety and persistence helpers for the local student-private workflow.

STUDENT_PRODUCTION_DATASET_TYPE <- "production-cumulative"
STUDENT_PRIVATE_CODE_ALPHABET <- strsplit("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", "", fixed = TRUE)[[1]]
STUDENT_PRIVATE_CODE_PATTERN <- "^UCR-(?:[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{4}-){3}[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{4}$"

assert_private_tree_ignored <- function(repo_root) {
  ignore_path <- file.path(repo_root, ".gitignore")
  if (!file.exists(ignore_path)) {
    stop("Missing repository .gitignore; refusing to use private student data.")
  }

  rules <- readLines(ignore_path, warn = FALSE, encoding = "UTF-8")
  rules <- sub("\\r$", "", rules)
  private_rule <- "/private/"
  private_positions <- which(rules == private_rule)
  if (!length(private_positions)) {
    stop(
      "The repository .gitignore must contain the root-anchored rule ",
      private_rule,
      " before private student data can be used."
    )
  }

  # Requiring the canonical rule after every negation keeps this check simple
  # and prevents a later broad ! pattern from weakening the private boundary.
  private_position <- max(private_positions)
  later_rules <- if (private_position < length(rules)) rules[(private_position + 1L):length(rules)] else character()
  later_negations <- later_rules[startsWith(later_rules, "!")]
  if (length(later_negations)) {
    stop(
      "The /private/ ignore rule must appear after all .gitignore negation rules; ",
      "a later negation could weaken the private-data boundary."
    )
  }

  invisible(TRUE)
}

student_write_json_atomic <- function(value, path) {
  parent <- dirname(path)
  if (!dir.exists(parent) && !dir.create(parent, recursive = TRUE, showWarnings = FALSE)) {
    stop("Could not create directory for ", path)
  }
  temporary <- tempfile(pattern = paste0(".", basename(path), "."), tmpdir = parent)
  on.exit(if (file.exists(temporary)) unlink(temporary), add = TRUE)
  jsonlite::write_json(value, temporary, auto_unbox = TRUE, pretty = TRUE, null = "null")
  if (file.exists(path)) {
    backup <- tempfile(pattern = paste0(".", basename(path), ".backup."), tmpdir = parent)
    if (!file.rename(path, backup)) stop("Could not stage the existing file for safe replacement: ", path)
    restored <- FALSE
    on.exit({
      if (!restored && file.exists(backup) && !file.exists(path)) file.rename(backup, path)
      if (file.exists(backup)) unlink(backup)
    }, add = TRUE)
    if (!file.rename(temporary, path)) {
      file.rename(backup, path)
      restored <- TRUE
      stop("Could not replace ", path)
    }
    restored <- TRUE
    unlink(backup)
  } else if (!file.rename(temporary, path)) {
    stop("Could not write ", path)
  }
  invisible(path)
}

student_production_paths <- function(repo_root) {
  private_root <- student_private_root(repo_root)
  list(
    root = private_root,
    record_dir = file.path(private_root, "student-records"),
    marker = file.path(private_root, "student-mode.json"),
    access = file.path(private_root, "student-access.json"),
    lock = file.path(private_root, ".student-production.lock")
  )
}

acquire_student_production_lock <- function(repo_root) {
  paths <- student_production_paths(repo_root)
  if (!dir.exists(paths$root) && !dir.create(paths$root, recursive = TRUE, showWarnings = FALSE)) {
    stop("Could not create the private student directory.")
  }
  if (!dir.create(paths$lock, showWarnings = FALSE)) {
    stop(
      "Another student-production addition appears to be in progress. ",
      "If no process is running, remove the stale lock directory: ", paths$lock
    )
  }
  paths$lock
}

release_student_production_lock <- function(lock_path) {
  if (dir.exists(lock_path)) unlink(lock_path, recursive = TRUE)
  invisible(TRUE)
}

student_production_marker <- function() {
  list(
    schemaVersion = "1.0",
    mode = "private",
    datasetType = STUDENT_PRODUCTION_DATASET_TYPE,
    generator = "scripts/add-student-private.R"
  )
}

student_production_access_index <- function(entries = list()) {
  list(
    schemaVersion = "1.0",
    mode = "private",
    datasetType = STUDENT_PRODUCTION_DATASET_TYPE,
    entries = entries
  )
}

validate_student_production_dataset <- function(repo_root, allow_empty = FALSE) {
  paths <- student_production_paths(repo_root)
  required <- c(paths$marker, paths$access, paths$record_dir)
  if (any(!file.exists(required) & !dir.exists(required))) {
    stop("Incomplete production private dataset; expected student-mode.json, student-access.json and student-records/.")
  }

  marker <- read_student_json(paths$marker, "production private mode marker")
  access <- read_student_json(paths$access, "production private access index")
  if (!identical(marker$mode, "private") || !identical(marker$datasetType, STUDENT_PRODUCTION_DATASET_TYPE)) {
    stop("Private student dataset is not marked as the cumulative production dataset.")
  }
  if (!identical(access$mode, "private") || !identical(access$datasetType, STUDENT_PRODUCTION_DATASET_TYPE)) {
    stop("Production private access index has invalid mode or datasetType metadata.")
  }
  entries <- access$entries
  if (is.null(entries)) entries <- list()
  if (!is.list(entries)) stop("Production private access index entries must be an array.")
  if (!length(entries) && !allow_empty) stop("The production private access index has no entries.")

  codes <- vapply(entries, function(entry) as.character(student_value(entry$code, "")), character(1))
  normalized_codes <- vapply(codes, normalize_student_code, character(1))
  ids <- vapply(entries, function(entry) as.character(student_value(entry$recordId, "")), character(1))
  files <- vapply(entries, function(entry) as.character(student_value(entry$recordFile, "")), character(1))
  if (length(entries)) {
    if (any(!grepl(STUDENT_PRIVATE_CODE_PATTERN, codes, perl = TRUE)) || anyDuplicated(normalized_codes)) {
      stop("Production student access codes must be canonical and unique.")
    }
    if (any(!grepl("^[a-z0-9][a-z0-9-]*$", ids)) || anyDuplicated(ids)) {
      stop("Production student record ids must be valid and unique.")
    }
    if (any(!grepl("^[a-z0-9][a-z0-9-]*\\.json$", files)) || any(files != basename(files)) || anyDuplicated(files)) {
      stop("Production student record filenames must be simple, valid and unique.")
    }
  }

  disk_files <- sort(list.files(paths$record_dir, pattern = "\\.json$", all.files = FALSE, no.. = TRUE))
  if (!identical(disk_files, sort(files))) {
    stop("Production student-record files do not exactly match the private access index.")
  }
  for (index in seq_along(entries)) {
    record <- read_student_json(file.path(paths$record_dir, files[[index]]), paste("production student record", ids[[index]]))
    validate_student_record(record, ids[[index]], "private")
  }

  list(paths = paths, marker = marker, access = access, entries = entries, codes = codes, ids = ids, files = files)
}

initialize_student_production_dataset <- function(repo_root) {
  assert_private_tree_ignored(repo_root)
  paths <- student_production_paths(repo_root)
  if (!dir.exists(paths$root) && !dir.create(paths$root, recursive = TRUE, showWarnings = FALSE)) {
    stop("Could not create the private student directory.")
  }
  signals <- c(paths$marker, paths$access, paths$record_dir)
  existing <- file.exists(signals) | dir.exists(signals)
  unrelated <- setdiff(list.files(paths$root, all.files = TRUE, no.. = TRUE), basename(paths$lock))
  if (!any(existing)) {
    if (length(unrelated)) stop("Refusing to initialize production data in a non-empty private directory.")
    if (!dir.create(paths$record_dir, recursive = TRUE, showWarnings = FALSE)) stop("Could not create ", paths$record_dir)
    student_write_json_atomic(student_production_marker(), paths$marker)
    student_write_json_atomic(student_production_access_index(), paths$access)
  } else if (!all(existing)) {
    stop("Incomplete private student dataset; refusing to initialize over partial data.")
  }
  validate_student_production_dataset(repo_root, allow_empty = TRUE)
}

student_random_access_code <- function() {
  if (!requireNamespace("openssl", quietly = TRUE)) {
    stop("Install the openssl package before generating private student access codes.")
  }
  # Sixteen characters from a 32-character alphabet encode 80 random bits.
  bits <- as.integer(rawToBits(openssl::rand_bytes(10)))
  groups <- matrix(bits, ncol = 5, byrow = TRUE)
  values <- as.integer(groups %*% (2^(0:4))) + 1L
  characters <- STUDENT_PRIVATE_CODE_ALPHABET[values]
  grouped <- vapply(split(characters, rep(1:4, each = 4)), paste0, collapse = "", FUN.VALUE = character(1))
  paste("UCR", paste(grouped, collapse = "-"), sep = "-")
}

student_public_development_codes <- function(repo_root) {
  index <- read_student_json(
    file.path(repo_root, "pilot", "shiny", "data", "access_codes.json"),
    "public pilot access index"
  )
  vapply(index$entries, function(entry) normalize_student_code(entry$code), character(1))
}

student_path_within <- function(path, parent) {
  path <- normalizePath(path, winslash = "/", mustWork = TRUE)
  parent <- normalizePath(parent, winslash = "/", mustWork = FALSE)
  if (.Platform$OS.type == "windows") {
    path <- tolower(path)
    parent <- tolower(parent)
  }
  identical(path, parent) || startsWith(path, paste0(parent, "/"))
}

add_student_production_record <- function(repo_root, record_path) {
  assert_private_tree_ignored(repo_root)
  record_path <- normalizePath(record_path, winslash = "/", mustWork = TRUE)
  paths <- student_production_paths(repo_root)
  if (student_path_within(record_path, repo_root) && !student_path_within(record_path, paths$root)) {
    stop("The incoming real-student record must be outside the repository or beneath its ignored /private/ tree.")
  }

  lock <- acquire_student_production_lock(repo_root)
  on.exit(release_student_production_lock(lock), add = TRUE)
  initialize_student_production_dataset(repo_root)
  current <- validate_student_production_dataset(repo_root, allow_empty = TRUE)

  record <- read_student_json(record_path, "incoming completed student record")
  id <- as.character(student_value(record$id, ""))
  validate_student_record(record, id, "private")
  if (id %in% current$ids) stop("Student record id already exists: ", id)
  filename <- paste0(id, ".json")
  destination <- file.path(paths$record_dir, filename)
  if (file.exists(destination) || filename %in% current$files) stop("Student record file already exists: ", filename)

  forbidden <- unique(c(
    vapply(current$codes, normalize_student_code, character(1)),
    student_public_development_codes(repo_root)
  ))
  code <- NULL
  for (attempt in seq_len(1000L)) {
    candidate <- student_random_access_code()
    if (!normalize_student_code(candidate) %in% forbidden) {
      code <- candidate
      break
    }
  }
  if (is.null(code)) stop("Could not generate a unique student access code.")

  entry <- list(code = code, recordId = id, recordFile = filename)
  updated_index <- student_production_access_index(c(current$entries, list(entry)))
  staging <- tempfile(pattern = ".student-stage-", tmpdir = paths$root)
  if (!dir.create(staging, showWarnings = FALSE)) stop("Could not create private staging directory.")
  on.exit(if (dir.exists(staging)) unlink(staging, recursive = TRUE), add = TRUE)
  staged_record <- file.path(staging, filename)
  staged_index <- file.path(staging, "student-access.json")
  student_write_json_atomic(record, staged_record)
  student_write_json_atomic(updated_index, staged_index)
  staged_check <- read_student_json(staged_record, "staged student record")
  validate_student_record(staged_check, id, "private")

  if (!file.rename(staged_record, destination)) stop("Could not publish the new private student record.")
  committed <- FALSE
  on.exit(if (!committed && file.exists(destination)) unlink(destination), add = TRUE)
  old_access <- readBin(paths$access, what = "raw", n = file.info(paths$access)$size)
  tryCatch({
    student_write_json_atomic(updated_index, paths$access)
    validate_student_production_dataset(repo_root)
    committed <- TRUE
  }, error = function(e) {
    connection <- file(paths$access, open = "wb")
    writeBin(old_access, connection)
    close(connection)
    if (file.exists(destination)) unlink(destination)
    stop("Student addition was rolled back: ", conditionMessage(e))
  })

  list(recordId = id, accessCode = code, recordFile = destination)
}
