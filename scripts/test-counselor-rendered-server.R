# Local browser-test server only; no corpus files or presentation settings written.
args <- commandArgs(trailingOnly = TRUE)
variant <- args[[1]]
port <- as.integer(args[[2]])
e <- new.env()
app <- source("pilot/counselor-shiny/app.R", local = e)$value
if (identical(variant, "fixtures")) {
  original <- e$read_json_file
  e$read_json_file <- function(path) {
    r <- original(path)
    if (!grepl("^cp-[0-9]{6}\\.json$", basename(path))) return(r)
    # Deliberately contaminated internal fields must never enter displayed prose.
    r$comparator$sourceNotes <- r$comparator$academicYear <- r$comparator$route <- "INTERNAL-SENTINEL-DO-NOT-DISPLAY"
    if (!is.null(r$exception)) r$exception$reason <- r$exception$curriculumContext <- "INTERNAL-SENTINEL-DO-NOT-DISPLAY"
    r$comparator$components <- lapply(r$comparator$components, function(c) { c$note <- "INTERNAL-SENTINEL-DO-NOT-DISPLAY"; c })
    r$blocks <- lapply(r$blocks, function(b) { b$rows <- lapply(b$rows, function(row) { row$cells <- lapply(row$cells, function(c) { if (is.list(c)) c$note <- "INTERNAL-SENTINEL-DO-NOT-DISPLAY"; c }); row }); b })
    if (r$id == "cp-000277") {
      r$audience <- list(schemaVersion = "1.0", programmeDescription = "African Studies examines African societies, languages, history and cultural life.", comparisonExplanation = "A full comparison is unavailable while a required component remains unidentified.", curriculum = list(status = "partial", componentIds = lapply(r$comparator$components, function(c) c$id), yearLabel = "2026–2027", limitation = "The verified list accounts for 175 EC. A required 5 EC remains unidentified; it is not a complete degree."))
    } else if (r$id %in% c("cp-000004", "cp-000002", "cp-000119")) {
      r$audience <- list(schemaVersion = "1.0", programmeDescription = "Explore the programme and its curriculum through the official source.", comparisonExplanation = "Specialist study and practical requirements differ from the UCR options.", conceptProgrammeIds = lapply(Filter(e$is_ucr_programme, r$programmes), function(p) p$id), curriculum = list(status = "complete", componentIds = lapply(r$comparator$components, function(c) c$id), yearLabel = "2026–2027", routeLabel = "Selected programme pathway"))
      if (r$id == "cp-000004") {
        r$audience$noteTypes <- lapply(r$notes, function(n) n$type)
        # Existing canonical concepts and limitation text selected, not rewritten.
      }
    } else if (r$id == "cp-000005") r$audience <- list(schemaVersion = "1.0", programmeDescription = "This programme description has been reviewed; other content remains under review.")
    r
  }
  e$COUNSELOR_PRESENTATION[["cp-000002"]] <- list(mode = "external-only", message = "INTERNAL-SENTINEL-DO-NOT-DISPLAY")
  e$COUNSELOR_PRESENTATION[["cp-000003"]] <- list(mode = "caution", message = "INTERNAL-SENTINEL-DO-NOT-DISPLAY")
}
shiny::runApp(app, host = "127.0.0.1", port = port, launch.browser = FALSE)
