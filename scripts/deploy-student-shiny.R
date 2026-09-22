#!/usr/bin/env Rscript

# Validate and deploy the student Shiny app with an explicit private bundle.
# The ignored private tree is included through appFiles; public example records
# and the public pilot access map are deliberately excluded.

args <- commandArgs(trailingOnly = TRUE)

option_value <- function(name, default = NULL) {
  prefix <- paste0(name, "=")
  matches <- args[startsWith(args, prefix)]
  if (length(matches) > 1) stop("Specify ", name, " only once.")
  if (!length(matches)) return(default)
  sub(paste0("^", prefix), "", matches[[1]])
}

known_argument <- args %in% c("--check", "--check-bundle") |
  startsWith(args, "--account=")
if (any(!known_argument)) stop("Unknown argument: ", args[!known_argument][[1]])
if (all(c("--check", "--check-bundle") %in% args)) stop("Use either --check or --check-bundle, not both.")

script_argument <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (!length(script_argument)) stop("Run this file with Rscript.")
script_path <- normalizePath(sub("^--file=", "", script_argument[[1]]), winslash = "/", mustWork = TRUE)
repo_root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Install the jsonlite package before checking or deploying the student app.")
}
source(file.path(repo_root, "scripts", "student-private-workflow.R"), local = TRUE)
source(file.path(repo_root, "pilot", "shiny", "student-data.R"), local = TRUE)
assert_private_tree_ignored(repo_root)

private_root <- file.path(repo_root, "private")
if (!dir.exists(private_root)) {
  stop(
    "Missing private student directory. Run scripts/add-student-private.R --init for production ",
    "or scripts/init-student-private-test.R for the disposable five-case test."
  )
}
private_files_on_disk <- list.files(private_root, recursive = TRUE, full.names = FALSE, all.files = TRUE, no.. = TRUE)
if (!length(private_files_on_disk)) stop("The private student directory is empty.")

config <- load_student_data_config(repo_root, "private")
dataset_type <- as.character(student_value(config$marker$datasetType, ""))
if (!dataset_type %in% c("five-public-fixture-test", STUDENT_PRODUCTION_DATASET_TYPE)) {
  stop("Private student dataset must be the marked five-case test or cumulative production dataset.")
}
if (identical(dataset_type, "five-public-fixture-test")) {
  validate_private_test_derivation(config, repo_root)
  for (index in seq_along(config$record_paths)) {
    validate_student_record_mechanically(repo_root, config$record_paths[[index]], config$record_ids[[index]])
  }
} else {
  production <- validate_student_production_dataset(repo_root)
  if (!identical(config$record_ids, production$ids) || !identical(config$record_files, production$files)) {
    stop("Production deployment configuration differs from the validated cumulative dataset.")
  }
}

required_files <- c(
  "pilot/shiny/app.R",
  "pilot/shiny/student-data.R",
  "pilot/shared.R",
  "assets/css/brand.css",
  "assets/css/shiny.css",
  "assets/brand/ucr-primary-plum.png",
  "assets/fonts/Inter_Bold.ttf",
  "assets/fonts/Inter_Light.ttf",
  "assets/fonts/Inter_Medium.ttf",
  "assets/fonts/IvyMode Light.otf",
  "assets/fonts/IvyMode Regular.otf",
  "assets/fonts/IvyMode Semibold.otf"
)

records <- lapply(seq_along(config$record_paths), function(index) {
  read_student_json(config$record_paths[[index]], paste("student record", config$record_ids[[index]]))
})
course_codes <- unlist(lapply(records, function(record) {
  unlist(lapply(record$programmes, function(programme) {
    unlist(lapply(student_value(programme$schedule$semesters, list()), function(semester) {
      vapply(student_value(semester$courses, list()), function(course) as.character(student_value(course$code, "")), character(1))
    }), use.names = FALSE)
  }), use.names = FALSE)
}), use.names = FALSE)
departments <- sort(unique(substr(course_codes[nzchar(course_codes)], 1, 3)))
course_files <- file.path("pilot", "shiny", "data", "courses", paste0(departments, ".json"))

private_runtime_files <- c(
  "private/student-mode.json",
  "private/student-access.json",
  file.path("private", "student-records", config$record_files)
)
runtime_files <- sort(unique(c(required_files, course_files, private_runtime_files)))

missing_runtime <- runtime_files[!file.exists(file.path(repo_root, runtime_files))]
if (length(missing_runtime)) stop("Deployment selection contains missing files: ", paste(missing_runtime, collapse = ", "))
if (any(startsWith(runtime_files, "data/examples/")) || "pilot/shiny/data/access_codes.json" %in% runtime_files) {
  stop("Private deployment selection must not contain public records or the public pilot access map.")
}
administrative_private_files <- c(
  "private/student-test-codes.txt",
  "private/student-last-batch-codes.csv"
)
if (any(administrative_private_files %in% runtime_files)) {
  stop("Local administrative code-reference files must not be included in the deployment bundle.")
}

bundle_bytes <- sum(file.info(file.path(repo_root, runtime_files))$size)
cat(
  "Student private deployment selection is valid.\n",
  "Mode: private\n",
  "Records: ", length(config$record_ids), "\n",
  "Files: ", length(runtime_files), "\n",
  "Size: ", format(bundle_bytes, big.mark = ",", scientific = FALSE), " bytes\n",
  sep = ""
)

if ("--check" %in% args) quit(status = 0)

if (!requireNamespace("rsconnect", quietly = TRUE)) {
  stop("Install the rsconnect package before checking the bundle or deploying the student app.")
}

if ("--check-bundle" %in% args) {
  selected_files <- rsconnect::listDeploymentFiles(repo_root, appFiles = runtime_files)
  if (!identical(sort(selected_files), sort(runtime_files))) {
    stop("rsconnect did not select exactly the expected student runtime files.")
  }
  if (!all(private_runtime_files %in% selected_files)) stop("The deployment bundle is missing private runtime files.")
  dependencies <- rsconnect::appDependencies(
    appDir = repo_root,
    appFiles = runtime_files,
    appMode = "shiny",
    dependencyResolution = "library"
  )
  expected_packages <- c("jsonlite", "shiny")
  missing_packages <- setdiff(expected_packages, dependencies$Package)
  if (length(missing_packages)) stop("rsconnect did not detect required package(s): ", paste(missing_packages, collapse = ", "))
  manifest_path <- file.path(repo_root, "manifest.json")
  if (file.exists(manifest_path)) stop("Refusing to overwrite existing manifest.json during the bundle check.")
  tryCatch({
    rsconnect::writeManifest(
      appDir = repo_root,
      appFiles = runtime_files,
      appPrimaryDoc = "pilot/shiny/app.R",
      appMode = "shiny",
      dependencyResolution = "library",
      quiet = TRUE
    )
    if (!file.exists(manifest_path)) stop("rsconnect did not create the temporary deployment manifest.")
  }, finally = {
    if (file.exists(manifest_path)) unlink(manifest_path)
  })
  cat("rsconnect student bundle and dependency checks passed.\n")
  quit(status = 0)
}

if (identical(dataset_type, "five-public-fixture-test")) {
  stop(
    "Refusing to deploy the disposable five-case dataset over the live student app. ",
    "Use --check or --check-bundle for that regression fixture."
  )
}

account <- option_value("--account", Sys.getenv("SHINYAPPS_ACCOUNT", unset = ""))
app_name <- "ucr-student"

rsconnect::deployApp(
  appDir = repo_root,
  appFiles = runtime_files,
  appPrimaryDoc = "pilot/shiny/app.R",
  appName = app_name,
  appTitle = "Your personalized UCR study possibilities",
  account = if (nzchar(account)) account else NULL,
  server = "shinyapps.io",
  appMode = "shiny",
  recordDir = file.path(repo_root, "pilot", "shiny")
)
