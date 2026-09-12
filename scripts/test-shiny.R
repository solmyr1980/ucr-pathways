student <- new.env()
counselor <- new.env()
source("pilot/shiny/app.R", local = student)
source("pilot/counselor-shiny/app.R", local = counselor)
codes <- jsonlite::fromJSON("pilot/shiny/data/access_codes.json", simplifyVector = FALSE)
for (entry in codes$entries) {
  stopifnot(identical(student$find_example_id(codes, tolower(gsub("-", " ", entry$code))), entry$example_id))
}
stopifnot(is.null(student$find_example_id(codes, "invalid")))
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

first_programme <- counselor$COUNSELOR_DATA$programmes[[1]]
test_comparison_id <- counselor$comparison_id(first_programme)
stopifnot(nzchar(test_comparison_id), file.exists(counselor$comparison_path(test_comparison_id)))
test_record <- jsonlite::fromJSON(counselor$comparison_path(test_comparison_id), simplifyVector = FALSE)

for (id in sprintf("p-%03d", 1:5)) {
  record <- jsonlite::fromJSON(paste0("data/examples/", id, ".json"), simplifyVector = FALSE)
  for (app in list(student, counselor)) {
    rendered <- as.character(app$render_compare_table(record))
    stopifnot(grepl("7.5 EC", rendered, fixed = TRUE), grepl("UCR courses", rendered, fixed = TRUE))
    for (note in record$notes) stopifnot(grepl(htmltools::htmlEscape(note$text), as.character(app$render_comparison_notes(record)), fixed = TRUE))
  }
}

shiny::testServer(counselor$server, {
  session$flushReact()
  shell <- output$app_body
  session$setInputs(search_text = "climate", institution = "All", language = "All")
  stopifnot(identical(shell, output$app_body)) # Typing must not recreate the input.
  session$setInputs(search_text = "test query", open_comparison = test_comparison_id)
  stopifnot(identical(selected()$id, test_record$id))
  session$setInputs(back_to_search = 1)
  stopifnot(is.null(selected()), identical(saved_search$text, "test query"))
})

shiny::testServer(student$server, {
  session$setInputs(access_code = tolower(codes$entries[[1]]$code), unlock_pathway = 1)
  stopifnot(identical(record()$id, codes$entries[[1]]$example_id))
  session$setInputs(reset_pathway = 1)
  stopifnot(is.null(record()))
})
cat("Shiny behavior checks passed.\n")
