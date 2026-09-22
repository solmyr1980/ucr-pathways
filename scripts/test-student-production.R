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

copy_relative <- function(relative) {
  source_path <- file.path(repo_root, relative)
  destination <- file.path(test_root, relative)
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
  "scripts/deploy-student-shiny.R",
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

# Creation of an initially empty cumulative dataset is valid for preparation,
# while app loading and deployment continue to fail closed until a record exists.
lock <- acquire_student_production_lock(test_root)
empty <- initialize_student_production_dataset(test_root)
release_student_production_lock(lock)
stopifnot(length(empty$entries) == 0L)
stopifnot(expect_error(load_student_data_config(test_root, "private")))

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
on.exit(unlink(c(first_input, second_input, third_input)), add = TRUE)

first <- add_student_production_record(test_root, first_input)
stopifnot(grepl(STUDENT_PRIVATE_CODE_PATTERN, first$accessCode, perl = TRUE))
first_path <- file.path(test_root, "private", "student-records", "p-001.json")
first_hash <- unname(tools::md5sum(first_path))

second <- add_student_production_record(test_root, second_input)
production <- validate_student_production_dataset(test_root)
stopifnot(identical(production$ids, c("p-001", "p-002")))
stopifnot(identical(production$codes[[1]], first$accessCode))
stopifnot(identical(unname(tools::md5sum(first_path)), first_hash))
stopifnot(!identical(normalize_student_code(first$accessCode), normalize_student_code(second$accessCode)))

# Duplicate ids, malformed records and concurrent additions are rejected.
stopifnot(expect_error(add_student_production_record(
  test_root,
  first_input
)))
malformed <- read_student_json(file.path(repo_root, "data", "examples", "p-003.json"))
malformed$origin <- "student"
malformed$interestInterpretation <- NULL
malformed_path <- tempfile("malformed-student-", fileext = ".json")
on.exit(if (file.exists(malformed_path)) unlink(malformed_path), add = TRUE)
jsonlite::write_json(malformed, malformed_path, auto_unbox = TRUE, pretty = TRUE, null = "null")
stopifnot(expect_error(add_student_production_record(test_root, malformed_path)))
held_lock <- acquire_student_production_lock(test_root)
stopifnot(expect_error(add_student_production_record(
  test_root,
  third_input
)))
release_student_production_lock(held_lock)

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
access_path <- file.path(test_root, "private", "student-access.json")
access_bytes <- readBin(access_path, what = "raw", n = file.info(access_path)$size)
file.rename(access_path, paste0(access_path, ".missing"))
stopifnot(expect_error(load_student_data_config(test_root, "private")))
file.rename(paste0(access_path, ".missing"), access_path)
writeLines("{ malformed", access_path, useBytes = TRUE)
stopifnot(expect_error(load_student_data_config(test_root, "private")))
connection <- file(access_path, open = "wb")
writeBin(access_bytes, connection)
close(connection)
stopifnot(identical(load_student_data_config(test_root, "private")$record_ids, c("p-001", "p-002")))

run_script <- function(arguments) {
  old <- setwd(test_root)
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

# Production data pass both the deployment selection and rsconnect bundle checks.
check <- run_script(c("scripts/deploy-student-shiny.R", "--check"))
if (check$status != 0L) stop(paste(check$output, collapse = "\n"))
bundle <- run_script(c("scripts/deploy-student-shiny.R", "--check-bundle"))
if (bundle$status != 0L) stop(paste(bundle$output, collapse = "\n"))

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
stopifnot(identical(student$STUDENT_DATA_CONFIG$record_ids, c("p-001", "p-002")))

shiny::testServer(student$make_student_server(student$STUDENT_DATA_CONFIG), {
  session$setInputs(access_code = first$accessCode, unlock_pathway = 1)
  stopifnot(identical(record()$id, "p-001"))
  session$flushReact()
  selected_html <- paste(as.character(output$app_body), collapse = "")
  stopifnot(!grepl(load_student_record_for_code(config, second$accessCode)$interests, selected_html, fixed = TRUE))
})

cat("Cumulative student production, isolation, deployment bundle, and startup checks passed.\n")
