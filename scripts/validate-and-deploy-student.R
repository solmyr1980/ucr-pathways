#!/usr/bin/env Rscript

# Run the full production validation and deploy the cumulative student app once.

args <- commandArgs(trailingOnly = TRUE)
account_args <- args[startsWith(args, "--account=")]
check_only <- "--check-only" %in% args
known <- args == "--check-only" | startsWith(args, "--account=")
if (any(!known)) stop("Unknown argument: ", args[!known][[1]])
if (length(account_args) > 1L) stop("Specify --account only once.")

script_argument <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (!length(script_argument)) stop("Run this file with Rscript.")
script_path <- normalizePath(sub("^--file=", "", script_argument[[1]]), winslash = "/", mustWork = TRUE)
repo_root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)
old_directory <- setwd(repo_root)
on.exit(setwd(old_directory), add = TRUE)

rscript <- file.path(R.home("bin"), "Rscript")
deploy_script <- file.path("scripts", "deploy-student-shiny.R")
run_step <- function(step_args, description) {
  status <- system2(rscript, c(deploy_script, step_args))
  if (!identical(status, 0L)) stop(description, " failed; deployment stopped.")
}

cat("Validating the complete private student dataset...\n")
run_step("--check", "Dataset validation")
cat("Validating the exact shinyapps.io bundle...\n")
run_step("--check-bundle", "Bundle validation")

if (check_only) {
  cat("All pre-deployment checks passed. No deployment was requested.\n")
  quit(status = 0)
}

cat("Deploying the cumulative dataset once...\n")
deployment_args <- if (length(account_args)) account_args else character()
run_step(deployment_args, "Student app deployment")
cat("Student app deployment completed successfully. Access codes may now be distributed.\n")
