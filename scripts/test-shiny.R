student <- new.env()
counselor <- new.env()
Sys.setenv(UCR_STUDENT_DATA_MODE = "public")
source("pilot/shiny/app.R", local = student)
source("pilot/counselor-shiny/app.R", local = counselor)
codes <- jsonlite::fromJSON("pilot/shiny/data/access_codes.json", simplifyVector = FALSE)
for (entry in codes$entries) {
  formatted <- tolower(gsub("-", " ", entry$code))
  loaded <- student$load_student_record_for_code(student$STUDENT_DATA_CONFIG, formatted)
  stopifnot(identical(loaded$id, entry$example_id))
}
stopifnot(identical(student$STUDENT_DATA_CONFIG$mode, "public"))
stopifnot(is.null(student$load_student_record_for_code(student$STUDENT_DATA_CONFIG, "invalid")))
stopifnot(is.na(student$normalize_student_code("UCR/INVALID")))
stopifnot(identical(student$course_level(3), "300-level"))

# Counselor data must be local, process-level and pre-indexed.
stopifnot(file.exists(counselor$PROGRAMME_FILE), file.exists(counselor$INTEREST_FILE))
stopifnot(!grepl("^https?://", counselor$PROGRAMME_FILE), !grepl("^https?://", counselor$INTEREST_FILE))
stopifnot(length(counselor$COUNSELOR_DATA$programmes) > 0)
stopifnot(length(counselor$search_programmes(counselor$COUNSELOR_DATA)) == length(counselor$COUNSELOR_DATA$programmes))
stopifnot(length(counselor$search_programmes(counselor$COUNSELOR_DATA, query = "zzzzzzzz")) == 0)
stopifnot(counselor$relationship_weight("Direct programme interest") > counselor$relationship_weight("Outcome or individual trajectory"))
stopifnot(all(vapply(counselor$COUNSELOR_DATA$programmes, function(x) nzchar(x$searchNorm), logical(1))))

nld_results <- counselor$search_programmes(counselor$COUNSELOR_DATA, language = "NLD")
stopifnot(all(vapply(nld_results, function(x) identical(x$programme$language, "NLD"), logical(1))))
if (counselor$IS_PILOT_DATA) {
  stopifnot(length(counselor$COUNSELOR_DATA$programmes) == 5, length(nld_results) == 2)
}
if (counselor$IS_REVIEW_DATA) {
  review_ids <- vapply(counselor$COUNSELOR_DATA$programmes, function(x) as.character(x$programmeProviderId), character(1))
  review_names <- vapply(counselor$COUNSELOR_DATA$programmes, function(x) as.character(x$displayName), character(1))
  expected_review_ids <- tools::file_path_sans_ext(sort(list.files(
    "data/counselor/comparisons",
    pattern = "^cp-[0-9]{6}\\.json$"
  )))
  stopifnot(identical(review_ids, expected_review_ids))
  stopifnot(identical(head(review_names, 4), c(
    "Bachelor of Public Administration",
    "Bachelor in Management of International Social Challenges",
    "Bachelor of Pedagogical Sciences",
    "Bachelor of Psychology"
  )))
  stopifnot(all(vapply(review_ids, function(id) file.exists(counselor$comparison_path(id)), logical(1))))
  psychology_results <- counselor$search_programmes(counselor$COUNSELOR_DATA, query = "psychology")
  stopifnot(any(vapply(psychology_results, function(x) identical(x$programme$programmeProviderId, "cp-000004"), logical(1))))
  stopifnot(length(counselor$search_programmes(counselor$COUNSELOR_DATA, query = "bestuurskunde")) == 0)
  stopifnot(!grepl("bestuurskunde", counselor$COUNSELOR_DATA$programmes[[1]]$searchNorm, fixed = TRUE))
}

first_programme <- counselor$COUNSELOR_DATA$programmes[[1]]
test_comparison_id <- counselor$comparison_id(first_programme)
stopifnot(nzchar(test_comparison_id), file.exists(counselor$comparison_path(test_comparison_id)))
test_record <- jsonlite::fromJSON(counselor$comparison_path(test_comparison_id), simplifyVector = FALSE)

# Counselor comparison summaries are derived from the four accepted production records.
acceptance_records <- lapply(sprintf("cp-%06d", 1:4), function(id) {
  record <- jsonlite::fromJSON(file.path("data/counselor/comparisons", paste0(id, ".json")), simplifyVector = FALSE)
  record$origin <- "counselor"
  record
})
expected_ucr_counts <- c(2L, 3L, 2L, 3L)
for (index in seq_along(acceptance_records)) {
  record <- acceptance_records[[index]]
  ucr_programmes <- counselor$ucr_programmes_for_summary(record)
  stopifnot(length(ucr_programmes) == expected_ucr_counts[[index]])
  summary_html <- as.character(counselor$render_comparison_summary(record))
  stopifnot(grepl("What this comparison shows", summary_html, fixed = TRUE))
  stopifnot(grepl("Important limitation", summary_html, fixed = TRUE))
  for (programme in ucr_programmes) {
    stopifnot(grepl(htmltools::htmlEscape(counselor$visible_label(record, programme)), summary_html, fixed = TRUE))
    rationale <- counselor$alternative_rationale_for(record, programme$id)
    if (!is.null(rationale) && nzchar(counselor$safe_text(rationale$concept))) {
      stopifnot(grepl(htmltools::htmlEscape(counselor$safe_text(rationale$concept)), summary_html, fixed = TRUE))
    }
  }
  route <- counselor$safe_text(counselor$comparator_meta(record)$route)
  if (nzchar(route)) stopifnot(grepl(htmltools::htmlEscape(route), summary_html, fixed = TRUE))
}
stopifnot(grepl("Brain &amp; Cognition specialisation", as.character(counselor$render_comparison_summary(acceptance_records[[4]])), fixed = TRUE))

# The summary-first view replaces the former generic bottom "How to read" note.
comparison_html <- as.character(counselor$render_comparison(acceptance_records[[1]]))
stopifnot(grepl("What this comparison shows", comparison_html, fixed = TRUE))
stopifnot(!grepl("How to read this comparison", comparison_html, fixed = TRUE))

# Relationship classifications remain internal ranking metadata, not counselor-facing search copy.
result_fixture <- list(list(
  programme = first_programme,
  matches = list(list(interest = "climate change", relationship = "Direct programme interest", score = 100))
))
result_html <- as.character(counselor$render_result_cards(result_fixture))
stopifnot(grepl("climate change", result_html, fixed = TRUE))
stopifnot(!grepl("Direct programme interest", result_html, fixed = TRUE))

for (id in sprintf("p-%03d", 1:5)) {
  record <- jsonlite::fromJSON(paste0("data/examples/", id, ".json"), simplifyVector = FALSE)
  for (app in list(student, counselor)) {
    rendered <- as.character(app$render_compare_table(record))
    stopifnot(grepl("7.5 EC", rendered, fixed = TRUE), grepl("UCR courses", rendered, fixed = TRUE))
    for (note in record$notes) stopifnot(grepl(htmltools::htmlEscape(note$text), as.character(app$render_comparison_notes(record)), fixed = TRUE))
  }

  student_options <- student$student_ucr_programmes(record)
  stopifnot(length(student_options) >= 1, length(student_options) <= 3)
  stopifnot(all(vapply(student_options, student$is_ucr_programme, logical(1))))
  programme_options_html <- as.character(student$render_programme_options(record))
  for (programme in student_options) {
    stopifnot(grepl(htmltools::htmlEscape(student$visible_label(record, programme)), programme_options_html, fixed = TRUE))
  }
}

# Explicitly exercise one- and two-alternative rendering using the first public fixture.
base_record <- jsonlite::fromJSON("data/examples/p-001.json", simplifyVector = FALSE)
base_ucr <- student$student_ucr_programmes(base_record)
stopifnot(length(base_ucr) >= 3)
for (count in c(1, 2)) {
  fixture <- base_record
  keep <- c(base_record$programmes[[1]]$id, vapply(base_ucr[seq_len(count)], function(x) x$id, character(1)))
  fixture$programmes <- c(list(base_record$programmes[[1]]), base_ucr[seq_len(count)])
  fixture$blocks <- lapply(fixture$blocks, function(block) {
    block$rows <- lapply(block$rows, function(row) {
      row$cells <- row$cells[names(row$cells) %in% keep]
      row
    })
    block$rows <- Filter(function(row) any(vapply(row$cells, function(cell) !is.null(cell) && length(cell) > 0, logical(1))), block$rows)
    block
  })
  fixture$blocks <- Filter(function(block) length(block$rows) > 0, fixture$blocks)
  stopifnot(length(student$student_ucr_programmes(fixture)) == count)
  stopifnot(nzchar(as.character(student$render_compare_table(fixture))))
  stopifnot(nzchar(as.character(student$render_programme_options(fixture))))
  stopifnot(nzchar(as.character(counselor$render_compare_table(fixture))))
}

shiny::testServer(counselor$server, {
  session$flushReact()
  shell <- output$app_body
  session$setInputs(search_text = "climate", institution = "All", language = "All")
  stopifnot(identical(shell, output$app_body)) # Typing must not recreate the input.
  session$setInputs(search_text = "test query", open_comparison = test_comparison_id)
  stopifnot(identical(selected()$id, test_record$id))
  if (!is.null(selected()$comparator)) stopifnot(identical(selected()$comparator$name, first_programme$displayName))
  if (!is.null(selected()$referenceProgramme)) stopifnot(identical(selected()$referenceProgramme$name, first_programme$displayName))
  session$setInputs(back_to_search = 1)
  stopifnot(is.null(selected()), identical(saved_search$text, "test query"))
})

shiny::testServer(student$server, {
  session$setInputs(access_code = tolower(codes$entries[[1]]$code), unlock_pathway = 1)
  stopifnot(identical(record()$id, codes$entries[[1]]$example_id))
  option_count <- length(student$student_ucr_programmes(record()))
  stopifnot(option_count >= 1, option_count <= 3)
  session$setInputs(reset_pathway = 1)
  stopifnot(is.null(record()))
})
cat("Shiny behavior checks passed.\n")
