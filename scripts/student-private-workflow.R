# Shared safety and persistence helpers for the local student-private workflow.

STUDENT_PRODUCTION_DATASET_TYPE <- "production-cumulative"
STUDENT_PRIVATE_CODE_ALPHABET <- strsplit("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", "", fixed = TRUE)[[1]]
STUDENT_PRIVATE_CODE_PATTERN <- "^UCR-(?:[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{4}-){3}[ABCDEFGHJKLMNPQRSTUVWXYZ23456789]{4}$"
STUDENT_OPTIONAL_RESEARCH_ID <- "optional-independent-research"
STUDENT_OPTIONAL_RESEARCH_TEXT <- "Optional independent research"
STUDENT_OPTIONAL_RESEARCH_CREDITS <- 15

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
    code_sheet = file.path(private_root, "student-last-batch-codes.csv"),
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
    generator = "scripts/add-students-private.R"
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

student_code_sheet_lines <- function(entries) {
  ids <- vapply(entries, function(entry) as.character(student_value(entry$recordId, "")), character(1))
  codes <- vapply(entries, function(entry) as.character(student_value(entry$code, "")), character(1))
  c("record_id,access_code", paste(ids, codes, sep = ","))
}

student_trimmed_string <- function(value) {
  if (is.null(value) || length(value) != 1L || is.na(value)) return("")
  trimws(as.character(value))
}

student_normalized_label <- function(value) {
  tolower(gsub("[[:space:]]+", " ", student_trimmed_string(value)))
}

student_credit_number <- function(value) {
  if (is.null(value) || length(value) != 1L || is.na(value)) return(NA_real_)
  if (is.numeric(value) && is.finite(value)) return(as.numeric(value))
  text <- gsub(",", ".", student_trimmed_string(value), fixed = TRUE)
  match <- regexpr("-?[0-9]+(?:\\.[0-9]+)?", text, perl = TRUE)
  if (match[[1]] < 0L) return(NA_real_)
  as.numeric(regmatches(text, match))
}

student_is_comparator_programme <- function(programme) {
  identical(programme$role, "comparator") || identical(programme$family, "comparator")
}

student_is_ucr_programme <- function(programme) {
  identical(programme$family, "ucr") ||
    student_trimmed_string(programme$role) %in% c(
      "ucr-alternative", "ucr-depth", "ucr-balanced", "ucr-thematic"
    )
}

student_scheduled_courses <- function(programme) {
  semesters <- student_value(programme$schedule$semesters, list())
  unlist(lapply(semesters, function(semester) student_value(semester$courses, list())), recursive = FALSE)
}

student_course_key <- function(course) {
  key <- student_trimmed_string(course$code)
  if (!nzchar(key)) key <- student_trimmed_string(course$name)
  tolower(key)
}

student_course_credits <- function(course) {
  credits <- student_credit_number(student_value(course$credits, 7.5))
  if (is.na(credits)) 0 else credits
}

student_is_advanced_course <- function(course) {
  level <- student_credit_number(course$level)
  !is.na(level) && (level >= 300 || (level >= 3 && level < 10))
}

student_normalize_comparison_cell <- function(cell) {
  if (is.null(cell)) return(NULL)
  if (is.character(cell) && length(cell) == 1L && nzchar(trimws(cell))) {
    return(list(text = cell))
  }
  if (is.list(cell) && nzchar(student_trimmed_string(cell$text))) return(cell)
  NULL
}

student_is_optional_research_cell <- function(cell) {
  isTRUE(cell$comparisonOnly) &&
    identical(student_trimmed_string(cell$comparisonElementId), STUDENT_OPTIONAL_RESEARCH_ID)
}

student_comparison_entries <- function(blocks, programme_id) {
  entries <- list()
  for (block_index in seq_along(blocks)) {
    block <- blocks[[block_index]]
    rows <- student_value(block$rows, list())
    for (row_index in seq_along(rows)) {
      cells <- rows[[row_index]]$cells
      cell <- if (is.list(cells)) student_normalize_comparison_cell(cells[[programme_id]]) else NULL
      if (!is.null(cell)) {
        entries[[length(entries) + 1L]] <- list(
          cell = cell,
          block = block,
          row_index = row_index
        )
      }
    }
  }
  entries
}

student_is_retained_legacy_fixture <- function(repo_root, record) {
  id <- student_trimmed_string(record$id)
  if (!grepl("^p-00[1-5]$", id)) return(FALSE)
  fixture_path <- file.path(repo_root, "data", "examples", paste0(id, ".json"))
  if (!file.exists(fixture_path)) return(FALSE)
  fixture <- read_student_json(fixture_path, paste("public source fixture", id))
  private_core <- record
  public_core <- fixture
  private_core$origin <- NULL
  private_core$interestInterpretation <- NULL
  public_core$origin <- NULL
  public_core$interestInterpretation <- NULL
  identical(private_core, public_core)
}

validate_student_record_mechanically <- function(repo_root, record_path, label = basename(record_path)) {
  record <- read_student_json(record_path, paste("student record", label))
  retained_legacy_fixture <- student_is_retained_legacy_fixture(repo_root, record)
  errors <- character()
  fail <- function(message) errors <<- c(errors, message)
  approximately_equal <- function(left, right) {
    !is.na(left) && !is.na(right) && abs(left - right) < 0.001
  }

  comparator <- student_value(record$comparator, record$referenceProgramme)
  if (!is.list(comparator)) {
    fail("comparator metadata is required")
  } else {
    if (!nzchar(student_trimmed_string(comparator$name))) fail("comparator.name is required")
    if (!nzchar(student_trimmed_string(comparator$institution))) fail("comparator.institution is required")
    source_url <- student_trimmed_string(comparator$primarySourceUrl)
    if (!grepl("^https?://[^[:space:]]+$", source_url, perl = TRUE)) {
      fail("comparator.primarySourceUrl must be an http(s) URL")
    }
  }

  programmes <- record$programmes
  if (!is.list(programmes) || length(programmes) < 2L || length(programmes) > 4L) {
    fail("programmes must contain one comparator followed by one to three UCR alternatives")
    programmes <- list()
  }
  if (length(programmes)) {
    if (!student_is_comparator_programme(programmes[[1]])) fail("programme 1 must be the comparator")
    if (length(programmes) > 1L) {
      for (index in 2:length(programmes)) {
        if (!student_is_ucr_programme(programmes[[index]]) || student_is_comparator_programme(programmes[[index]])) {
          fail(paste0("programme ", index, " must be a UCR alternative"))
        }
      }
    }
  }

  for (index in seq_along(programmes)) {
    programme <- programmes[[index]]
    if (index == 1L) next
    programme_id <- student_trimmed_string(programme$id)
    semesters <- programme$schedule$semesters
    if (!is.list(semesters) || length(semesters) != 6L) {
      fail(paste0("UCR programme ", programme_id, " must have exactly six semesters"))
      next
    }
    for (semester_index in seq_along(semesters)) {
      courses <- semesters[[semester_index]]$courses
      if (!is.list(courses) || length(courses) != 4L) {
        fail(paste0(
          "UCR programme ", programme_id, ", semester ", semester_index,
          ": expected four courses"
        ))
      }
    }
    courses <- student_scheduled_courses(programme)
    course_keys <- vapply(courses, student_course_key, character(1))
    if (length(courses) != 24L || length(unique(course_keys[nzchar(course_keys)])) != 24L) {
      fail(paste0("UCR programme ", programme_id, " must contain exactly 24 unique scheduled courses"))
    }
    advanced_count <- sum(vapply(courses, student_is_advanced_course, logical(1)))
    if (advanced_count < 6L) {
      fail(paste0(
        "UCR programme ", programme_id, " has ", advanced_count,
        " 300-level courses; at least 6 are required"
      ))
    }
    ppd_locations <- integer()
    for (semester_index in seq_along(semesters)) {
      codes <- vapply(
        student_value(semesters[[semester_index]]$courses, list()),
        function(course) toupper(student_trimmed_string(course$code)),
        character(1)
      )
      if (any(codes == "ACCPPDE101")) ppd_locations <- c(ppd_locations, rep(semester_index, sum(codes == "ACCPPDE101")))
    }
    if (length(ppd_locations) != 1L) {
      fail(paste0("UCR programme ", programme_id, " must schedule ACCPPDE101 exactly once"))
    } else if (ppd_locations[[1]] > 2L) {
      fail(paste0("UCR programme ", programme_id, " must schedule ACCPPDE101 in Year 1"))
    }
  }

  blocks <- student_value(record$blocks, list())
  for (programme_index in seq_along(programmes)) {
    programme <- programmes[[programme_index]]
    programme_id <- student_trimmed_string(programme$id)
    if (!nzchar(programme_id)) next
    entries <- student_comparison_entries(blocks, programme_id)
    comparison_only <- vapply(entries, function(entry) {
      isTRUE(entry$cell$comparisonOnly) || nzchar(student_trimmed_string(entry$cell$comparisonElementId))
    }, logical(1))
    optional_research <- vapply(entries, function(entry) {
      student_is_optional_research_cell(entry$cell)
    }, logical(1))
    invalid_comparison_only <- comparison_only & !optional_research
    if (any(invalid_comparison_only)) {
      fail(paste0("comparison ", programme_id, " contains an unknown comparison-only element"))
    }
    for (entry in entries[optional_research]) {
      if (!identical(student_trimmed_string(entry$cell$text), STUDENT_OPTIONAL_RESEARCH_TEXT) ||
          !approximately_equal(student_credit_number(entry$cell$credits), STUDENT_OPTIONAL_RESEARCH_CREDITS)) {
        fail(paste0(
          "comparison ", programme_id,
          " has invalid Optional independent research text or credits"
        ))
      }
    }
    if (student_is_ucr_programme(programme)) {
      if (!retained_legacy_fixture && sum(optional_research) != 1L) {
        fail(paste0(
          "comparison ", programme_id,
          " must contain Optional independent research exactly once"
        ))
      }
    } else if (any(optional_research)) {
      fail("the comparator must not contain the UCR-only Optional independent research element")
    }
    curriculum_entries <- entries[!comparison_only]
    credits <- vapply(curriculum_entries, function(entry) student_credit_number(entry$cell$credits), numeric(1))
    if (length(credits) && all(!is.na(credits)) && !approximately_equal(sum(credits), 180)) {
      fail(paste0(
        "comparison ", programme_id, " totals ", sum(credits),
        " EC; every programme comparison must total 180 EC"
      ))
    } else if (!length(credits) || any(is.na(credits)) || any(credits <= 0)) {
      fail(paste0("comparison ", programme_id, " requires positive explicit numeric credits"))
    }

    if (student_is_ucr_programme(programme)) {
      courses <- student_scheduled_courses(programme)
      course_codes <- vapply(courses, function(course) tolower(student_trimmed_string(course$code)), character(1))
      course_names <- vapply(courses, function(course) student_normalized_label(course$name), character(1))
      seen <- character()
      for (entry in curriculum_entries) {
        cell <- entry$cell
        cell_code <- tolower(student_trimmed_string(cell$courseCode))
        matches <- if (nzchar(cell_code)) which(course_codes == cell_code) else which(course_names == student_normalized_label(cell$text))
        if (length(matches) != 1L) {
          reference <- if (nzchar(cell_code)) cell_code else student_trimmed_string(cell$text)
          fail(paste0("comparison ", programme_id, ": ", reference, " does not identify exactly one scheduled UCR course"))
          next
        }
        course <- courses[[matches[[1]]]]
        key <- student_course_key(course)
        if (key %in% seen) fail(paste0("comparison ", programme_id, ": duplicate course ", key))
        seen <- c(seen, key)
        if (!identical(student_normalized_label(cell$text), student_normalized_label(course$name))) {
          fail(paste0("comparison ", programme_id, ": displayed course text does not match the scheduled course"))
        }
        if (!approximately_equal(student_credit_number(cell$credits), student_course_credits(course))) {
          fail(paste0("comparison ", programme_id, ": displayed course credits do not match the scheduled course"))
        }
      }
      missing <- courses[!vapply(courses, function(course) student_course_key(course) %in% seen, logical(1))]
      if (length(missing)) {
        names <- vapply(missing, function(course) student_trimmed_string(student_value(course$code, course$name)), character(1))
        fail(paste0(
          "comparison ", programme_id, ": scheduled courses missing from comparison: ",
          paste(names, collapse = ", ")
        ))
      }
    } else if (
      student_is_comparator_programme(programme) &&
        is.list(comparator) &&
        is.list(comparator$components) &&
        length(comparator$components)
    ) {
      components <- comparator$components
      component_ids <- vapply(components, function(component) student_trimmed_string(component$id), character(1))
      component_credits <- vapply(components, function(component) student_credit_number(component$credits), numeric(1))
      if (any(!nzchar(component_ids)) || anyDuplicated(component_ids)) fail("comparator.components requires unique stable ids")
      if (any(is.na(component_credits)) || any(component_credits <= 0) || !approximately_equal(sum(component_credits), 180)) {
        fail(paste0("comparator.components total ", sum(component_credits, na.rm = TRUE), " EC; reconstructed comparator must total 180 EC"))
      }
      seen_components <- character()
      for (entry in curriculum_entries) {
        component_id <- student_trimmed_string(entry$cell$componentId)
        match <- which(component_ids == component_id)
        if (!nzchar(component_id) || length(match) != 1L) {
          fail("comparison comparator: every cell must reference exactly one canonical component")
          next
        }
        if (component_id %in% seen_components) fail(paste0("comparison comparator: duplicate component ", component_id))
        seen_components <- c(seen_components, component_id)
        component <- components[[match[[1]]]]
        if (!identical(student_normalized_label(entry$cell$text), student_normalized_label(component$name))) {
          fail("comparison comparator: displayed text does not match the referenced component")
        }
        if (!approximately_equal(student_credit_number(entry$cell$credits), student_credit_number(component$credits))) {
          fail("comparison comparator: displayed credits do not match the referenced component")
        }
      }
      missing_components <- setdiff(component_ids, seen_components)
      if (length(missing_components)) {
        fail(paste0("comparison comparator: canonical components missing from comparison: ", paste(missing_components, collapse = ", ")))
      }
    }
  }

  if (!retained_legacy_fixture) {
    ucr_programmes <- programmes[vapply(programmes, student_is_ucr_programme, logical(1))]
    if (length(ucr_programmes) > 1L) {
      for (left_index in seq_len(length(ucr_programmes) - 1L)) {
        for (right_index in (left_index + 1L):length(ucr_programmes)) {
          left <- ucr_programmes[[left_index]]
          right <- ucr_programmes[[right_index]]
          left_courses <- student_scheduled_courses(left)
          right_courses <- student_scheduled_courses(right)
          left_keys <- unique(vapply(left_courses, student_course_key, character(1)))
          right_keys <- unique(vapply(right_courses, student_course_key, character(1)))
          left_distinct <- setdiff(left_keys, right_keys)
          right_distinct <- setdiff(right_keys, left_keys)
          left_ec <- sum(vapply(left_courses[vapply(left_courses, function(course) student_course_key(course) %in% left_distinct, logical(1))], student_course_credits, numeric(1)))
          right_ec <- sum(vapply(right_courses[vapply(right_courses, function(course) student_course_key(course) %in% right_distinct, logical(1))], student_course_credits, numeric(1)))
          if (length(left_distinct) < 4L || length(right_distinct) < 4L || left_ec + 0.001 < 30 || right_ec + 0.001 < 30) {
            fail(paste0(
              "UCR alternatives ", left$id, " and ", right$id,
              " are not substantively distinct: each alternative must differ by at least 4 courses / 30 EC"
            ))
          }
        }
      }
    }
  }

  if (length(errors)) {
    stop("Mechanical validation failed for ", label, ":\n", paste(unique(errors), collapse = "\n"))
  }
  invisible(TRUE)
}

validate_student_production_dataset <- function(
  repo_root,
  allow_empty = FALSE,
  allow_unindexed_records = FALSE
) {
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
  missing_files <- setdiff(files, disk_files)
  unindexed_files <- setdiff(disk_files, files)
  if (length(missing_files)) {
    stop(
      "The private access index refers to missing student-record files: ",
      paste(missing_files, collapse = ", ")
    )
  }
  if (length(unindexed_files) && !allow_unindexed_records) {
    stop(
      "Unregistered JSON files are present in private/student-records: ",
      paste(unindexed_files, collapse = ", "),
      ". Run scripts/add-students-private.R before validation or deployment."
    )
  }
  for (index in seq_along(entries)) {
    record_path <- file.path(paths$record_dir, files[[index]])
    record <- read_student_json(record_path, paste("production student record", ids[[index]]))
    validate_student_record(record, ids[[index]], "private")
    validate_student_record_mechanically(repo_root, record_path, ids[[index]])
  }

  list(
    paths = paths,
    marker = marker,
    access = access,
    entries = entries,
    codes = codes,
    ids = ids,
    files = files,
    unindexed_files = unindexed_files
  )
}

validate_existing_private_dataset_for_migration <- function(repo_root) {
  paths <- student_production_paths(repo_root)
  required <- c(paths$marker, paths$access, paths$record_dir)
  if (any(!file.exists(required) & !dir.exists(required))) return(NULL)

  marker <- read_student_json(paths$marker, "private student mode marker")
  access <- read_student_json(paths$access, "private student access index")
  if (!identical(marker$mode, "private") || !identical(access$mode, "private")) {
    return(NULL)
  }

  entries <- access$entries
  if (is.null(entries)) entries <- list()
  if (!is.list(entries)) stop("Existing private student access-index entries must be an array.")

  codes <- vapply(entries, function(entry) as.character(student_value(entry$code, "")), character(1))
  normalized_codes <- vapply(codes, normalize_student_code, character(1))
  ids <- vapply(entries, function(entry) as.character(student_value(entry$recordId, "")), character(1))
  files <- vapply(entries, function(entry) as.character(student_value(entry$recordFile, "")), character(1))

  if (length(entries)) {
    if (any(!grepl(STUDENT_PRIVATE_CODE_PATTERN, codes, perl = TRUE)) || anyDuplicated(normalized_codes)) {
      stop("Existing private student access codes are not canonical and unique; refusing metadata migration.")
    }
    if (any(!grepl("^[a-z0-9][a-z0-9-]*$", ids)) || anyDuplicated(ids)) {
      stop("Existing private student record ids are not valid and unique; refusing metadata migration.")
    }
    if (any(!grepl("^[a-z0-9][a-z0-9-]*\\.json$", files)) || any(files != basename(files)) || anyDuplicated(files)) {
      stop("Existing private student record filenames are not simple, valid and unique; refusing metadata migration.")
    }
  }

  disk_files <- sort(list.files(paths$record_dir, pattern = "\\.json$", all.files = FALSE, no.. = TRUE))
  missing_files <- setdiff(files, disk_files)
  if (length(missing_files)) {
    stop(
      "Existing private access index refers to missing student-record files: ",
      paste(missing_files, collapse = ", "),
      ". Refusing metadata migration."
    )
  }

  for (index in seq_along(entries)) {
    record_path <- file.path(paths$record_dir, files[[index]])
    record <- read_student_json(
      record_path,
      paste("existing private student record", ids[[index]])
    )
    validate_student_record(record, ids[[index]], "private")
    validate_student_record_mechanically(repo_root, record_path, ids[[index]])
  }

  list(
    marker = marker,
    access = access,
    entries = entries,
    codes = codes,
    ids = ids,
    files = files,
    unindexed_files = setdiff(disk_files, files)
  )
}

migrate_private_dataset_to_production <- function(repo_root) {
  paths <- student_production_paths(repo_root)
  required <- c(paths$marker, paths$access, paths$record_dir)
  if (any(!file.exists(required) & !dir.exists(required))) return(FALSE)

  marker <- read_student_json(paths$marker, "private student mode marker")
  access <- read_student_json(paths$access, "private student access index")
  already_production <- identical(marker$mode, "private") &&
    identical(marker$datasetType, STUDENT_PRODUCTION_DATASET_TYPE) &&
    identical(access$mode, "private") &&
    identical(access$datasetType, STUDENT_PRODUCTION_DATASET_TYPE)
  if (already_production) return(FALSE)

  existing <- validate_existing_private_dataset_for_migration(repo_root)
  if (is.null(existing)) {
    stop("Existing private student dataset cannot be safely migrated to cumulative production mode.")
  }

  new_marker <- existing$marker
  new_marker$schemaVersion <- as.character(student_value(new_marker$schemaVersion, "1.0"))
  new_marker$mode <- "private"
  new_marker$datasetType <- STUDENT_PRODUCTION_DATASET_TYPE
  new_marker$generator <- "scripts/add-students-private.R"

  new_access <- existing$access
  new_access$schemaVersion <- as.character(student_value(new_access$schemaVersion, "1.0"))
  new_access$mode <- "private"
  new_access$datasetType <- STUDENT_PRODUCTION_DATASET_TYPE
  new_access$entries <- existing$entries

  old_marker <- readBin(paths$marker, what = "raw", n = file.info(paths$marker)$size)
  old_access <- readBin(paths$access, what = "raw", n = file.info(paths$access)$size)
  migrated <- FALSE
  tryCatch({
    student_write_json_atomic(new_marker, paths$marker)
    student_write_json_atomic(new_access, paths$access)
    migrated_dataset <- validate_student_production_dataset(
      repo_root,
      allow_empty = TRUE,
      allow_unindexed_records = TRUE
    )
    if (!identical(migrated_dataset$ids, existing$ids) ||
        !identical(migrated_dataset$codes, existing$codes) ||
        !identical(migrated_dataset$files, existing$files)) {
      stop("Metadata migration changed existing student records, codes, or filenames.")
    }
    migrated <- TRUE
  }, error = function(e) {
    marker_connection <- file(paths$marker, open = "wb")
    writeBin(old_marker, marker_connection)
    close(marker_connection)
    access_connection <- file(paths$access, open = "wb")
    writeBin(old_access, access_connection)
    close(access_connection)
    stop("Private student metadata migration was rolled back: ", conditionMessage(e))
  })

  migrated
}

initialize_student_production_dataset <- function(repo_root, allow_unindexed_records = FALSE) {
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
  } else if (
    allow_unindexed_records &&
      dir.exists(paths$record_dir) &&
      !file.exists(paths$marker) &&
      !file.exists(paths$access)
  ) {
    top_level <- setdiff(
      list.files(paths$root, all.files = TRUE, no.. = TRUE),
      c(basename(paths$record_dir), basename(paths$lock))
    )
    record_items <- list.files(paths$record_dir, all.files = TRUE, no.. = TRUE)
    invalid_record_items <- record_items[!grepl("^[a-z0-9][a-z0-9-]*\\.json$", record_items)]
    if (length(top_level) || length(invalid_record_items)) {
      stop(
        "Refusing to initialize around unexpected files in private/. Keep only lower-case JSON records in ",
        "private/student-records for first-time registration."
      )
    }
    student_write_json_atomic(student_production_marker(), paths$marker)
    student_write_json_atomic(student_production_access_index(), paths$access)
  } else if (!all(existing)) {
    stop("Incomplete private student dataset; refusing to initialize over partial data.")
  }
  validate_student_production_dataset(
    repo_root,
    allow_empty = TRUE,
    allow_unindexed_records = allow_unindexed_records
  )
}

register_unindexed_student_records <- function(repo_root, lock_already_held = FALSE) {
  assert_private_tree_ignored(repo_root)
  paths <- student_production_paths(repo_root)
  if (!lock_already_held) {
    lock <- acquire_student_production_lock(repo_root)
    on.exit(release_student_production_lock(lock), add = TRUE)
  }

  migrated_private_dataset <- migrate_private_dataset_to_production(repo_root)
  initialize_student_production_dataset(repo_root, allow_unindexed_records = TRUE)
  current <- validate_student_production_dataset(
    repo_root,
    allow_empty = TRUE,
    allow_unindexed_records = TRUE
  )
  incoming_files <- current$unindexed_files
  if (!length(incoming_files)) {
    student_write_text_atomic(student_code_sheet_lines(current$entries), paths$code_sheet)
    return(list(
      records = list(),
      codeSheet = paths$code_sheet,
      migratedPrivateDataset = migrated_private_dataset
    ))
  }

  incoming <- lapply(seq_along(incoming_files), function(index) {
    filename <- incoming_files[[index]]
    source <- file.path(paths$record_dir, filename)
    record <- read_student_json(source, paste("unregistered student record", filename))
    id <- as.character(student_value(record$id, ""))
    validate_student_record(record, id, "private")
    validate_student_record_mechanically(repo_root, source, id)
    expected_filename <- paste0(id, ".json")
    if (!identical(filename, expected_filename)) {
      stop(
        "Student record filename must match its id exactly: expected ",
        expected_filename,
        " but found ",
        filename,
        "."
      )
    }
    list(record = record, id = id, filename = filename, source = source)
  })
  incoming_ids <- vapply(incoming, function(item) item$id, character(1))
  if (anyDuplicated(incoming_ids)) stop("The unregistered batch contains duplicate student record ids.")
  duplicate_ids <- intersect(incoming_ids, current$ids)
  if (length(duplicate_ids)) stop("Student record id already exists: ", paste(duplicate_ids, collapse = ", "))

  forbidden <- unique(c(
    vapply(current$codes, normalize_student_code, character(1)),
    student_public_development_codes(repo_root)
  ))
  codes <- character(length(incoming))
  for (index in seq_along(incoming)) {
    for (attempt in seq_len(1000L)) {
      candidate <- student_random_access_code()
      normalized <- normalize_student_code(candidate)
      generated <- codes[nzchar(codes)]
      generated <- vapply(generated, normalize_student_code, character(1))
      if (!normalized %in% c(forbidden, generated)) {
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
  code_sheet_lines <- student_code_sheet_lines(updated_index$entries)
  old_access <- readBin(paths$access, what = "raw", n = file.info(paths$access)$size)

  committed <- FALSE
  tryCatch({
    student_write_json_atomic(updated_index, paths$access)
    validate_student_production_dataset(repo_root)
    student_write_text_atomic(code_sheet_lines, paths$code_sheet)
    committed <- TRUE
  }, error = function(e) {
    connection <- file(paths$access, open = "wb")
    writeBin(old_access, connection)
    close(connection)
    stop("Student registration was rolled back: ", conditionMessage(e))
  })
  if (!committed) stop("Student registration did not complete.")

  list(
    records = lapply(seq_along(incoming), function(index) {
      list(recordId = incoming_ids[[index]], accessCode = codes[[index]], recordFile = incoming[[index]]$source)
    }),
    codeSheet = paths$code_sheet,
    migratedPrivateDataset = migrated_private_dataset
  )
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
    validate_student_record_mechanically(repo_root, record_paths[[index]], id)
    list(record = record, id = id, filename = paste0(id, ".json"), source = record_paths[[index]])
  })
  incoming_ids <- vapply(incoming, function(item) item$id, character(1))
  incoming_files <- vapply(incoming, function(item) item$filename, character(1))
  if (anyDuplicated(incoming_ids)) stop("The batch contains duplicate student record ids.")
  if (anyDuplicated(incoming_files)) stop("The batch contains duplicate student record filenames.")

  lock <- acquire_student_production_lock(repo_root)
  on.exit(release_student_production_lock(lock), add = TRUE)
  if (!dir.exists(paths$record_dir) && !dir.create(paths$record_dir, recursive = TRUE, showWarnings = FALSE)) {
    stop("Could not create ", paths$record_dir)
  }

  destinations <- file.path(paths$record_dir, incoming_files)
  published <- character()
  for (index in seq_along(incoming)) {
    destination <- destinations[[index]]
    same_file <- file.exists(destination) && identical(
      normalizePath(incoming[[index]]$source, winslash = "/", mustWork = TRUE),
      normalizePath(destination, winslash = "/", mustWork = TRUE)
    )
    if (same_file) next
    if (file.exists(destination)) {
      stop("Student record file already exists: ", destination)
    }
    student_write_json_atomic(incoming[[index]]$record, destination)
    published <- c(published, destination)
  }

  committed <- FALSE
  on.exit(if (!committed && length(published)) unlink(published[file.exists(published)]), add = TRUE)
  registered <- register_unindexed_student_records(repo_root, lock_already_held = TRUE)
  registered_ids <- vapply(registered$records, function(item) item$recordId, character(1))
  if (!all(incoming_ids %in% registered_ids)) {
    stop("Compatibility import did not register every supplied student record as new.")
  }
  committed <- TRUE

  list(
    records = registered$records[registered_ids %in% incoming_ids],
    codeSheet = registered$codeSheet,
    migratedPrivateDataset = registered$migratedPrivateDataset
  )
}

add_student_production_record <- function(repo_root, record_path) {
  batch <- add_student_production_records(repo_root, record_path)
  result <- batch$records[[1]]
  result$codeSheet <- batch$codeSheet
  result$migratedPrivateDataset <- batch$migratedPrivateDataset
  result
}
