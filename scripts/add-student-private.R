#!/usr/bin/env Rscript

# Initialize or append to the cumulative ignored production student dataset.

args <- commandArgs(trailingOnly = TRUE)
record_args <- args[startsWith(args, "--record=")]
initialize_only <- "--init" %in% args
quiet <- "--quiet" %in% args
known <- args %in% c("--init", "--quiet") | startsWith(args, "--record=")
if (any(!known)) stop("Unknown argument: ", args[!known][[1]])
if (length(record_args) > 1) stop("Specify --record only once.")
if (initialize_only && length(record_args)) stop("Use either --init or --record, not both.")
if (!initialize_only && !length(record_args)) stop("Specify --init or --record=<completed-student-record.json>.")

script_argument <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (!length(script_argument)) stop("Run this file with Rscript.")
script_path <- normalizePath(sub("^--file=", "", script_argument[[1]]), winslash = "/", mustWork = TRUE)
repo_root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Install the jsonlite package before using the private student workflow.")
}
if (!requireNamespace("openssl", quietly = TRUE)) {
  stop("Install the openssl package before using the private student workflow.")
}

source(file.path(repo_root, "pilot", "shiny", "student-data.R"), local = TRUE)
source(file.path(repo_root, "scripts", "student-private-workflow.R"), local = TRUE)
assert_private_tree_ignored(repo_root)

if (initialize_only) {
  lock <- acquire_student_production_lock(repo_root)
  on.exit(release_student_production_lock(lock), add = TRUE)
  config <- initialize_student_production_dataset(repo_root)
  if (!quiet) {
    cat(
      "Cumulative production student dataset is ready.\n",
      "Records: ", length(config$entries), "\n",
      "Location: private/\n",
      sep = ""
    )
  }
  quit(status = 0)
}

record_path <- sub("^--record=", "", record_args[[1]])
if (!nzchar(record_path)) stop("--record requires a JSON file path.")
result <- add_student_production_record(repo_root, record_path)
if (quiet) {
  cat(result$accessCode, "\n", sep = "")
} else {
  cat(
    "Student added to the cumulative private dataset.\n",
    "Record ID: ", result$recordId, "\n",
    "Stable access code: ", result$accessCode, "\n",
    "Private code sheet: ", result$resultsFile, "\n",
    "The access code will remain unchanged when later students are added.\n",
    "No deployment has occurred yet; deploy successfully before distributing the code.\n",
    sep = ""
  )
}
