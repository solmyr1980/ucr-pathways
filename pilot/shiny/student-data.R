# Server-side student data loading and validation.
#
# Public development mode reads the tracked fixtures in this checkout. Private
# mode reads only the ignored private bundle and never consults public records.

student_value <- function(x, fallback = NULL) {
  if (is.null(x) || length(x) == 0 || identical(x, "")) fallback else x
}

normalize_student_code <- function(x) {
  if (is.null(x) || length(x) != 1 || is.na(x)) return(NA_character_)
  value <- toupper(trimws(as.character(x)))
  if (!nzchar(value)) return("")
  if (!grepl("^[A-Z0-9[:space:]-]+$", value)) return(NA_character_)
  gsub("[[:space:]-]", "", value)
}

read_student_json <- function(path, label = path) {
  if (!file.exists(path)) stop("Missing ", label, ": ", path)
  tryCatch(
    jsonlite::fromJSON(path, simplifyVector = FALSE),
    error = function(e) stop("Malformed ", label, ": ", conditionMessage(e))
  )
}

student_private_root <- function(repo_root) file.path(repo_root, "private")

resolve_student_data_mode <- function(repo_root, requested = Sys.getenv("UCR_STUDENT_DATA_MODE", unset = "auto")) {
  requested <- tolower(trimws(requested))
  if (!nzchar(requested)) requested <- "auto"
  if (!requested %in% c("auto", "public", "private")) {
    stop("UCR_STUDENT_DATA_MODE must be public, private, or auto.")
  }
  if (!identical(requested, "auto")) return(requested)
  private_root <- student_private_root(repo_root)
  marker_file <- file.path(private_root, "student-mode.json")
  private_signals <- c(
    marker_file,
    file.path(private_root, "student-access.json"),
    file.path(private_root, "student-records")
  )
  if (file.exists(marker_file)) return("private")
  if (any(file.exists(private_signals) | dir.exists(private_signals))) {
    stop("Incomplete private student dataset: student-mode.json is missing. Refusing public fallback.")
  }
  "public"
}

student_record_id <- function(entry, mode) {
  value <- if (identical(mode, "private")) entry$recordId else entry$example_id
  as.character(student_value(value, ""))
}

student_record_filename <- function(entry, mode) {
  if (identical(mode, "private")) return(as.character(student_value(entry$recordFile, "")))
  paste0(student_record_id(entry, mode), ".json")
}

validate_student_programme_concepts <- function(record, programmes, expected_id, required = FALSE) {
  rationale <- record$academicRationale
  if (is.null(rationale)) {
    if (required) stop("Student record ", expected_id, " has no academicRationale.")
    return(invisible(TRUE))
  }
  if (!is.list(rationale) || is.null(rationale$alternatives) || !is.list(rationale$alternatives)) {
    stop("Student record ", expected_id, " must contain academicRationale.alternatives.")
  }

  programme_ids <- vapply(programmes, function(programme) {
    as.character(student_value(programme$id, ""))
  }, character(1))
  comparator_ids <- programme_ids[vapply(programmes, function(programme) {
    identical(programme$role, "comparator") || identical(programme$family, "comparator")
  }, logical(1))]
  ucr_ids <- programme_ids[vapply(programmes, function(programme) {
    identical(programme$family, "ucr") ||
      as.character(student_value(programme$role, "")) %in% c("ucr-alternative", "ucr-depth", "ucr-balanced", "ucr-thematic")
  }, logical(1))]

  alternatives <- rationale$alternatives
  rationale_ids <- vapply(seq_along(alternatives), function(index) {
    item <- alternatives[[index]]
    if (!is.list(item)) stop("Student record ", expected_id, " has an invalid programme concept entry.")
    programme_id <- item$programmeId
    concept <- item$concept
    if (is.null(programme_id) || length(programme_id) != 1 || is.na(programme_id) || !nzchar(trimws(as.character(programme_id)))) {
      stop("Student record ", expected_id, " has a programme concept without programmeId.")
    }
    if (is.null(concept) || length(concept) != 1 || is.na(concept) || !nzchar(trimws(as.character(concept)))) {
      stop("Student record ", expected_id, " has a blank concept for programme ", as.character(programme_id), ".")
    }
    as.character(programme_id)
  }, character(1))

  unknown_ids <- setdiff(rationale_ids, programme_ids)
  if (length(unknown_ids)) {
    stop("Student record ", expected_id, " references an unknown programmeId in academicRationale: ", paste(unknown_ids, collapse = ", "), ".")
  }
  if (any(rationale_ids %in% comparator_ids)) {
    stop("Student record ", expected_id, " must not assign a programme concept to the comparator.")
  }
  if (anyDuplicated(rationale_ids)) {
    stop("Student record ", expected_id, " has duplicate programme concepts.")
  }
  if (length(rationale_ids) != length(ucr_ids) || !setequal(rationale_ids, ucr_ids)) {
    stop("Student record ", expected_id, " must contain exactly one programme concept for every UCR alternative.")
  }
  invisible(TRUE)
}

validate_student_record <- function(record, expected_id, mode) {
  if (!is.list(record)) stop("Student record ", expected_id, " must be a JSON object.")
  if (!identical(as.character(student_value(record$id, "")), expected_id)) {
    stop("Student record id does not match its access-index id: ", expected_id)
  }
  if (!nzchar(trimws(as.character(student_value(record$interests, ""))))) {
    stop("Student record ", expected_id, " has no original interest statement.")
  }
  if (identical(mode, "private")) {
    if (!identical(record$origin, "student")) stop("Private record ", expected_id, " must have origin student.")
    if (!nzchar(trimws(as.character(student_value(record$interestInterpretation, ""))))) {
      stop("Private record ", expected_id, " has no interestInterpretation.")
    }
  }
  programmes <- record$programmes
  if (!is.list(programmes) || length(programmes) < 2 || length(programmes) > 4) {
    stop("Student record ", expected_id, " must contain one comparator and one to three UCR alternatives.")
  }
  comparator_count <- sum(vapply(programmes, function(programme) {
    identical(programme$role, "comparator") || identical(programme$family, "comparator")
  }, logical(1)))
  ucr_count <- sum(vapply(programmes, function(programme) {
    identical(programme$family, "ucr") ||
      as.character(student_value(programme$role, "")) %in% c("ucr-alternative", "ucr-depth", "ucr-balanced", "ucr-thematic")
  }, logical(1)))
  if (comparator_count != 1 || ucr_count < 1 || ucr_count > 3) {
    stop("Student record ", expected_id, " has an invalid comparator/UCR alternative structure.")
  }
  comparator_flags <- vapply(programmes, function(programme) {
    identical(programme$role, "comparator") || identical(programme$family, "comparator")
  }, logical(1))
  ucr_flags <- vapply(programmes, function(programme) {
    identical(programme$family, "ucr") ||
      as.character(student_value(programme$role, "")) %in% c("ucr-alternative", "ucr-depth", "ucr-balanced", "ucr-thematic")
  }, logical(1))
  if (any(comparator_flags & ucr_flags)) {
    stop("Student record ", expected_id, " incorrectly classifies a comparator as a UCR alternative.")
  }
  programme_ids <- vapply(programmes, function(programme) as.character(student_value(programme$id, "")), character(1))
  if (any(!nzchar(programme_ids)) || anyDuplicated(programme_ids)) {
    stop("Student record ", expected_id, " must use unique nonblank programme ids.")
  }
  validate_student_programme_concepts(record, programmes, expected_id, required = identical(mode, "private"))
  if (!is.list(record$blocks) || !length(record$blocks)) {
    stop("Student record ", expected_id, " has no comparison blocks.")
  }
  invisible(TRUE)
}

load_student_data_config <- function(repo_root, requested_mode = Sys.getenv("UCR_STUDENT_DATA_MODE", unset = "auto")) {
  mode <- resolve_student_data_mode(repo_root, requested_mode)
  if (identical(mode, "private")) {
    private_root <- student_private_root(repo_root)
    marker_file <- file.path(private_root, "student-mode.json")
    marker <- read_student_json(marker_file, "private student mode marker")
    if (!identical(marker$mode, "private")) stop("Private student mode marker must declare mode private.")
    access_file <- file.path(private_root, "student-access.json")
    record_dir <- file.path(private_root, "student-records")
  } else {
    private_root <- NULL
    marker_file <- NULL
    marker <- NULL
    access_file <- file.path(repo_root, "pilot", "shiny", "data", "access_codes.json")
    record_dir <- file.path(repo_root, "data", "examples")
  }

  access_map <- read_student_json(access_file, paste(mode, "student access index"))
  entries <- access_map$entries
  if (!is.list(entries) || !length(entries)) stop("The ", mode, " student access index has no entries.")
  if (identical(mode, "private") && !identical(access_map$mode, "private")) {
    stop("Private student access index must declare mode private.")
  }

  normalized_codes <- vapply(entries, function(entry) normalize_student_code(entry$code), character(1))
  if (any(is.na(normalized_codes)) || any(!nzchar(normalized_codes))) {
    stop("Every student access-index entry must have a valid access code.")
  }
  if (anyDuplicated(normalized_codes)) stop("Student access codes must be unique after normalization.")

  ids <- vapply(entries, student_record_id, character(1), mode = mode)
  files <- vapply(entries, student_record_filename, character(1), mode = mode)
  if (any(!grepl("^[a-z0-9][a-z0-9-]*$", ids))) stop("Student record ids contain an invalid value.")
  if (anyDuplicated(ids)) stop("Student record ids must be unique.")
  if (any(!nzchar(files)) || any(files != basename(files)) || any(grepl("[/\\\\]", files))) {
    stop("Student recordFile values must be simple JSON filenames inside the student-records directory.")
  }
  if (any(!grepl("^[a-z0-9][a-z0-9-]*\\.json$", files))) stop("Student record filenames are invalid.")
  if (anyDuplicated(files)) stop("Student record filenames must be unique.")

  if (identical(mode, "private")) {
    private_pattern <- "^UCR-(?:[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{4}-){3}[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{4}$"
    displayed_codes <- vapply(entries, function(entry) as.character(student_value(entry$code, "")), character(1))
    if (any(!grepl(private_pattern, displayed_codes, perl = TRUE))) {
      stop("Private access codes must use the canonical UCR-XXXX-XXXX-XXXX-XXXX format and approved alphabet.")
    }
  }

  record_paths <- file.path(record_dir, files)
  missing <- record_paths[!file.exists(record_paths)]
  if (length(missing)) stop("Missing referenced student record(s): ", paste(missing, collapse = ", "))
  for (index in seq_along(record_paths)) {
    record <- read_student_json(record_paths[[index]], paste("student record", ids[[index]]))
    validate_student_record(record, ids[[index]], mode)
  }

  list(
    mode = mode,
    marker_file = marker_file,
    marker = marker,
    access_file = access_file,
    access_map = access_map,
    record_dir = record_dir,
    record_ids = ids,
    record_files = files,
    record_paths = record_paths,
    course_dir = file.path(repo_root, "pilot", "shiny", "data", "courses")
  )
}

find_student_entry <- function(config, submitted_code) {
  target <- normalize_student_code(submitted_code)
  if (is.na(target) || !nzchar(target)) return(NULL)
  entries <- config$access_map$entries
  matches <- vapply(entries, function(entry) identical(normalize_student_code(entry$code), target), logical(1))
  if (!any(matches)) return(NULL)
  entries[[which(matches)[[1]]]]
}

load_student_record_for_code <- function(config, submitted_code) {
  entry <- find_student_entry(config, submitted_code)
  if (is.null(entry)) return(NULL)
  id <- student_record_id(entry, config$mode)
  path <- file.path(config$record_dir, student_record_filename(entry, config$mode))
  record <- read_student_json(path, paste("student record", id))
  validate_student_record(record, id, config$mode)
  if (is.null(record$origin)) record$origin <- "student"
  record
}

validate_private_test_derivation <- function(config, repo_root) {
  if (!identical(config$mode, "private") || !identical(config$marker$datasetType, "five-public-fixture-test")) {
    stop("Private test derivation validation requires the marked five-public-fixture test dataset.")
  }
  expected_ids <- sprintf("p-%03d", 1:5)
  if (!identical(sort(config$record_ids), expected_ids)) stop("Private test dataset must contain exactly p-001 through p-005.")
  for (index in seq_along(config$record_ids)) {
    id <- config$record_ids[[index]]
    private_record <- read_student_json(config$record_paths[[index]], paste("private test record", id))
    public_record <- read_student_json(file.path(repo_root, "data", "examples", paste0(id, ".json")), paste("public source fixture", id))
    private_core <- private_record
    public_core <- public_record
    private_core$origin <- NULL
    private_core$interestInterpretation <- NULL
    public_core$origin <- NULL
    public_core$interestInterpretation <- NULL
    if (!identical(private_core, public_core)) {
      stop("Private test record ", id, " differs from its public source outside the permitted student fields.")
    }
  }
  invisible(TRUE)
}

student_course_file <- function(config, department) {
  if (!grepl("^[A-Z]{3}$", department)) stop("Invalid course department code.")
  file.path(config$course_dir, paste0(department, ".json"))
}
