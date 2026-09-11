library(shiny)
library(jsonlite)

REPO_RAW <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main"
PROGRAMME_URL <- paste0(REPO_RAW, "/data/counselor/pilot-programmes.json")
INTEREST_URL <- paste0(REPO_RAW, "/data/counselor/pilot-interests.json")
EXAMPLE_BASE <- paste0(REPO_RAW, "/data/examples")
UCR_LOGO_URL <- paste0(REPO_RAW, "/assets/brand/ucr-primary-plum.png")
UCR_WEBSITE_URL <- "https://ucr.nl/"
UCR_COURSES_URL <- "https://ucr.nl/education/courses/"
PROGRAM_BUILDER_URL <- "https://program.ucr.nl/"
UCR_COURSE_EC <- 7.5

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0 || identical(x, "")) y else x
}

safe_text <- function(x) x %||% ""

cache_bust <- function(url) {
  separator <- if (grepl("\\?", url)) "&" else "?"
  paste0(url, separator, "cb=", sprintf("%.0f", as.numeric(Sys.time()) * 1000))
}

fetch_json <- function(url) fromJSON(cache_bust(url), simplifyVector = FALSE)

norm <- function(x) {
  x <- tolower(iconv(safe_text(x), to = "ASCII//TRANSLIT"))
  gsub("[^a-z0-9]+", " ", x)
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

visible_label <- function(record, programme) {
  meta <- comparator_meta(record)
  programme_name <- safe_text(meta$name)
  institution <- safe_text(meta$institution)
  if (identical(programme$role, "comparator")) return(paste0(programme_name, " at ", institution))
  if (identical(programme$role, "ucr-depth")) return(paste0("Closest match to ", programme_name))
  if (identical(programme$role, "ucr-balanced")) return(paste0(programme_name, " + related subjects"))
  if (identical(programme$role, "ucr-thematic")) return("A broader programme around related interests")
  safe_text(programme$label)
}

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

relationship_weight <- function(x) {
  key <- tolower(safe_text(x))
  if (grepl("direct programme interest", key, fixed = TRUE)) return(100)
  if (grepl("stable study direction", key, fixed = TRUE)) return(80)
  if (grepl("curricular topic", key, fixed = TRUE)) return(60)
  if (grepl("illustrative", key, fixed = TRUE)) return(40)
  if (grepl("outcome", key, fixed = TRUE)) return(20)
  10
}

term_hits <- function(query, text) {
  terms <- unlist(strsplit(norm(query), "\\s+"))
  terms <- terms[nzchar(terms)]
  if (!length(terms)) return(0)
  haystack <- norm(text)
  sum(vapply(terms, function(term) grepl(term, haystack, fixed = TRUE), logical(1)))
}

search_programmes <- function(programmes, interests, query = "", institution = "All") {
  query <- trimws(query)
  result <- list()

  for (programme in programmes) {
    if (!identical(institution, "All") && !identical(safe_text(programme$institution), institution)) next

    provider_id <- as.character(programme$programmeProviderId)
    p_interests <- Filter(function(x) identical(as.character(x$programmeProviderId), provider_id), interests)
    programme_text <- paste(programme$displayName, programme$registryName, programme$institution, programme$degree, programme$language)
    score <- 0
    matches <- list()

    if (!nzchar(query)) {
      score <- 1
    } else {
      p_hits <- term_hits(query, programme_text)
      if (p_hits > 0) score <- score + 180 + 25 * p_hits
      if (nzchar(norm(query)) && grepl(norm(query), norm(programme_text), fixed = TRUE)) score <- score + 100

      for (interest in p_interests) {
        hits <- term_hits(query, interest$interest)
        if (hits > 0) {
          interest_score <- relationship_weight(interest$relationship) + 12 * hits
          if (nzchar(norm(query)) && grepl(norm(query), norm(interest$interest), fixed = TRUE)) interest_score <- interest_score + 45
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
    vapply(result, function(x) x$programme$displayName, character(1))
  )]
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
        ec <- credit_text(value$credits, if (identical(programme$family, "ucr")) UCR_COURSE_EC else NULL)
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
  if (!length(results)) return(div(class = "no-results", "No matching pilot programmes were found."))

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
            paste(vapply(matches, function(x) x$interest, character(1)), collapse = " · ")
          )
        } else if (nzchar(safe_text(programme$registryName)) && !identical(programme$registryName, programme$displayName)) {
          div(class = "match-line", paste0("Registry name: ", programme$registryName))
        }
      ),
      tags$button(type = "button", class = "open-comparison", `data-id` = programme$exampleId, "Compare with UCR")
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
    div(
      class = "transparency-note",
      tags$strong("How to read this comparison"),
      tags$p("The first UCR programme is the closest feasible match. The other two show broader ways of combining the field with related subjects and interests. These are illustrative feasible compositions, not official UCR tracks or guaranteed future schedules.")
    ),
    div(class = "cta-row", tags$a(class = "primary-cta", href = PROGRAM_BUILDER_URL, target = "_blank", rel = "noopener", "Explore the UCR Program Builder ↗"))
  )
}

render_search_shell <- function() {
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
        textInput("search_text", "Search by programme or interest", placeholder = "e.g. Psychology, climate change, artificial intelligence…"),
        uiOutput("institution_filter")
      ),
      div(class = "pilot-note", "Pilot: this search currently contains five programme-provider comparisons. The production app will use the full deterministic comparison library.")
    ),
    uiOutput("search_results")
  )
}

ui <- fluidPage(
  tags$head(
    tags$meta(name = "viewport", content = "width=device-width, initial-scale=1"),
    tags$title("Compare bachelor programmes with UCR"),
    tags$style(HTML("
      @font-face { font-family:'IvyMode UCR'; src:url('https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/assets/fonts/IvyMode%20Regular.otf') format('opentype'); font-weight:400; font-display:swap; }
      @font-face { font-family:'Inter UCR'; src:url('https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/assets/fonts/Inter_Medium.ttf') format('truetype'); font-weight:400; font-display:swap; }
      @font-face { font-family:'Inter UCR'; src:url('https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/assets/fonts/Inter_Bold.ttf') format('truetype'); font-weight:700; font-display:swap; }
      :root{--plum:#491E34;--white:#F8F5EE;--black:#2E2D2D;--grey:#5C606B;--blue:#C8DFE6;--yellow:#FFE1A4}
      html,body{margin:0;background:var(--white);color:var(--black);font-family:'Inter UCR',Inter,Arial,sans-serif} body::before{content:'';display:block;height:24px;background:var(--plum)}
      .container-fluid{max-width:1500px;padding:0 28px 52px} h1,h2,h3{font-family:'IvyMode UCR',Georgia,serif;color:var(--plum);font-weight:400}
      .ucr-header{padding:24px 0 20px}.ucr-logo{width:auto;max-width:245px;max-height:68px}.hero{margin-bottom:22px}.hero h1{font-size:clamp(34px,3.2vw,50px);line-height:1.05;margin:0 0 12px;max-width:1050px}.hero p{color:var(--grey);font-size:17px;line-height:1.55;max-width:950px}
      .search-box{background:#fff;border:1px solid rgba(73,30,52,.16);border-radius:16px;padding:20px;margin-bottom:20px}.search-grid{display:grid;grid-template-columns:1fr 300px;gap:12px;align-items:end}.form-control{min-height:48px;border-radius:10px;border-color:rgba(73,30,52,.28);font-size:16px}.pilot-note{background:rgba(255,225,164,.45);border-radius:10px;padding:10px 13px;color:var(--grey);font-size:13px;margin-top:12px}
      .results-meta{color:var(--grey);margin:4px 0 12px}.results{display:grid;gap:10px}.result-card{display:flex;justify-content:space-between;align-items:center;gap:20px;background:#fff;border:1px solid rgba(73,30,52,.14);border-radius:14px;padding:17px 18px}.result-card h3{margin:0 0 4px;font-size:23px}.institution{margin:0;color:var(--grey)}.match-line{color:var(--grey);font-size:13px;margin-top:8px;line-height:1.4}.open-comparison{background:var(--plum);color:#fff;border:0;border-radius:9px;padding:11px 14px;font-weight:700;white-space:nowrap}.no-results{padding:26px;background:#fff;border-radius:14px;color:var(--grey)}
      .comparison-head{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;margin-bottom:18px}.comparison-head h1{margin:0 0 8px;font-size:clamp(31px,3vw,43px)}.comparison-head p{color:var(--grey);max-width:850px}.secondary-button{background:transparent!important;color:var(--plum)!important;border:1px solid rgba(73,30,52,.28)!important;border-radius:10px}
      .compare-scroll{overflow-x:auto;border:1px solid rgba(73,30,52,.14);border-radius:14px;background:#fff}.compare-table{border-collapse:separate;border-spacing:0;min-width:1120px;width:100%;table-layout:fixed}.compare-table th,.compare-table td{border-right:1px solid rgba(73,30,52,.1);border-bottom:1px solid rgba(73,30,52,.1);padding:13px 15px;vertical-align:top}.compare-table thead th{background:var(--plum);color:#fff;border-right-color:rgba(255,255,255,.18)}.programme-title{font-size:16px;font-weight:700}.programme-title a,.programme-source{color:inherit}.programme-source{display:inline-block;margin-top:5px;color:#fff;opacity:.82;font-size:12px}.block-row th{background:var(--blue);color:var(--plum);font-size:14px;font-weight:700}.comparison-cell{background:#fff;line-height:1.35}.comparison-cell.emphasis{background:rgba(255,225,164,.36)}.empty-cell{background:rgba(92,96,107,.035)}.ec-badge{display:inline-block;margin-top:6px;padding:2px 6px;border-radius:999px;background:rgba(73,30,52,.08);color:var(--grey);font-size:11px}.cell-note{color:var(--grey);font-size:12px;margin-top:5px}.transparency-note{margin-top:18px;background:#fff;border-left:5px solid var(--plum);padding:14px 17px;color:var(--grey);line-height:1.5}.transparency-note p{margin:5px 0 0}.cta-row{display:flex;justify-content:flex-end;margin-top:20px}.primary-cta{display:inline-block;background:var(--plum);color:#fff!important;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none!important}
      @media(max-width:900px){.container-fluid{padding:0 14px 40px}.search-grid{grid-template-columns:1fr}.result-card{display:block}.open-comparison{margin-top:13px}.comparison-head{display:block}.comparison-head .secondary-button{margin-top:10px}.ucr-logo{max-width:210px}}
    ")),
    tags$script(HTML("
      $(document).on('click', '.open-comparison', function(){
        Shiny.setInputValue('open_comparison', String($(this).data('id')), {priority:'event'});
      });
    "))
  ),
  uiOutput("app_body")
)

server <- function(input, output, session) {
  programmes <- reactiveVal(list())
  interests <- reactiveVal(list())
  selected <- reactiveVal(NULL)
  load_error <- reactiveVal(NULL)

  observe({
    tryCatch({
      p <- fetch_json(PROGRAMME_URL)$programmes %||% list()
      i <- fetch_json(INTEREST_URL)$interests %||% list()
      programmes(p)
      interests(i)
    }, error = function(e) {
      load_error("The counselor pilot data could not be loaded from GitHub.")
      message("Counselor pilot data error: ", conditionMessage(e))
    })
  })

  results <- reactive({
    search_programmes(programmes(), interests(), input$search_text %||% "", input$institution %||% "All")
  })

  output$app_body <- renderUI({
    record <- selected()
    if (!is.null(record)) return(render_comparison(record))
    render_search_shell()
  })

  output$institution_filter <- renderUI({
    p <- programmes()
    institutions <- sort(unique(vapply(p, function(x) safe_text(x$institution), character(1))))
    selectInput("institution", "Institution", choices = c("All", institutions), selected = input$institution %||% "All")
  })

  output$search_results <- renderUI({
    if (nzchar(safe_text(load_error()))) {
      return(div(class = "no-results", safe_text(load_error())))
    }
    found <- results()
    tagList(
      div(class = "results-meta", paste0(length(found), " programme", if (length(found) == 1) "" else "s", " found")),
      div(class = "results", render_result_cards(found))
    )
  })

  observeEvent(input$open_comparison, {
    example_id <- safe_text(input$open_comparison)
    if (!grepl("^[a-z0-9-]+$", example_id)) return()
    tryCatch({
      record <- fetch_json(paste0(EXAMPLE_BASE, "/", example_id, ".json"))
      record$origin <- "counselor"
      selected(record)
    }, error = function(e) {
      showModal(modalDialog(
        title = "Could not load comparison",
        "The selected comparison could not be loaded from GitHub.",
        easyClose = TRUE,
        footer = modalButton("Close")
      ))
      message("Counselor comparison load error: ", conditionMessage(e))
    })
  })

  observeEvent(input$back_to_search, selected(NULL))
}

shinyApp(ui, server)
