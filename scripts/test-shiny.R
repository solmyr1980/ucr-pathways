Sys.setenv(UCR_PILOT_LOCAL_DATA = "true")
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

programmes <- counselor$fetch_json(counselor$PROGRAMME_URL)$programmes
interests <- counselor$fetch_json(counselor$INTEREST_URL)$interests
stopifnot(length(counselor$search_programmes(programmes, interests)) == 5)
stopifnot(length(counselor$search_programmes(programmes, interests, language = "NLD")) == 2)
stopifnot(length(counselor$search_programmes(programmes, interests, query = "zzzzzzzz")) == 0)
stopifnot(counselor$relationship_weight("Direct programme interest") > counselor$relationship_weight("Outcome or individual trajectory"))

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
  session$setInputs(search_text = "crime", open_comparison = "p-004")
  stopifnot(identical(selected()$id, "p-004"))
  session$setInputs(back_to_search = 1)
  stopifnot(is.null(selected()), identical(saved_search$text, "crime"))
})

shiny::testServer(student$server, {
  session$setInputs(access_code = tolower(codes$entries[[1]]$code), unlock_pathway = 1)
  stopifnot(identical(record()$id, codes$entries[[1]]$example_id))
  session$setInputs(reset_pathway = 1)
  stopifnot(is.null(record()))
})
cat("Shiny behavior checks passed.\n")
