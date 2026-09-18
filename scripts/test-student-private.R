#!/usr/bin/env Rscript

if (!requireNamespace("jsonlite", quietly = TRUE) || !requireNamespace("shiny", quietly = TRUE)) {
  stop("Install jsonlite and shiny before running private student-app tests.")
}

repo_root <- normalizePath(".", winslash = "/", mustWork = TRUE)
source(file.path(repo_root, "scripts", "student-private-workflow.R"), local = TRUE)
source(file.path(repo_root, "pilot", "shiny", "student-data.R"), local = TRUE)

expect_error <- function(expression) inherits(try(force(expression), silent = TRUE), "try-error")
test_ignore_contract <- function() {
  test_root <- tempfile("student-private-ignore-")
  dir.create(test_root)
  on.exit(unlink(test_root, recursive = TRUE), add = TRUE)
  ignore_path <- file.path(test_root, ".gitignore")

  writeLines("/private/", ignore_path)
  stopifnot(isTRUE(assert_private_tree_ignored(test_root)))

  writeLines("private/", ignore_path)
  stopifnot(expect_error(assert_private_tree_ignored(test_root)))

  writeLines(c("/private/", "!/*"), ignore_path)
  stopifnot(expect_error(assert_private_tree_ignored(test_root)))
}

test_ignore_contract()
assert_private_tree_ignored(repo_root)
config <- load_student_data_config(repo_root, "private")
if (!identical(config$marker$datasetType, "five-public-fixture-test")) {
  stop("Refusing to test or modify a private dataset that is not the generated five-case test dataset.")
}
stopifnot(identical(sort(config$record_ids), sprintf("p-%03d", 1:5)))
validate_private_test_derivation(config, repo_root)

private_codes <- vapply(config$access_map$entries, function(entry) entry$code, character(1))
normalized_private <- vapply(private_codes, normalize_student_code, character(1))
stopifnot(length(unique(normalized_private)) == 5)
for (index in seq_along(private_codes)) {
  code <- private_codes[[index]]
  spaced <- tolower(gsub("-", " ", code))
  stopifnot(identical(normalize_student_code(spaced), normalize_student_code(code)))
  record <- load_student_record_for_code(config, spaced)
  stopifnot(identical(record$id, config$record_ids[[index]]))
  public_record <- read_student_json(file.path(repo_root, "data", "examples", paste0(record$id, ".json")))
  stopifnot(identical(record$interests, public_record$interests))
  stopifnot(nzchar(record$interestInterpretation), identical(record$origin, "student"))
}
stopifnot(is.na(normalize_student_code("UCR/INVALID")))
stopifnot(is.null(load_student_record_for_code(config, "UCR-XXXX-XXXX-XXXX-XXXX")))

public_codes <- read_student_json(
  file.path(repo_root, "pilot", "shiny", "data", "access_codes.json"),
  "public pilot access index"
)
for (entry in public_codes$entries) {
  stopifnot(is.null(load_student_record_for_code(config, entry$code)))
}

# The private tree is covered by the repository's root ignore rule and is not
# mounted as a Shiny static resource.
resource_code <- paste(readLines(file.path(repo_root, "pilot", "shared.R"), warn = FALSE), collapse = "\n")
stopifnot(!grepl("addResourcePath\\([^\\n]*private", resource_code))
stopifnot(!dir.exists(file.path(repo_root, "pilot", "shiny", "www", "private")))

Sys.setenv(UCR_STUDENT_DATA_MODE = "private")
student <- new.env()
source(file.path(repo_root, "pilot", "shiny", "app.R"), local = student)
stopifnot(identical(student$STUDENT_DATA_CONFIG$mode, "private"))

shiny::testServer(student$make_student_server(config), {
  session$flushReact()
  locked_html <- paste(as.character(output$app_body), collapse = "")
  stopifnot(!any(vapply(private_codes, grepl, logical(1), x = locked_html, fixed = TRUE)))
  stopifnot(!any(vapply(config$record_ids, grepl, logical(1), x = locked_html, fixed = TRUE)))

  session$setInputs(access_code = public_codes$entries[[1]]$code, unlock_pathway = 1)
  stopifnot(is.null(record()))
  session$setInputs(access_code = "UCR-XXXX-XXXX-XXXX-XXXX", unlock_pathway = 2)
  stopifnot(is.null(record()))

  session$setInputs(access_code = private_codes[[1]], unlock_pathway = 3)
  stopifnot(identical(record()$id, config$record_ids[[1]]))
  session$flushReact()
  selected_html <- paste(as.character(output$app_body), collapse = "")
  stopifnot(grepl(record()$interests, selected_html, fixed = TRUE))
  second_record <- load_student_record_for_code(config, private_codes[[2]])
  stopifnot(!grepl(second_record$interests, selected_html, fixed = TRUE))
})

run_deployment_check <- function() {
  output <- system2(
    file.path(R.home("bin"), "Rscript"),
    c("scripts/deploy-student-shiny.R", "--check"),
    stdout = TRUE,
    stderr = TRUE
  )
  status <- attr(output, "status")
  if (is.null(status)) status <- 0L
  list(status = status, output = output)
}

stopifnot(run_deployment_check()$status == 0L)

second_init <- system2(
  file.path(R.home("bin"), "Rscript"),
  "scripts/init-student-private-test.R",
  stdout = TRUE,
  stderr = TRUE
)
second_init_status <- attr(second_init, "status")
if (is.null(second_init_status)) second_init_status <- 0L
stopifnot(second_init_status != 0L)

# The actual deployment check must reject both a missing record and malformed
# private JSON. These mutations are permitted only for the marked test dataset
# and are restored immediately.
record_path <- config$record_paths[[1]]
hidden_path <- paste0(record_path, ".missing-check")
if (file.exists(hidden_path)) stop("Unexpected deployment-test backup file already exists: ", hidden_path)
if (!file.rename(record_path, hidden_path)) stop("Could not prepare missing-record deployment test.")
on.exit(if (file.exists(hidden_path)) file.rename(hidden_path, record_path), add = TRUE)
missing_result <- run_deployment_check()
if (!file.rename(hidden_path, record_path)) stop("Could not restore missing-record deployment test fixture.")
stopifnot(missing_result$status != 0L)

access_path <- config$access_file
access_size <- file.info(access_path)$size
connection <- file(access_path, open = "rb")
original_access <- readBin(connection, what = "raw", n = access_size)
close(connection)
restore_access <- function() {
  connection <- file(access_path, open = "wb")
  writeBin(original_access, connection)
  close(connection)
}
on.exit(restore_access(), add = TRUE)
writeLines("{ malformed", access_path, useBytes = TRUE)
malformed_result <- run_deployment_check()
restore_access()
stopifnot(malformed_result$status != 0L)

cat("Private student data, isolation, app behavior, and deployment rejection checks passed.\n")
