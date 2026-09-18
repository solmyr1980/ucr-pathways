#!/usr/bin/env Rscript

# Create the ignored five-record private dataset used to test the student-app
# deployment path. This script never edits the tracked public fixtures.

args <- commandArgs(trailingOnly = TRUE)
known <- args %in% c("--reset-test", "--quiet")
if (any(!known)) stop("Unknown argument: ", args[!known][[1]])
if (sum(args == "--reset-test") > 1) stop("Specify --reset-test only once.")
if (sum(args == "--quiet") > 1) stop("Specify --quiet only once.")
reset_test <- "--reset-test" %in% args
quiet <- "--quiet" %in% args

script_argument <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (!length(script_argument)) stop("Run this file with Rscript.")
script_path <- normalizePath(sub("^--file=", "", script_argument[[1]]), winslash = "/", mustWork = TRUE)
repo_root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Install the jsonlite package before initializing the private test dataset.")
}
if (!requireNamespace("openssl", quietly = TRUE)) {
  stop("Install the openssl package before initializing the private test dataset.")
}

source(file.path(repo_root, "scripts", "student-private-workflow.R"), local = TRUE)
source(file.path(repo_root, "pilot", "shiny", "student-data.R"), local = TRUE)
assert_private_tree_ignored(repo_root)

test_ids <- sprintf("p-%03d", 1:5)
interpretations <- c(
  "p-001" = "Economic development and inequality, and how political institutions and public policy shape prosperity.",
  "p-002" = "Astronomy and space exploration viewed through physics, data analysis, technology, and the societal choices surrounding space activity.",
  "p-003" = "How language, creative writing, media, and consumer psychology shape communication and advertising.",
  "p-004" = "Crime, punishment, and fairness examined through law, philosophy, politics, psychology, and social institutions.",
  "p-005" = "Mathematical and analytical problem-solving applied to climate change and practical environmental challenges."
)

private_root <- student_private_root(repo_root)
record_dir <- file.path(private_root, "student-records")
marker_file <- file.path(private_root, "student-mode.json")
access_file <- file.path(private_root, "student-access.json")
codes_file <- file.path(private_root, "student-test-codes.txt")
guarded_paths <- c(marker_file, access_file, codes_file, record_dir)

write_json_atomic <- function(value, path) {
  temporary <- tempfile(pattern = paste0(basename(path), "."), tmpdir = dirname(path))
  on.exit(if (file.exists(temporary)) unlink(temporary), add = TRUE)
  jsonlite::write_json(value, temporary, auto_unbox = TRUE, pretty = TRUE, null = "null")
  if (!file.rename(temporary, path)) stop("Could not write ", path)
}

write_text_atomic <- function(lines, path) {
  temporary <- tempfile(pattern = paste0(basename(path), "."), tmpdir = dirname(path))
  on.exit(if (file.exists(temporary)) unlink(temporary), add = TRUE)
  writeLines(lines, temporary, useBytes = TRUE)
  if (!file.rename(temporary, path)) stop("Could not write ", path)
}

if (any(file.exists(guarded_paths) | dir.exists(guarded_paths))) {
  if (!reset_test) {
    stop(
      "Private student data already exist. Nothing was changed. ",
      "Use --reset-test only to replace a dataset previously created by this test initializer."
    )
  }
  marker <- read_student_json(marker_file, "private test marker")
  if (!identical(marker$datasetType, "five-public-fixture-test") ||
      !identical(marker$generator, "scripts/init-student-private-test.R")) {
    stop("Refusing --reset-test because the existing private dataset is not marked as this five-case test dataset.")
  }
  old_index <- read_student_json(access_file, "existing private test access index")
  old_ids <- sort(vapply(old_index$entries, function(entry) as.character(student_value(entry$recordId, "")), character(1)))
  old_files <- sort(vapply(old_index$entries, function(entry) as.character(student_value(entry$recordFile, "")), character(1)))
  disk_files <- if (dir.exists(record_dir)) sort(list.files(record_dir, all.files = FALSE, no.. = TRUE)) else character()
  if (!identical(old_ids, sort(test_ids)) || !identical(old_files, paste0(sort(test_ids), ".json")) ||
      !identical(disk_files, old_files)) {
    stop("Refusing --reset-test because the existing private record set is not exactly the generated five-case test dataset.")
  }
  explicit_files <- c(file.path(record_dir, old_files), access_file, marker_file, codes_file)
  unlink(explicit_files[file.exists(explicit_files)])
}

if (!dir.exists(record_dir) && !dir.create(record_dir, recursive = TRUE, showWarnings = FALSE)) {
  stop("Could not create ", record_dir)
}

alphabet <- strsplit("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", "", fixed = TRUE)[[1]]
random_code <- function() {
  bits <- as.integer(rawToBits(openssl::rand_bytes(10)))
  groups <- matrix(bits, ncol = 5, byrow = TRUE)
  values <- as.integer(groups %*% (2^(0:4))) + 1L
  characters <- alphabet[values]
  paste("UCR", paste(vapply(split(characters, rep(1:4, each = 4)), paste0, collapse = "", FUN.VALUE = character(1)), collapse = "-"), sep = "-")
}

public_index <- read_student_json(
  file.path(repo_root, "pilot", "shiny", "data", "access_codes.json"),
  "public pilot access index"
)
forbidden <- vapply(public_index$entries, function(entry) normalize_student_code(entry$code), character(1))
codes <- character()
while (length(codes) < length(test_ids)) {
  candidate <- random_code()
  normalized <- normalize_student_code(candidate)
  if (!normalized %in% c(forbidden, vapply(codes, normalize_student_code, character(1)))) {
    codes <- c(codes, candidate)
  }
}

entries <- vector("list", length(test_ids))
for (index in seq_along(test_ids)) {
  id <- test_ids[[index]]
  source_file <- file.path(repo_root, "data", "examples", paste0(id, ".json"))
  record <- read_student_json(source_file, paste("public fixture", id))
  original_interests <- record$interests
  record$origin <- "student"
  record$interestInterpretation <- unname(interpretations[[id]])
  if (!identical(record$interests, original_interests)) stop("Initializer altered the original interest statement for ", id)
  destination <- file.path(record_dir, paste0(id, ".json"))
  write_json_atomic(record, destination)
  entries[[index]] <- list(code = codes[[index]], recordId = id, recordFile = paste0(id, ".json"))
}

access_index <- list(
  schemaVersion = "1.0",
  mode = "private",
  datasetType = "five-public-fixture-test",
  entries = entries
)
marker <- list(
  schemaVersion = "1.0",
  mode = "private",
  datasetType = "five-public-fixture-test",
  generator = "scripts/init-student-private-test.R"
)
write_json_atomic(access_index, access_file)
write_json_atomic(marker, marker_file)

code_lines <- c(
  "UCR student-app private five-case test codes",
  "Generated locally. Keep this file private.",
  "",
  sprintf("%s  %s", test_ids, codes)
)
write_text_atomic(code_lines, codes_file)

config <- load_student_data_config(repo_root, "private")
if (!identical(sort(config$record_ids), sort(test_ids))) stop("Generated private dataset did not validate as expected.")
validate_private_test_derivation(config, repo_root)

if (quiet) {
  cat("Private five-case student test dataset created; codes saved in the ignored local code file.\n")
} else {
  cat(
    "Private five-case student test dataset created.\n",
    "Access codes:\n",
    paste(sprintf("  %s  %s", test_ids, codes), collapse = "\n"),
    "\n\nSaved for later reference in: private/student-test-codes.txt\n",
    sep = ""
  )
}
