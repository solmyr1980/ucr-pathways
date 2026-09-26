#!/usr/bin/env Rscript

# Deploy the counselor Shiny app to shinyapps.io from the authoritative
# repository files. rsconnect creates the upload bundle; no maintained copy of
# the app, counselor data, or shared brand assets is required.

args <- commandArgs(trailingOnly = TRUE)
`%||%` <- function(value, fallback) if (is.null(value) || length(value) == 0L) fallback else value

option_value <- function(name, default = NULL) {
  prefix <- paste0(name, "=")
  matches <- args[startsWith(args, prefix)]
  if (length(matches) > 1) stop("Specify ", name, " only once.")
  if (!length(matches)) return(default)
  sub(paste0("^", prefix), "", matches[[1]])
}

known_argument <- args %in% c("--check", "--check-bundle") |
  startsWith(args, "--account=") |
  startsWith(args, "--app-name=")
if (any(!known_argument)) stop("Unknown argument: ", args[!known_argument][[1]])
if (all(c("--check", "--check-bundle") %in% args)) {
  stop("Use either --check or --check-bundle, not both.")
}

script_argument <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (!length(script_argument)) stop("Run this file with Rscript.")
script_path <- normalizePath(sub("^--file=", "", script_argument[[1]]), winslash = "/", mustWork = TRUE)
repo_root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)

required_files <- c(
  "pilot/counselor-shiny/app.R",
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

mode_definitions <- list(
  production = list(
    programmes = "data/counselor/programmes.json",
    interests = "data/counselor/interests.json",
    comparison_directory = "data/counselor/comparisons"
  ),
  review = list(
    programmes = "data/counselor/review-programmes.json",
    interests = "data/counselor/review-interests.json",
    comparison_directory = "data/counselor/comparisons"
  ),
  pilot = list(
    programmes = "data/counselor/pilot-programmes.json",
    interests = "data/counselor/pilot-interests.json",
    comparison_directory = "data/examples"
  )
)

missing_required <- required_files[!file.exists(file.path(repo_root, required_files))]
if (length(missing_required)) {
  stop("Missing required counselor runtime file(s): ", paste(missing_required, collapse = ", "))
}

mode_available <- vapply(names(mode_definitions), function(mode_name) {
  definition <- mode_definitions[[mode_name]]
  has_programmes <- file.exists(file.path(repo_root, definition$programmes))
  has_interests <- file.exists(file.path(repo_root, definition$interests))
  if (xor(has_programmes, has_interests)) {
    stop("Incomplete ", mode_name, " data mode: programme and interest indexes must both be present.")
  }
  has_programmes && has_interests
}, logical(1))

if (!any(mode_available)) stop("No complete counselor data mode is available for deployment.")

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Install the jsonlite package before checking or deploying the counselor app.")
}

comparison_files_for <- function(mode_name) {
  definition <- mode_definitions[[mode_name]]
  programme_data <- jsonlite::fromJSON(
    file.path(repo_root, definition$programmes),
    simplifyVector = FALSE
  )
  interest_data <- jsonlite::fromJSON(
    file.path(repo_root, definition$interests),
    simplifyVector = FALSE
  )
  if (!length(programme_data$programmes)) stop("No programmes found in ", definition$programmes, ".")
  if (is.null(interest_data$interests)) stop("No interests array found in ", definition$interests, ".")

  comparison_ids <- vapply(programme_data$programmes, function(programme) {
    id <- programme$comparisonId
    if (is.null(id) || !nzchar(as.character(id))) id <- programme$exampleId
    if (is.null(id)) "" else as.character(id)
  }, character(1))
  if (any(!nzchar(comparison_ids))) stop("A programme in ", definition$programmes, " has no comparison ID.")

  comparison_files <- file.path(definition$comparison_directory, paste0(comparison_ids, ".json"))
  missing_comparisons <- comparison_files[!file.exists(file.path(repo_root, comparison_files))]
  if (length(missing_comparisons)) {
    stop("Missing comparison file(s) for ", mode_name, " mode: ", paste(missing_comparisons, collapse = ", "))
  }
  if (mode_name != "pilot") {
    for (index in seq_along(comparison_ids)) {
      record <- jsonlite::fromJSON(file.path(repo_root, comparison_files[[index]]), simplifyVector = FALSE)
      status <- record$recordStatus %||% "comparison"
      if (!identical(record$id, comparison_ids[[index]]) ||
          !status %in% c("comparison", "exception") ||
          (identical(status, "exception") && (!nzchar(record$exception$reason %||% "") ||
                                               length(record$programmes %||% list()) != 1L)) ||
          (identical(status, "comparison") && length(record$programmes %||% list()) < 2L)) {
        stop("Invalid completed counselor record for ", comparison_ids[[index]], ".")
      }
      indexed_status <- programme_data$programmes[[index]]$recordStatus %||% "comparison"
      if (!identical(status, indexed_status)) stop("Stale counselor index status for ", comparison_ids[[index]], ".")
    }
  }
  comparison_files
}

available_modes <- names(mode_available)[mode_available]
referenced_comparisons <- unique(unlist(lapply(available_modes, comparison_files_for), use.names = FALSE))
index_files <- unique(unlist(lapply(mode_definitions[available_modes], function(definition) {
  c(definition$programmes, definition$interests)
}), use.names = FALSE))
course_directory <- "pilot/shiny/data/courses"
course_files <- file.path(course_directory, list.files(file.path(repo_root, course_directory), pattern = "^[A-Z]{3}\\.json$"))
if (!length(course_files)) stop("No UCR course-description files found in ", course_directory, ".")

runtime_files <- sort(unique(c(
  required_files,
  index_files,
  referenced_comparisons,
  course_files
)))

missing_runtime <- runtime_files[!file.exists(file.path(repo_root, runtime_files))]
if (length(missing_runtime)) stop("Deployment selection contains missing files: ", paste(missing_runtime, collapse = ", "))

active_mode <- available_modes[[1]]
bundle_bytes <- sum(file.info(file.path(repo_root, runtime_files))$size)
cat(
  "Counselor deployment selection is valid.\n",
  "Active data mode: ", active_mode, "\n",
  "Available data modes: ", paste(available_modes, collapse = ", "), "\n",
  "Files: ", length(runtime_files), "\n",
  "Size: ", format(bundle_bytes, big.mark = ",", scientific = FALSE), " bytes\n",
  sep = ""
)

if ("--check" %in% args) quit(status = 0)

if (!requireNamespace("rsconnect", quietly = TRUE)) {
  stop("Install the rsconnect package before checking or deploying the counselor app.")
}

if ("--check-bundle" %in% args) {
  selected_files <- rsconnect::listDeploymentFiles(repo_root, appFiles = runtime_files)
  if (!identical(sort(selected_files), sort(runtime_files))) {
    stop("rsconnect did not select exactly the expected counselor runtime files.")
  }
  dependencies <- rsconnect::appDependencies(
    appDir = repo_root,
    appFiles = runtime_files,
    appMode = "shiny",
    dependencyResolution = "library"
  )
  expected_packages <- c("jsonlite", "shiny")
  missing_packages <- setdiff(expected_packages, dependencies$Package)
  if (length(missing_packages)) {
    stop("rsconnect did not detect required package(s): ", paste(missing_packages, collapse = ", "))
  }
  manifest_path <- file.path(repo_root, "manifest.json")
  if (file.exists(manifest_path)) stop("Refusing to overwrite existing manifest.json during the bundle check.")
  tryCatch({
    rsconnect::writeManifest(
      appDir = repo_root,
      appFiles = runtime_files,
      appPrimaryDoc = "pilot/counselor-shiny/app.R",
      appMode = "shiny",
      dependencyResolution = "library",
      quiet = TRUE
    )
    if (!file.exists(manifest_path)) stop("rsconnect did not create the temporary deployment manifest.")
  }, finally = {
    if (file.exists(manifest_path)) unlink(manifest_path)
  })
  cat("rsconnect bundle and dependency checks passed.\n")
  quit(status = 0)
}

account <- option_value("--account", Sys.getenv("SHINYAPPS_ACCOUNT", unset = ""))
app_name <- option_value("--app-name", Sys.getenv("UCR_COUNSELOR_SHINY_APP_NAME", unset = "ucr-counselor"))
if (!nzchar(app_name)) stop("The shinyapps.io application name cannot be blank.")

rsconnect::deployApp(
  appDir = repo_root,
  appFiles = runtime_files,
  appPrimaryDoc = "pilot/counselor-shiny/app.R",
  appName = app_name,
  appTitle = "UCR bachelor programme comparisons",
  account = if (nzchar(account)) account else NULL,
  server = "shinyapps.io",
  appMode = "shiny",
  recordDir = file.path(repo_root, "pilot", "counselor-shiny")
)
