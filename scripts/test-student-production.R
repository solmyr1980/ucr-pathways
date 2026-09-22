#!/usr/bin/env Rscript

# Test cumulative production behavior in an isolated synthetic repository.
# This script never reads, writes or removes the operator's real /private/ tree.

required_packages <- c("jsonlite", "openssl", "shiny", "rsconnect")
missing_packages <- required_packages[!vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing_packages)) stop("Install required test packages: ", paste(missing_packages, collapse = ", "))

repo_root <- normalizePath(".", winslash = "/", mustWork = TRUE)
source(file.path(repo_root, "pilot", "shiny", "student-data.R"), local = TRUE)
source(file.path(repo_root, "scripts", "student-private-workflow.R"), local = TRUE)

expect_error <- function(expression) inherits(try(force(expression), silent = TRUE), "try-error")
test_root <- tempfile("student-production-repo-")
dir.create(test_root)
on.exit(unlink(test_root, recursive = TRUE), add = TRUE)

copy_relative <- function(relative, destination_root = test_root) {
  source_path <- file.path(repo_root, relative)
  destination <- file.path(destination_root, relative)
  if (!file.exists(source_path) && !dir.exists(source_path)) stop("Missing test source: ", source_path)
  dir.create(dirname(destination), recursive = TRUE, showWarnings = FALSE)
  if (dir.exists(source_path)) {
    dir.create(destination, recursive = TRUE, showWarnings = FALSE)
    children <- list.files(source_path, full.names = TRUE, all.files = TRUE, no.. = TRUE)
    if (length(children) && !all(file.copy(children, destination, recursive = TRUE, copy.mode = TRUE))) {
      stop("Could not copy test directory: ", relative)
    }
  } else if (!file.copy(source_path, destination, copy.mode = TRUE)) {
    stop("Could not copy test file: ", relative)
  }
}

for (relative in c(
  ".gitignore",
  "scripts/student-private-workflow.R",
  "scripts/add-students-private.R",
  "scripts/deploy-student-shiny.R",
  "scripts/validate-and-deploy-student.R",
  "pilot/shiny/app.R",
  "pilot/shiny/student-data.R",
  "pilot/shiny/data",
  "pilot/shared.R",
  "assets/css",
  "assets/brand/ucr-primary-plum.png",
  "assets/fonts"
)) {
  copy_relative(relative)
}

run_script <- function(arguments, execution_root = test_root) {
  old <- setwd(execution_root)
  on.exit(setwd(old), add = TRUE)
  output <- system2(
    file.path(R.home("bin"), "Rscript"),
    arguments,
    stdout = TRUE,
    stderr = TRUE
  )
  status <- attr(output, "status")
  if (is.null(status)) status <- 0L
  list(status = status, output = output)
}

completed_fixture <- function(id, interpretation) {
  record <- read_student_json(file.path(repo_root, "data", "examples", paste0(id, ".json")))
  record$origin <- "student"
  record$interestInterpretation <- interpretation
  path <- tempfile(paste0(id, "-completed-"), fileext = ".json")
  jsonlite::write_json(record, path, auto_unbox = TRUE, pretty = TRUE, null = "null")
  path
}
first_input <- completed_fixture("p-001", "A synthetic completed interpretation for the first production-workflow test record.")
second_input <- completed_fixture("p-002", "A synthetic completed interpretation for the second production-workflow test record.")
third_input <- completed_fixture("p-003", "A synthetic completed interpretation for the lock-rejection test.")
fourth_input <- completed_fixture("p-004", "A synthetic completed interpretation for the malformed-batch test record.")
on.exit(unlink(c(first_input, second_input, third_input, fourth_input)), add = TRUE)

# First-time use starts with completed files placed directly in the familiar
# private/student-records directory. Registration creates the missing metadata.
record_dir <- file.path(test_root, "private", "student-records")
dir.create(record_dir, recursive = TRUE)
stopifnot(file.copy(first_input, file.path(record_dir, "p-001.json")))
stopifnot(file.copy(second_input, file.path(record_dir, "p-002.json")))
stopifnot(expect_error(load_student_data_config(test_root, "private")))
batch_add <- run_script(c("scripts/add-students-private.R", "--quiet"))
if (batch_add$status != 0L) stop(paste(batch_add$output, collapse = "\n"))

batch_results_path <- file.path(test_root, "private", "student-last-batch-codes.csv")
batch_results <- read.csv(batch_results_path, stringsAsFactors = FALSE)
stopifnot(identical(batch_results$record_id, c("p-001", "p-002")))
first <- list(
  recordId = "p-001",
  accessCode = batch_results$access_code[[1]],
  resultsFile = batch_results_path
)
second <- list(
  recordId = "p-002",
  accessCode = batch_results$access_code[[2]],
  resultsFile = batch_results_path
)
stopifnot(grepl(STUDENT_PRIVATE_CODE_PATTERN, first$accessCode, perl = TRUE))
first_path <- file.path(test_root, "private", "student-records", "p-001.json")
first_hash <- unname(tools::md5sum(first_path))

production <- validate_student_production_dataset(test_root)
stopifnot(identical(production$ids, c("p-001", "p-002")))
stopifnot(identical(production$codes[[1]], first$accessCode))
stopifnot(identical(unname(tools::md5sum(first_path)), first_hash))
stopifnot(!identical(normalize_student_code(first$accessCode), normalize_student_code(second$accessCode)))

# Explicit single-record import remains available as a compatibility fallback
# and continues to reject duplicate ids.
stopifnot(expect_error(add_student_production_records(
  test_root,
  c(first_input, third_input)
)))

# A malformed member rejects the complete directly placed batch. Input files
# remain available for correction, while the access index and code sheet remain
# unchanged.
stopifnot(file.copy(third_input, file.path(record_dir, "p-003.json")))
malformed <- read_student_json(fourth_input, "malformed production fixture")
malformed$interestInterpretation <- NULL
jsonlite::write_json(
  malformed,
  file.path(record_dir, "p-004.json"),
  auto_unbox = TRUE,
  pretty = TRUE,
  null = "null"
)
access_path <- file.path(test_root, "private", "student-access.json")
access_before_failure <- readBin(access_path, what = "raw", n = file.info(access_path)$size)
codes_before_failure <- readBin(batch_results_path, what = "raw", n = file.info(batch_results_path)$size)
failed_batch <- run_script(c("scripts/add-students-private.R", "--quiet"))
stopifnot(failed_batch$status != 0L)
pending <- validate_student_production_dataset(
  test_root,
  allow_unindexed_records = TRUE
)
stopifnot(identical(pending$ids, c("p-001", "p-002")))
stopifnot(identical(pending$unindexed_files, c("p-003.json", "p-004.json")))
stopifnot(identical(
  readBin(access_path, what = "raw", n = file.info(access_path)$size),
  access_before_failure
))
stopifnot(identical(
  readBin(batch_results_path, what = "raw", n = file.info(batch_results_path)$size),
  codes_before_failure
))

# Concurrent registration is rejected without modifying pending files.
held_lock <- acquire_student_production_lock(test_root)
stopifnot(expect_error(register_unindexed_student_records(test_root)))
release_student_production_lock(held_lock)

# A later successful batch preserves all earlier records and codes. The private
# code sheet intentionally contains only the most recently registered batch.
unlink(file.path(record_dir, "p-004.json"))
later_add <- run_script(c("scripts/add-students-private.R", "--quiet"))
if (later_add$status != 0L) stop(paste(later_add$output, collapse = "\n"))
production <- validate_student_production_dataset(test_root)
stopifnot(identical(production$ids, c("p-001", "p-002", "p-003")))
stopifnot(identical(production$codes[[1]], first$accessCode))
stopifnot(identical(production$codes[[2]], second$accessCode))
stopifnot(identical(unname(tools::md5sum(first_path)), first_hash))
latest_results <- read.csv(batch_results_path, stringsAsFactors = FALSE)
stopifnot(identical(latest_results$record_id, "p-003"))

# Running registration with no new files is a successful no-op and does not
# replace the latest code sheet.
no_change <- run_script(c("scripts/add-students-private.R"))
stopifnot(no_change$status == 0L)
stopifnot(any(grepl("No new student records", no_change$output, fixed = TRUE)))
stopifnot(identical(read.csv(batch_results_path, stringsAsFactors = FALSE)$record_id, "p-003"))

# Public development codes do not unlock private production records.
config <- load_student_data_config(test_root, "private")
public_index <- read_student_json(
  file.path(test_root, "pilot", "shiny", "data", "access_codes.json"),
  "public pilot access index"
)
stopifnot(is.null(load_student_record_for_code(config, public_index$entries[[1]]$code)))
stopifnot(identical(load_student_record_for_code(config, first$accessCode)$id, "p-001"))

# Missing or malformed private indexes fail closed. All mutations occur only in
# the isolated synthetic repository.
access_bytes <- readBin(access_path, what = "raw", n = file.info(access_path)$size)
file.rename(access_path, paste0(access_path, ".missing"))
stopifnot(expect_error(load_student_data_config(test_root, "private")))
file.rename(paste0(access_path, ".missing"), access_path)
writeLines("{ malformed", access_path, useBytes = TRUE)
stopifnot(expect_error(load_student_data_config(test_root, "private")))
connection <- file(access_path, open = "wb")
writeBin(access_bytes, connection)
close(connection)
stopifnot(identical(load_student_data_config(test_root, "private")$record_ids, c("p-001", "p-002", "p-003")))

# The operator's one-command deploy wrapper runs both pre-deployment checks.
deployment_check <- run_script(c("scripts/validate-and-deploy-student.R", "--check-only"))
if (deployment_check$status != 0L) stop(paste(deployment_check$output, collapse = "\n"))

# The resulting production configuration can start the app and reveals only the
# selected record after a valid code.
old_mode <- Sys.getenv("UCR_STUDENT_DATA_MODE", unset = NA_character_)
old <- setwd(test_root)
Sys.setenv(UCR_STUDENT_DATA_MODE = "private")
student <- new.env()
student_source <- source(file.path(test_root, "pilot", "shiny", "app.R"), local = student)
setwd(old)
if (is.na(old_mode)) Sys.unsetenv("UCR_STUDENT_DATA_MODE") else Sys.setenv(UCR_STUDENT_DATA_MODE = old_mode)
stopifnot(inherits(student_source$value, "shiny.appobj"))
stopifnot(identical(student$STUDENT_DATA_CONFIG$record_ids, c("p-001", "p-002", "p-003")))

shiny::testServer(student$make_student_server(student$STUDENT_DATA_CONFIG), {
  session$setInputs(access_code = first$accessCode, unlock_pathway = 1)
  stopifnot(identical(record()$id, "p-001"))
  session$flushReact()
  selected_html <- paste(as.character(output$app_body), collapse = "")
  stopifnot(!grepl(load_student_record_for_code(config, second$accessCode)$interests, selected_html, fixed = TRUE))
})

# An existing private dataset can become the cumulative production dataset
# without deleting or rewriting any existing record or changing any existing
# access code. A newly placed record is then appended in the same run.
migration_root <- tempfile("student-existing-to-production-")
dir.create(migration_root)
on.exit(unlink(migration_root, recursive = TRUE), add = TRUE)
for (relative in c(
  ".gitignore",
  "scripts/student-private-workflow.R",
  "scripts/add-students-private.R",
  "scripts/init-student-private-test.R",
  "pilot/shiny/student-data.R",
  "pilot/shiny/data",
  "data/examples"
)) {
  copy_relative(relative, migration_root)
}
test_initialization <- run_script(c("scripts/init-student-private-test.R", "--quiet"), migration_root)
if (test_initialization$status != 0L) stop(paste(test_initialization$output, collapse = "\n"))

before_config <- load_student_data_config(migration_root, "private")
before_entries <- before_config$access_map$entries
before_codes <- vapply(before_entries, function(entry) as.character(entry$code), character(1))
before_paths <- before_config$record_paths
before_hashes <- unname(tools::md5sum(before_paths))
stopifnot(identical(before_config$record_ids, sprintf("p-%03d", 1:5)))

# Simulate older private metadata. The migration must validate and preserve the
# indexed dataset rather than depend on one exact historical datasetType label.
legacy_marker_path <- file.path(migration_root, "private", "student-mode.json")
legacy_access_path <- file.path(migration_root, "private", "student-access.json")
legacy_marker <- read_student_json(legacy_marker_path, "legacy private marker")
legacy_access <- read_student_json(legacy_access_path, "legacy private access index")
legacy_marker$datasetType <- "legacy-private-test"
legacy_marker$generator <- NULL
legacy_access$datasetType <- "legacy-private-test"
student_write_json_atomic(legacy_marker, legacy_marker_path)
student_write_json_atomic(legacy_access, legacy_access_path)

real_record <- read_student_json(first_input, "synthetic first real record")
real_record$id <- "p-006"
jsonlite::write_json(
  real_record,
  file.path(migration_root, "private", "student-records", "p-006.json"),
  auto_unbox = TRUE,
  pretty = TRUE,
  null = "null"
)
migration <- run_script("scripts/add-students-private.R", migration_root)
if (migration$status != 0L) stop(paste(migration$output, collapse = "\n"))
stopifnot(any(grepl("existing records and access codes preserved", migration$output, fixed = TRUE)))

migrated <- validate_student_production_dataset(migration_root)
expected_ids <- sprintf("p-%03d", 1:6)
stopifnot(identical(migrated$ids, expected_ids))
stopifnot(identical(migrated$files, paste0(expected_ids, ".json")))
stopifnot(identical(migrated$entries[1:5], before_entries))
stopifnot(identical(migrated$codes[1:5], before_codes))
stopifnot(identical(
  unname(tools::md5sum(file.path(migration_root, "private", "student-records", paste0(sprintf("p-%03d", 1:5), ".json")))),
  before_hashes
))
stopifnot(file.exists(file.path(migration_root, "private", "student-test-codes.txt")))
latest_migration_results <- read.csv(
  file.path(migration_root, "private", "student-last-batch-codes.csv"),
  stringsAsFactors = FALSE
)
stopifnot(identical(latest_migration_results$record_id, "p-006"))

cat("Direct-folder registration, non-destructive metadata migration, deployment checks, and startup checks passed.\n")
