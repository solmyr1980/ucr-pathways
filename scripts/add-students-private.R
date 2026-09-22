#!/usr/bin/env Rscript

# Register every new JSON record already placed in private/student-records.

args <- commandArgs(trailingOnly = TRUE)
quiet <- "--quiet" %in% args
known <- args == "--quiet"
if (any(!known)) stop("Unknown argument: ", args[!known][[1]])

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

result <- register_unindexed_student_records(repo_root)
if (!length(result$records)) {
  if (!quiet) {
    cat(
      "No new student records were found in private/student-records.\n",
      "No files or access codes were changed.\n",
      sep = ""
    )
  }
  quit(status = 0)
}

if (quiet) {
  cat(result$resultsFile, "\n", sep = "")
} else {
  if (isTRUE(result$migratedPrivateDataset)) {
    cat("Existing private dataset migrated to cumulative production mode; existing records and access codes preserved.\n\n")
  }
  cat(
    "New student records registered.\n",
    "Records registered: ", length(result$records), "\n",
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
