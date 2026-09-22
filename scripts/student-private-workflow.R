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

student_write_text_atomic <- function(lines, path) {
  parent <- dirname(path)
  if (!dir.exists(parent) && !dir.create(parent, recursive = TRUE, showWarnings = FALSE)) {
    stop("Could not create directory for ", path)
  }
  temporary <- tempfile(pattern = paste0(".", basename(path), "."), tmpdir = parent)
  on.exit(if (file.exists(temporary)) unlink(temporary), add = TRUE)
  writeLines(lines, temporary, useBytes = TRUE)
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
    batch_results = file.path(private_root, "student-last-batch-codes.csv"),
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

add_student_production_records <- function(repo_root, record_paths) {
  assert_private_tree_ignored(repo_root)
  if (!length(record_paths)) stop("No completed student records were supplied.")
  record_paths <- vapply(record_paths, normalizePath, character(1), winslash = "/", mustWork = TRUE)
  if (anyDuplicated(record_paths)) stop("The same input record was supplied more than once.")
  paths <- student_production_paths(repo_root)
  invalid_locations <- vapply(record_paths, function(record_path) {
    student_path_within(record_path, repo_root) && !student_path_within(record_path, paths$root)
  }, logical(1))
  if (any(invalid_locations)) {
    stop(
      "Incoming real-student records must be outside the repository or beneath its ignored /private/ tree: ",
      paste(record_paths[invalid_locations], collapse = ", ")
    )
  }

  incoming <- lapply(seq_along(record_paths), function(index) {
    record <- read_student_json(record_paths[[index]], paste("incoming completed student record", index))
    id <- as.character(student_value(record$id, ""))
    validate_student_record(record, id, "private")
    list(record = record, id = id, filename = paste0(id, ".json"), source = record_paths[[index]])
  })
  incoming_ids <- vapply(incoming, function(item) item$id, character(1))
  incoming_files <- vapply(incoming, function(item) item$filename, character(1))
  if (anyDuplicated(incoming_ids)) stop("The batch contains duplicate student record ids.")
  if (anyDuplicated(incoming_files)) stop("The batch contains duplicate student record filenames.")

  lock <- acquire_student_production_lock(repo_root)
  on.exit(release_student_production_lock(lock), add = TRUE)
  initialize_student_production_dataset(repo_root)
  current <- validate_student_production_dataset(repo_root, allow_empty = TRUE)
  duplicate_ids <- intersect(incoming_ids, current$ids)
  if (length(duplicate_ids)) stop("Student record id already exists: ", paste(duplicate_ids, collapse = ", "))
  duplicate_files <- intersect(incoming_files, current$files)
  if (length(duplicate_files)) stop("Student record file already exists: ", paste(duplicate_files, collapse = ", "))

  forbidden <- unique(c(
    vapply(current$codes, normalize_student_code, character(1)),
    student_public_development_codes(repo_root)
  ))
  codes <- character(length(incoming))
  for (index in seq_along(incoming)) {
    for (attempt in seq_len(1000L)) {
      candidate <- student_random_access_code()
      normalized <- normalize_student_code(candidate)
      if (!normalized %in% c(forbidden, vapply(codes[nzchar(codes)], normalize_student_code, character(1)))) {
        codes[[index]] <- candidate
        break
      }
    }
    if (!nzchar(codes[[index]])) stop("Could not generate a unique student access code.")
  }

  new_entries <- lapply(seq_along(incoming), function(index) {
    list(code = codes[[index]], recordId = incoming_ids[[index]], recordFile = incoming_files[[index]])
  })
  updated_index <- student_production_access_index(c(current$entries, new_entries))
  staging <- tempfile(pattern = ".student-stage-", tmpdir = paths$root)
  if (!dir.create(staging, showWarnings = FALSE)) stop("Could not create private staging directory.")
  on.exit(if (dir.exists(staging)) unlink(staging, recursive = TRUE), add = TRUE)
  staged_records <- file.path(staging, incoming_files)
  destinations <- file.path(paths$record_dir, incoming_files)
  for (index in seq_along(incoming)) {
    student_write_json_atomic(incoming[[index]]$record, staged_records[[index]])
    staged_check <- read_student_json(staged_records[[index]], paste("staged student record", incoming_ids[[index]]))
    validate_student_record(staged_check, incoming_ids[[index]], "private")
  }
  results_lines <- c(
    "record_id,access_code",
    paste(incoming_ids, codes, sep = ",")
  )
  staged_results <- file.path(staging, "student-last-batch-codes.csv")
  student_write_text_atomic(results_lines, staged_results)

  published <- character()
  for (index in seq_along(staged_records)) {
    if (!file.rename(staged_records[[index]], destinations[[index]])) {
      if (length(published)) unlink(published[file.exists(published)])
      stop("Could not publish the complete private student batch.")
    }
    published <- c(published, destinations[[index]])
  }
  committed <- FALSE
  on.exit(if (!committed && length(published)) unlink(published[file.exists(published)]), add = TRUE)
  old_access <- readBin(paths$access, what = "raw", n = file.info(paths$access)$size)
  tryCatch({
    student_write_json_atomic(updated_index, paths$access)
    validate_student_production_dataset(repo_root)
    results <- readLines(staged_results, warn = FALSE, encoding = "UTF-8")
    student_write_text_atomic(results, paths$batch_results)
    committed <- TRUE
  }, error = function(e) {
    connection <- file(paths$access, open = "wb")
    writeBin(old_access, connection)
    close(connection)
    if (length(published)) unlink(published[file.exists(published)])
    stop("Student batch was rolled back: ", conditionMessage(e))
  })

  list(
    records = lapply(seq_along(incoming), function(index) {
      list(recordId = incoming_ids[[index]], accessCode = codes[[index]], recordFile = destinations[[index]])
    }),
    resultsFile = paths$batch_results
  )
}

add_student_production_record <- function(repo_root, record_path) {
  batch <- add_student_production_records(repo_root, record_path)
  result <- batch$records[[1]]
  result$resultsFile <- batch$resultsFile
  result
}
