e <- new.env()
source("pilot/counselor-shiny/app.R", local = e)
load_record <- function(id) jsonlite::fromJSON(paste0("data/counselor/comparisons/", id, ".json"), simplifyVector = FALSE)
r <- load_record("cp-000019")
before <- serialize(r, NULL)
r$audience <- NULL # Explicit unreviewed legacy fixture.
r$comparator$sourceNotes <- r$comparator$academicYear <- r$comparator$route <- "INTERNAL-SENTINEL"
r$notes <- lapply(r$notes, function(n) { n$text <- "INTERNAL-SENTINEL"; n })
r$blocks <- lapply(r$blocks, function(b) { b$rows <- lapply(b$rows, function(row) { row$cells <- lapply(row$cells, function(cell) { if (is.list(cell)) cell$note <- "INTERNAL-SENTINEL"; cell }); row }); b })
html <- as.character(e$render_comparison(r))
stopifnot(!grepl("INTERNAL-SENTINEL", html, fixed = TRUE), grepl("awaiting review", html, fixed = TRUE))
stopifnot(grepl("column-select", html, fixed = TRUE), grepl("blank cell", html, fixed = TRUE))
r$audience <- list(schemaVersion = "1.0", programmeDescription = "Study art and culture in society.", comparisonExplanation = "The required specialist placement differs.", conceptProgrammeIds = list("ucr-1"), cellNotes = list(list(programmeId = "comparator", reference = r$comparator$components[[1]]$id, text = "Reviewed partial correspondence.")))
html <- as.character(e$render_comparison(r))
stopifnot(grepl("Study art and culture in society", html), grepl("required specialist placement differs", html), grepl("Reviewed partial correspondence", html), !grepl("INTERNAL-SENTINEL", html))
stopifnot(grepl(htmltools::htmlEscape(r$academicRationale$alternatives[[1]]$concept), html, fixed = TRUE))
x <- load_record("cp-000277")
x$audience <- NULL # Explicit unreviewed exception fixture.
x$exception$reason <- x$exception$curriculumContext <- x$comparator$academicYear <- x$comparator$sourceNotes <- "INTERNAL-SENTINEL"
html <- as.character(e$render_comparison(x))
stopifnot(!grepl("INTERNAL-SENTINEL", html), !grepl("External programme components", html), grepl("no complete degree pathway is certified", html))
x$audience <- list(schemaVersion = "1.0", curriculum = list(status = "partial", componentIds = lapply(x$comparator$components, function(c) c$id), limitation = "A required 5 EC remains unidentified."))
html <- as.character(e$render_comparison(x))
stopifnot(grepl("Verified partial curriculum", html), grepl("required 5 EC remains unidentified", html))
x$audience$curriculum$status <- "complete"
stopifnot(identical(e$curriculum_view(x)$status, "unreviewed"))
x$audience <- list(schemaVersion = "1.0", curriculum = list(status = "partial"))
stopifnot(!length(e$curriculum_view(x)$components))
e$COUNSELOR_PRESENTATION[[r$id]] <- list(mode = "caution", message = "INTERNAL-SENTINEL")
stopifnot(!grepl("INTERNAL-SENTINEL", as.character(e$render_comparison(r))))
for (count in 1:3) {
  f <- load_record("cp-000019"); f$programmes <- f$programmes[1:(count+1)]
  html <- as.character(e$render_compare_table(f))
  stopifnot(grepl(paste0('data-count="',count+1,'"'), html, fixed = TRUE))
}
stopifnot(identical(serialize(load_record("cp-000019"), NULL), before))
for (code in c("BENBUSI211", "MCCHEAM316")) {
  d <- jsonlite::fromJSON(paste0("pilot/shiny/data/courses/", substr(code,1,3), ".json"))$descriptions[[code]]
  stopifnot(nzchar(d))
  if (code == "BENBUSI211") stopifnot(grepl("business, economic and societal",d,fixed=TRUE))
  else stopifnot(grepl("history of art history",d,fixed=TRUE))
}
stopifnot(grepl(e$COURSE_DESCRIPTION_UNAVAILABLE, as.character(e$course_description_dialog("UNKNOWN","Unknown",NULL)),fixed=TRUE))
cat("Counselor audience leakage, progressive review, incomplete curriculum and modal regression checks passed.\n")
