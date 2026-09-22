#!/usr/bin/env Rscript

# Add every completed JSON record in one folder to the cumulative private dataset.

args <- commandArgs(trailingOnly = TRUE)
folder_args <- args[startsWith(args, "--folder=")]
quiet <- "--quiet" %in% args
known <- args == "--quiet" | startsWith(args, "--folder=")
if (any(!known)) stop("Unknown argument: ", args[!known][[1]])
if (length(folder_args) != 1L) stop("Specify --folder=<completed-records-folder> exactly once.")

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

folder <- sub("^--folder=", "", folder_args[[1]])
if (!nzchar(folder) || !dir.exists(folder)) stop("--folder must name an existing folder.")
folder <- normalizePath(folder, winslash = "/", mustWork = TRUE)
record_paths <- sort(list.files(
  folder,
  pattern = "\\.json$",
  full.names = TRUE,
  recursive = FALSE,
  ignore.case = TRUE
))
if (!length(record_paths)) stop("The folder contains no JSON records: ", folder)

result <- add_student_production_records(repo_root, record_paths)
if (quiet) {
  cat(result$resultsFile, "\n", sep = "")
} else {
  cat(
    "Student batch added to the cumulative private dataset.\n",
    "Records added: ", length(result$records), "\n",
    "No deployment has occurred yet.\n\n",
    sep = ""
  )
  for (record in result$records) {
    cat(record$recordId, ": ", record$accessCode, "\n", sep = "")
  }
  cat(
    "\nPrivate code sheet: ", result$resultsFile, "\n",
    "Deploy successfully before distributing these access codes.\n",
    sep = ""
  )
}
