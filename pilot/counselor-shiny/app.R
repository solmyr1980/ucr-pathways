library(shiny)
library(jsonlite)

# Run from the repository root or the app directory; keep code, assets and data in one deployed release.
root_candidates <- c(getwd(), file.path(getwd(), ".."), file.path(getwd(), "../.."))
REPO_ROOT <- root_candidates[file.exists(file.path(root_candidates, "assets/css/brand.css"))][1]
if (is.na(REPO_ROOT)) stop("Run this app from a complete ucr-pathways repository checkout or deployment bundle.")
REPO_ROOT <- normalizePath(REPO_ROOT)
source(file.path(REPO_ROOT, "pilot/shared.R"), local = TRUE)

COUNSELOR_DATA_DIR <- file.path(REPO_ROOT, "data", "counselor")
PRODUCTION_PROGRAMME_FILE <- file.path(COUNSELOR_DATA_DIR, "programmes.json")
PRODUCTION_INTEREST_FILE <- file.path(COUNSELOR_DATA_DIR, "interests.json")
PILOT_PROGRAMME_FILE <- file.path(COUNSELOR_DATA_DIR, "pilot-programmes.json")
PILOT_INTEREST_FILE <- file.path(COUNSELOR_DATA_DIR, "pilot-interests.json")
PRODUCTION_COMPARISON_DIR <- file.path(COUNSELOR_DATA_DIR, "comparisons")
PILOT_COMPARISON_DIR <- file.path(REPO_ROOT, "data", "examples")

USE_PRODUCTION_INDEX <- file.exists(PRODUCTION_PROGRAMME_FILE) && file.exists(PRODUCTION_INTEREST_FILE)
PROGRAMME_FILE <- if (USE_PRODUCTION_INDEX) PRODUCTION_PROGRAMME_FILE else PILOT_PROGRAMME_FILE
INTEREST_FILE <- if (USE_PRODUCTION_INDEX) PRODUCTION_INTEREST_FILE else PILOT_INTEREST_FILE
IS_PILOT_DATA <- !USE_PRODUCTION_INDEX

UCR_LOGO_URL <- "ucr-assets/brand/ucr-primary-plum.png"
UCR_WEBSITE_URL <- "https://ucr.nl/"
UCR_COURSES_URL <- "https://ucr.nl/education/courses/"
PROGRAM_BUILDER_URL <- "https://program.ucr.nl/"
UCR_COURSE_EC <- 7.5
SEARCH_DEBOUNCE_MS <- 250

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0 || identical(x, "")) y else x
}

safe_text <- function(x) {
  if (is.null(x) || length(x) == 0 || is.na(x[[1]]) || identical(x[[1]], "")) return("")
  as.character(x[[1]])
}

read_json_file <- function(path) {
  fromJSON(path, simplifyVector = FALSE)
}

norm <- function(x) {
  x <- iconv(safe_text(x), to = "ASCII//TRANSLIT", sub = "")
  x <- tolower(x %||% "")
  trimws(gsub("[^a-z0-9]+", " ", x))
}

relationship_weight <- function(x) {
  key <- tolower(safe_text(x))
  if (grepl("direct programme interest", key, fixed = TRUE)) return(100)
  if (grepl("stable study direction", key, fixed = TRUE)) return(80)
  if (grepl("curricular topic", key, fixed = TRUE)) return(60)
  if (grepl("illustrative", key, fixed = TRUE)) return(40)
  if (grepl("outcome", key, fixed = TRUE)) return(20)
  10
}

prepare_search_data <- function(programmes, interests) {
  prepared_programmes <- lapply(programmes, function(programme) {
    programme$searchNorm <- norm(paste(
      safe_text(programme$displayName),
      safe_text(programme$registryName),
      safe_text(programme$institution),
      safe_text(programme$degree),
      safe_text(programme$language)
    ))
    programme
  })

  prepared_interests <- lapply(interests, function(interest) {
    interest$searchNorm <- norm(interest$interest)
    interest$searchWeight <- relationship_weight(interest$relationship)
    interest
  })

  if (length(prepared_interests)) {
    provider_ids <- vapply(prepared_interests, function(x) as.character(x$programmeProviderId), character(1))
    interests_by_provider <- split(prepared_interests, provider_ids)
  } else {
    interests_by_provider <- list()
  }

  list(
    programmes = prepared_programmes,
    interestsByProvider = interests_by_provider
  )
}

# Load and prepare the discovery index once per R process, not once per counselor session.
COUNSELOR_DATA_ERROR <- NULL
COUNSELOR_DATA <- tryCatch({
  programme_payload <- read_json_file(PROGRAMME_FILE)
  interest_payload <- read_json_file(INTEREST_FILE)
  prepare_search_data(
    programme_payload$programmes %||% list(),
    interest_payload$interests %||% list()
  )
}, error = function(e) {
  COUNSELOR_DATA_ERROR <<- conditionMessage(e)
  list(programmes = list(), interestsByProvider = list())
})

comparison_id <- function(programme) {
  id <- safe_text(programme$comparisonId)
  if (!nzchar(id)) id <- safe_text(programme$exampleId)
  if (!nzchar(id)) id <- safe_text(programme$programmeProviderId)
  id
}

comparison_path <- function(id) {
  base_dir <- if (USE_PRODUCTION_INDEX) PRODUCTION_COMPARISON_DIR else PILOT_COMPARISON_DIR
  path <- file.path(base_dir, paste0(id, ".json"))
  if (!file.exists(path)) stop("No local comparison record found for ", id)
  path
}

term_hits_normalized <- function(terms, haystack) {
  if (!length(terms) || !nzchar(haystack)) return(0)
  sum(vapply(terms, function(term) grepl(term, haystack, fixed = TRUE), logical(1)))
}

search_programmes <- function(search_data, query = "", institution = "All", language = "All") {
  query_norm <- norm(query)
  terms <- unlist(strsplit(query_norm, "\\s+"))
  terms <- terms[nzchar(terms)]
  result <- list()

  for (programme in search_data$programmes) {
    if (!identical(institution, "All") && !identical(safe_text(programme$institution), institution)) next
    if (!identical(language, "All") && !identical(safe_text(programme$language), language)) next

    provider_id <- as.character(programme$programmeProviderId)
    p_interests <- search_data$interestsByProvider[[provider_id]] %||% list()
    programme_norm <- safe_text(programme$searchNorm)
    score <- 0
    matches <- list()

    if (!nzchar(query_norm)) {
      score <- 1
    } else {
      p_hits <- term_hits_normalized(terms, programme_norm)
      if (p_hits > 0) score <- score + 180 + 25 * p_hits
      if (grepl(query_norm, programme_norm, fixed = TRUE)) score <- score + 100

      for (interest in p_interests) {
        interest_norm <- safe_text(interest$searchNorm)
        hits <- term_hits_normalized(terms, interest_norm)
        if (hits > 0) {
          interest_score <- as.numeric(interest$searchWeight %||% relationship_weight(interest$relationship)) + 12 * hits
          if (grepl(query_norm, interest_norm, fixed = TRUE)) interest_score <- interest_score + 45
          score <- max(score, interest_score)
          matches[[length(matches) + 1]] <- list(
            interest = safe_text(interest$interest),
            relationship = safe_text(interest$relationship),
            score = interest_score
          )
        }
      }
    }

    if (score > 0) {
      if (length(matches)) matches <- matches[order(vapply(matches, function(x) -x$score, numeric(1)))]
      result[[length(result) + 1]] <- list(programme = programme, score = score, matches = head(matches, 3))
    }
  }

  if (!length(result)) return(list())
  result[order(
    vapply(result, function(x) -x$score, numeric(1)),
    vapply(result, function(x) safe_text(x$programme$displayName), character(1))
  )]
}

brand_header <- function() {
  div(
    class = "ucr-header",
    tags$a(
      href = UCR_WEBSITE_URL,
      target = "_blank",
      rel = "noopener",
      tags$img(src = UCR_LOGO_URL, class = "ucr-logo", alt = "University College Roosevelt")
    )
  )
}

comparator_meta <- function(record) record$comparator %||% record$referenceProgramme %||% list()

cell_value <- function(cell) {
  if (is.null(cell)) return(NULL)
  if (is.character(cell)) return(list(text = cell))
  if (is.list(cell) && nzchar(safe_text(cell$text))) return(cell)
  NULL
}

credit_text <- function(value, fallback = NULL) {
  if (!is.null(value) && nzchar(trimws(as.character(value)))) return(paste0(value, " EC"))
  if (!is.null(fallback)) return(paste0(fallback, " EC"))
  ""
}

render_compare_table <- function(record) {
  programmes <- record$programmes %||% list()
  meta <- comparator_meta(record)

  headers <- lapply(programmes, function(programme) {
    label <- visible_label(record, programme)
    if (identical(programme$role, "comparator") && nzchar(safe_text(meta$primarySourceUrl))) {
      title <- tags$a(href = meta$primarySourceUrl, target = "_blank", rel = "noopener", paste0(label, " ↗"))
    } else {
      title <- label
    }
    tags$th(
      div(class = "programme-title", title),
      if (!identical(programme$role, "comparator")) {
        tags$a(class = "programme-source", href = UCR_COURSES_URL, target = "_blank", rel = "noopener", "UCR courses ↗")
      }
    )
  })

  rows <- list()
  for (block in record$blocks %||% list()) {
    rows[[length(rows) + 1]] <- tags$tr(class = "block-row", tags$th(colspan = length(programmes), safe_text(block$title)))
    for (row in block$rows %||% list()) {
      cells <- lapply(programmes, function(programme) {
        value <- cell_value(row$cells[[programme$id]])
        if (is.null(value)) return(tags$td(class = "empty-cell", "\u00A0"))
        ec <- credit_text(value$credits, if (!identical(programme$role, "comparator")) UCR_COURSE_EC else NULL)
        tags$td(
          class = if (isTRUE(value$emphasis)) "comparison-cell emphasis" else "comparison-cell",
          div(class = "cell-text", safe_text(value$text)),
          if (nzchar(ec)) div(class = "ec-badge", ec),
          if (nzchar(safe_text(value$note))) div(class = "cell-note", safe_text(value$note))
        )
      })
      rows[[length(rows) + 1]] <- do.call(tags$tr, cells)
    }
  }

  div(
    class = "compare-scroll",
    tags$table(
      class = "compare-table",
      tags$thead(do.call(tags$tr, headers)),
      tags$tbody(do.call(tagList, rows))
    )
  )
}

render_result_cards <- function(results) {
  if (!length(results)) return(div(class = "no-results", "No matching programmes were found."))

  do.call(tagList, lapply(results, function(result) {
    programme <- result$programme
    matches <- result$matches %||% list()
    div(
      class = "result-card",
      div(
        class = "result-main",
        tags$h3(safe_text(programme$displayName)),
        tags$p(class = "institution", safe_text(programme$institution)),
        if (length(matches)) {
          div(
            class = "match-line",
            tags$strong("Matching interests: "),
            paste(vapply(matches, function(x) paste0(x$interest, " (", x$relationship, ")"), character(1)), collapse = " · ")
          )
        } else if (nzchar(safe_text(programme$registryName)) && !identical(programme$registryName, programme$displayName)) {
          div(class = "match-line", paste0("Registry name: ", programme$registryName))
        }
      ),
      tags$button(type = "button", class = "open-comparison", `data-id` = comparison_id(programme), "Compare with UCR")
    )
  }))
}

render_comparison <- function(record) {
  div(
    class = "comparison-shell",
    brand_header(),
    div(
      class = "comparison-head",
      div(
        tags$h1("See how this bachelor compares with study options at UCR"),
        tags$p("This is a pre-produced programme comparison. Your search helped you find the programme; it did not personalize the comparison.")
      ),
      actionButton("back_to_search", "← Back to search", class = "secondary-button")
    ),
    render_compare_table(record),
    render_comparison_notes(record),
    div(
      class = "transparency-note",
      tags$strong("How to read this comparison"),
      tags$p("The first UCR programme is the closest feasible match. The other two show broader ways of combining the field with related subjects and interests. These are illustrative feasible compositions, not official UCR tracks or guaranteed future schedules.")
    ),
    div(class = "cta-row", tags$a(class = "primary-cta", href = PROGRAM_BUILDER_URL, target = "_blank", rel = "noopener", "Explore the UCR Program Builder ↗"))
  )
}

render_search_shell <- function(search_text = "") {
  div(
    brand_header(),
    div(
      class = "hero",
      tags$h1("See how different bachelor’s programmes compare with study options at UCR"),
      tags$p("Search by bachelor’s programme or by what your student is interested in. Select a programme to see the closest UCR match and two broader ways of combining the field with related subjects and interests.")
    ),
    div(
      class = "search-box",
      div(
        class = "search-grid",
        textInput("search_text", "Search by programme or interest", value = search_text, placeholder = "e.g. Psychology, climate change, artificial intelligence…"),
        uiOutput("institution_filter"),
        uiOutput("language_filter")
      ),
      if (IS_PILOT_DATA) {
        div(class = "pilot-note", paste0("Pilot: this search currently contains ", length(COUNSELOR_DATA$programmes), " programme-provider comparisons. The production app will use the full deterministic comparison library."))
      }
    ),
    uiOutput("search_results")
  )
}

ui <- fluidPage(
  tags$head(
    tags$meta(name = "viewport", content = "width=device-width, initial-scale=1"),
    tags$title("Compare bachelor programmes with UCR"),
    tags$style(HTML("
      html,body{margin:0;background:var(--white);color:var(--black);font-family:Inter,Arial,sans-serif} body::before{content:'';display:block;height:24px;background:var(--plum)}
      .container-fluid{max-width:1500px;padding:0 28px 52px} h1,h2,h3{font-family:IvyMode,Georgia,serif;color:var(--plum);font-weight:400}
      .ucr-header{padding:24px 0 20px}.ucr-logo{width:auto;max-width:245px;max-height:68px}.hero{margin-bottom:22px}.hero h1{font-size:clamp(34px,3.2vw,50px);line-height:1.05;margin:0 0 12px;max-width:1050px}.hero p{color:var(--grey);font-size:17px;line-height:1.55;max-width:950px}
      .search-box{background:#fff;border:1px solid rgba(73,30,52,.16);border-radius:16px;padding:20px;margin-bottom:20px}.search-grid{display:grid;grid-template-columns:minmax(0,1fr) 260px 180px;gap:12px;align-items:end}.form-control{min-height:48px;border-radius:10px;border-color:rgba(73,30,52,.28);font-size:16px}.pilot-note{background:rgba(255,225,164,.45);border-radius:10px;padding:10px 13px;color:var(--grey);font-size:13px;margin-top:12px}
      .results-meta{color:var(--grey);margin:4px 0 12px}.results{display:grid;gap:10px}.result-card{display:flex;justify-content:space-between;align-items:center;gap:20px;background:#fff;border:1px solid rgba(73,30,52,.14);border-radius:14px;padding:17px 18px}.result-card h3{margin:0 0 4px;font-size:23px}.institution{margin:0;color:var(--grey)}.match-line{color:var(--grey);font-size:13px;margin-top:8px;line-height:1.4}.open-comparison{background:var(--plum);color:#fff;border:0;border-radius:9px;padding:11px 14px;font-weight:700;white-space:nowrap}.no-results{padding:26px;background:#fff;border-radius:14px;color:var(--grey)}
      .comparison-head{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;margin-bottom:18px}.comparison-head h1{margin:0 0 8px;font-size:clamp(31px,3vw,43px)}.comparison-head p{color:var(--grey);max-width:850px}.secondary-button{background:transparent!important;color:var(--plum)!important;border:1px solid rgba(73,30,52,.28)!important;border-radius:10px}
      .compare-scroll{overflow-x:auto;border:1px solid rgba(73,30,52,.14);border-radius:14px;background:#fff}.compare-table{border-collapse:separate;border-spacing:0;min-width:1120px;width:100%;table-layout:fixed}.compare-table th,.compare-table td{border-right:1px solid rgba(73,30,52,.1);border-bottom:1px solid rgba(73,30,52,.1);padding:13px 15px;vertical-align:top}.compare-table thead th{background:var(--plum);color:#fff;border-right-color:rgba(255,255,255,.18)}.programme-title{font-size:16px;font-weight:700}.programme-title a,.programme-source{color:inherit}.programme-source{display:inline-block;margin-top:5px;color:#fff;opacity:.82;font-size:12px}.block-row th{background:var(--blue);color:var(--plum);font-size:14px;font-weight:700}.comparison-cell{background:#fff;line-height:1.35}.comparison-cell.emphasis{background:rgba(255,225,164,.36)}.empty-cell{background:rgba(92,96,107,.035)}.ec-badge{display:inline-block;margin-top:6px;padding:2px 6px;border-radius:999px;background:rgba(73,30,52,.08);color:var(--grey);font-size:11px}.cell-note{color:var(--grey);font-size:12px;margin-top:5px}.transparency-note{margin-top:18px;background:#fff;border-left:5px solid var(--plum);padding:14px 17px;color:var(--grey);line-height:1.5}.transparency-note p{margin:5px 0 0}.cta-row{display:flex;justify-content:flex-end;margin-top:20px}.primary-cta{display:inline-block;background:var(--plum);color:#fff!important;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none!important}
      @media(max-width:900px){.container-fluid{padding:0 14px 40px}.search-grid{grid-template-columns:1fr}.result-card{display:block}.open-comparison{margin-top:13px}.comparison-head{display:block}.comparison-head .secondary-button{margin-top:10px}.ucr-logo{max-width:210px}}
    ")),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/brand.css"),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/shiny.css"),
    tags$script(HTML("
      $(document).on('click', '.open-comparison', function(){
        Shiny.setInputValue('open_comparison', String($(this).data('id')), {priority:'event'});
      });
    "))
  ),
  uiOutput("app_body")
)

server <- function(input, output, session) {
  selected <- reactiveVal(NULL)
  saved_search <- reactiveValues(text = "", institution = "All", language = "All")
  observeEvent(input$search_text, saved_search$text <- input$search_text)
  observeEvent(input$institution, saved_search$institution <- input$institution)
  observeEvent(input$language, saved_search$language <- input$language)

  search_inputs <- reactive({
    list(
      query = input$search_text %||% "",
      institution = input$institution %||% "All",
      language = input$language %||% "All"
    )
  })
  debounced_search_inputs <- debounce(search_inputs, SEARCH_DEBOUNCE_MS)

  results <- reactive({
    if (nzchar(safe_text(COUNSELOR_DATA_ERROR))) return(list())
    params <- debounced_search_inputs()
    search_programmes(COUNSELOR_DATA, params$query, params$institution, params$language)
  })

  output$app_body <- renderUI({
    record <- selected()
    if (!is.null(record)) return(render_comparison(record))
    render_search_shell(isolate(saved_search$text))
  })

  output$institution_filter <- renderUI({
    institutions <- sort(unique(vapply(COUNSELOR_DATA$programmes, function(x) safe_text(x$institution), character(1))))
    selectInput("institution", "Institution", choices = c("All", institutions), selected = isolate(saved_search$institution))
  })

  output$language_filter <- renderUI({
    languages <- sort(unique(vapply(COUNSELOR_DATA$programmes, function(x) safe_text(x$language), character(1))))
    labels <- vapply(languages, function(x) switch(x, ENG = "English", NLD = "Dutch", x), character(1))
    selectInput("language", "Teaching language", choices = c("All" = "All", setNames(languages, labels)), selected = isolate(saved_search$language))
  })

  output$search_results <- renderUI({
    if (nzchar(safe_text(COUNSELOR_DATA_ERROR))) {
      return(div(class = "no-results", "The counselor comparison index could not be loaded from the deployed application data."))
    }
    found <- results()
    tagList(
      div(class = "results-meta", paste0(length(found), " programme", if (length(found) == 1) "" else "s", " found")),
      div(class = "results", render_result_cards(found))
    )
  })

  observeEvent(input$open_comparison, {
    id <- safe_text(input$open_comparison)
    if (!grepl("^[A-Za-z0-9._-]+$", id)) return()
    tryCatch({
      record <- read_json_file(comparison_path(id))
      record$origin <- "counselor" # Presentation context only; fixture provenance is unchanged.
      selected(record)
    }, error = function(e) {
      showModal(modalDialog(
        title = "Could not load comparison",
        "The selected comparison could not be loaded from the deployed application data.",
        easyClose = TRUE,
        footer = modalButton("Close")
      ))
      message("Counselor comparison load error: ", conditionMessage(e))
    })
  })

  observeEvent(input$back_to_search, selected(NULL))
}

shinyApp(ui, server)
