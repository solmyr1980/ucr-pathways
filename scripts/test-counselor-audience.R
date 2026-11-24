e <- new.env()
source("pilot/counselor-shiny/app.R", local = e)
load_record <- function(id) jsonlite::fromJSON(paste0("data/counselor/comparisons/", id, ".json"), simplifyVector = FALSE)
# A multilingual programme appears in every applicable filter in the original search order.
language_fixture <- e$prepare_search_data(list(
  list(programmeProviderId = "one", displayName = "One", language = "ENG,NLD"),
  list(programmeProviderId = "two", displayName = "Two", language = "NLD / DEU / ENG"),
  list(programmeProviderId = "three", displayName = "Three", language = "ENG"),
  list(programmeProviderId = "four", displayName = "Four", language = "")
), list())
ids <- function(results) vapply(results, function(x) x$programme$programmeProviderId, character(1))
all_ids <- ids(e$search_programmes(language_fixture))
for (lang in c("ENG", "NLD", "DEU")) {
  eligible <- switch(lang, ENG = c("one","two","three"), NLD = c("one","two"), DEU = "two")
  stopifnot(identical(ids(e$search_programmes(language_fixture, language = lang)),
                      all_ids[all_ids %in% eligible]))
}

phrase_fixture <- e$prepare_search_data(list(
  list(programmeProviderId = "title", displayName = "Political Economy", language = "ENG"),
  list(programmeProviderId = "interest", displayName = "History", language = "NLD"),
  list(programmeProviderId = "split", displayName = "Political", institution = "Economy Institute"),
  list(programmeProviderId = "substring", displayName = "Geopolitical Economy")
), list(
  list(programmeProviderId = "interest", interest = "European political-economy since 1945"),
  list(programmeProviderId = "interest", interest = "Political thought"),
  list(programmeProviderId = "split", interest = "The economy"),
  list(programmeProviderId = "split", interest = "Political"),
  list(programmeProviderId = "split", interest = "Economy and political institutions")
))
search <- function(query, ...) e$search_programmes(phrase_fixture, query, ...)
exact <- search('"political economy"')
stopifnot(identical(ids(exact), c("title", "interest")),
          identical(exact[[2]]$matches[[1]]$interest, "European political-economy since 1945"),
          length(exact[[2]]$matches) == 1L,
          identical(ids(search('“POLITICAL ECONOMY”')), ids(exact)),
          identical(ids(search('"political economy"', language = "NLD")), "interest"),
          identical(ids(search('"political economy" "political thought"')), "interest"),
          setequal(ids(search('"political economy" institutions')), ids(exact)),
          identical(ids(search('"political economy')), ids(search("political economy"))),
          length(search("political economy")) == 4L)

r <- load_record("cp-000019")
before <- serialize(r, NULL)
r$audience <- NULL # Explicit unreviewed legacy fixture.
r$comparator$sourceNotes <- r$comparator$academicYear <- r$comparator$route <- "INTERNAL-SENTINEL"
r$notes <- lapply(r$notes, function(n) { n$text <- "INTERNAL-SENTINEL"; n })
r$blocks <- lapply(r$blocks, function(b) { b$rows <- lapply(b$rows, function(row) { row$cells <- lapply(row$cells, function(cell) { if (is.list(cell)) cell$note <- "INTERNAL-SENTINEL"; cell }); row }); b })
html <- as.character(e$render_comparison(r))
stopifnot(!grepl("INTERNAL-SENTINEL", html, fixed = TRUE), !grepl("awaiting review", html, fixed = TRUE))
stopifnot(grepl("column-select", html, fixed = TRUE), grepl("blank cell", html, fixed = TRUE))
r$audience <- list(schemaVersion = "1.0", programmeDescription = "Study art and culture in society.", comparisonExplanation = "The required specialist placement differs.", conceptProgrammeIds = list("ucr-1"), cellNotes = list(list(programmeId = "comparator", reference = r$comparator$components[[1]]$id, text = "Reviewed partial correspondence.")))
html <- as.character(e$render_comparison(r))
stopifnot(!grepl("Study art and culture in society", html), !grepl("required specialist placement differs", html), !grepl("Reviewed partial correspondence", html), !grepl("INTERNAL-SENTINEL", html))
stopifnot(!grepl(htmltools::htmlEscape(r$academicRationale$alternatives[[1]]$concept), html, fixed = TRUE))
x <- load_record("cp-000277")
x$audience <- NULL # Explicit unreviewed exception fixture.
x$acceptance <- NULL
x$exception$type <- "external-programme-unresolved"
x$exception$reason <- x$exception$curriculumContext <- x$comparator$academicYear <- x$comparator$sourceNotes <- "INTERNAL-SENTINEL"
html <- as.character(e$render_comparison(x))
stopifnot(!grepl("INTERNAL-SENTINEL", html), !grepl("external-table", html), grepl("Insufficient verified evidence for a reliable comparison", html))
x$audience <- list(schemaVersion = "1.0", curriculum = list(status = "partial", componentIds = list(x$comparator$components[[1]]$id), limitation = "A required 5 EC remains unidentified."))
html <- as.character(e$render_comparison(x))
stopifnot(grepl("Verified partial curriculum", html), !grepl("required 5 EC remains unidentified", html),
          grepl("external-table", html),
          grepl(htmltools::htmlEscape(x$comparator$components[[1]]$name), html, fixed = TRUE),
          !grepl(htmltools::htmlEscape(x$comparator$components[[2]]$name), html, fixed = TRUE))
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


e$COUNSELOR_PRESENTATION <- e$read_presentation_settings(e$PRESENTATION_FILE)

# A caution or bounded comparison needs reviewed copy before release. Run across
# the real corpus so a newly added case cannot silently use the ordinary default.
for (path in list.files("data/counselor/comparisons", pattern = "^cp-.*\\.json$", full.names = TRUE)) {
  record <- jsonlite::fromJSON(path, simplifyVector = FALSE)
  setting <- e$presentation_setting(record$id)
  if (identical(record$recordStatus, "exception") || identical(setting$mode, "external-only")) next
  view <- e$curriculum_view(record)
  qualified <- e$qualified_comparison(record)
  if (view$status %in% c("partial", "unresolved") && !qualified) next
  paragraph <- e$safe_text(setting$introduction)
  if (identical(setting$mode, "caution") || qualified) stopifnot(nzchar(paragraph))
  stopifnot(identical(grepl("{credits}", paragraph, fixed = TRUE), qualified))
  intro <- as.character(e$comparison_introduction(setting, qualified, view, record$audience$comparisonScope))
  row_sentence <- "Courses in the same row cover related material without necessarily being equivalent."
  stopifnot(!grepl("{credits}", intro, fixed = TRUE),
            grepl("blank cell", intro, ignore.case = TRUE),
            lengths(regmatches(intro, gregexpr(row_sentence, intro, fixed = TRUE))) == 1L,
            grepl("closest", intro) || record$id == "cp-000373")
  blocks <- e$counselor_blocks(record, setting)
  final_rows <- blocks[[length(blocks)]]$rows
  final_ids <- vapply(final_rows, function(r) e$safe_text(r$cells$comparator$componentId), character(1))
  stopifnot(all(unlist(setting$closingChoices) %in% final_ids),
            all(names(setting$blockTitles) %in% vapply(blocks, function(b) e$safe_text(b$id), character(1))))
  first_ucr <- Filter(e$is_ucr_programme, record$programmes)[[1]]$id
  has_research <- function(block) any(vapply(block$rows, function(row)
    identical(row$cells[[first_ucr]]$comparisonElementId, "optional-independent-research"), logical(1)))
  expected_block <- if (isTRUE(setting$keepResearchInBlock)) {
    Filter(has_research, record$blocks)[[1]]$id
  } else blocks[[length(blocks)]]$id
  stopifnot(identical(Filter(has_research, blocks)[[1]]$id, expected_block))
  if (!is.null(setting$closingBlock)) stopifnot(identical(tail(record$blocks, 1L)[[1]]$id, setting$closingBlock))
  if (qualified) {
    documented <- sum(vapply(view$components, function(x) as.numeric(x$credits), numeric(1)))
    stopifnot(grepl(paste(format(documented, trim = TRUE), "of 180 EC"), intro, fixed = TRUE))
  }
}
cat("Corpus introductions, research and elective placement, and qualified credit totals passed.\n")
