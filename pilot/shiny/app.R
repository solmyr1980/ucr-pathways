library(shiny)
library(jsonlite)

EXAMPLE_BASE <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/data/examples"
PILOT_DATA_BASE <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/pilot/shiny/data"
PROGRAM_BUILDER_URL <- "https://program.ucr.nl/"

cache_bust <- function(url) {
  separator <- if (grepl("\\?", url)) "&" else "?"
  paste0(url, separator, "cb=", as.integer(as.numeric(Sys.time()) * 1000))
}

fetch_json <- function(url) {
  fromJSON(cache_bust(url), simplifyVector = FALSE)
}

normalize_code <- function(x) {
  toupper(gsub("[^A-Z0-9]", "", trimws(x %||% "")))
}

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0 || identical(x, "")) y else x
}

find_example_id <- function(access_map, submitted_code) {
  target <- normalize_code(submitted_code)
  if (!nzchar(target)) return(NULL)
  for (entry in access_map$entries %||% list()) {
    if (identical(normalize_code(entry$code), target)) return(entry$example_id)
  }
  NULL
}

safe_text <- function(x) x %||% ""

cell_value <- function(cell) {
  if (is.null(cell)) return(NULL)
  if (is.character(cell)) return(list(text = cell))
  if (is.list(cell) && nzchar(safe_text(cell$text))) return(cell)
  NULL
}

render_compare_table <- function(pathway) {
  programmes <- pathway$programmes %||% list()
  blocks <- pathway$blocks %||% list()
  header_cells <- lapply(programmes, function(programme) {
    tags$th(
      div(class = "programme-title", safe_text(programme$label)),
      if (nzchar(safe_text(programme$subtitle))) div(class = "programme-subtitle", safe_text(programme$subtitle))
    )
  })
  body_rows <- list()
  for (block in blocks) {
    body_rows[[length(body_rows) + 1]] <- tags$tr(
      class = "block-row",
      tags$th(colspan = length(programmes), safe_text(block$title))
    )
    for (row in block$rows %||% list()) {
      row_cells <- lapply(programmes, function(programme) {
        value <- cell_value(row$cells[[programme$id]])
        if (is.null(value)) {
          tags$td(class = "empty-cell", "\u00A0")
        } else {
          tags$td(
            class = if (isTRUE(value$emphasis)) "comparison-cell emphasis" else "comparison-cell",
            div(class = "cell-text", safe_text(value$text)),
            if (nzchar(safe_text(value$note))) div(class = "cell-note", safe_text(value$note))
          )
        }
      })
      body_rows[[length(body_rows) + 1]] <- do.call(tags$tr, row_cells)
    }
  }
  div(
    class = "compare-scroll",
    tags$table(
      class = "compare-table",
      tags$thead(do.call(tags$tr, header_cells)),
      tags$tbody(do.call(tagList, body_rows))
    )
  )
}

course_button <- function(course) {
  code <- safe_text(course$code)
  tags$button(
    type = "button",
    class = "course-link",
    `data-code` = code,
    div(class = "course-name", safe_text(course$name)),
    div(class = "course-meta", paste0("Level ", safe_text(course$level)), if (nzchar(code)) paste0(" · ", code) else "")
  )
}

render_schedule <- function(programme) {
  semester_cards <- lapply(programme$schedule$semesters %||% list(), function(semester) {
    tags$section(
      class = "semester-card",
      tags$h4(safe_text(semester$label)),
      if (nzchar(safe_text(semester$term))) div(class = "semester-term", safe_text(semester$term)),
      div(class = "semester-courses", do.call(tagList, lapply(semester$courses %||% list(), course_button)))
    )
  })
  div(
    class = "schedule-programme",
    div(
      class = "schedule-header",
      tags$h3(safe_text(programme$label)),
      if (nzchar(safe_text(programme$subtitle))) tags$p(safe_text(programme$subtitle))
    ),
    div(class = "semester-grid", do.call(tagList, semester_cards))
  )
}

render_schedules <- function(pathway) {
  ucr_programmes <- Filter(function(programme) identical(programme$family, "ucr"), pathway$programmes %||% list())
  div(class = "schedules", do.call(tagList, lapply(ucr_programmes, render_schedule)))
}

render_pathway <- function(pathway) {
  reference <- pathway$referenceProgramme %||% list()
  source_url <- safe_text(reference$primarySourceUrl)
  reference_line <- safe_text(reference$provenance)
  fluidRow(
    column(
      width = 12,
      div(
        class = "pathway-shell",
        div(
          class = "topbar",
          div(
            div(class = "eyebrow", "UCR PATHWAYS"),
            tags$h1(safe_text(pathway$display$title %||% "See how your interests could take shape in a disciplinary degree and three progressively broader UCR pathways."))
          ),
          actionButton("reset_pathway", "Use another code", class = "secondary-button")
        ),
        div(
          class = "interest-card",
          div(class = "interest-label", paste0(safe_text(pathway$display$interestLabel %||% "Your interests"), ":")),
          div(class = "interest-text", safe_text(pathway$interests))
        ),
        if (nzchar(reference_line)) {
          div(
            class = "reference-line",
            if (nzchar(source_url)) tags$a(href = source_url, target = "_blank", rel = "noopener", paste0(reference_line, " ↗")) else reference_line
          )
        },
        tabsetPanel(
          id = "pathway_tab",
          type = "pills",
          tabPanel(
            "Compare programmes",
            div(class = "tab-copy", safe_text(pathway$display$comparisonNote)),
            render_compare_table(pathway)
          ),
          tabPanel(
            "Semester plans",
            div(class = "tab-copy", "Click or tap any UCR course to see its current description."),
            render_schedules(pathway)
          )
        ),
        div(
          class = "cta-row",
          tags$a(class = "primary-cta", href = PROGRAM_BUILDER_URL, target = "_blank", rel = "noopener", "Build your own UCR programme →")
        )
      )
    )
  )
}

ui <- fluidPage(
  tags$head(
    tags$meta(name = "viewport", content = "width=device-width, initial-scale=1"),
    tags$title("UCR Pathways — Shiny pilot"),
    tags$style(HTML("
      :root { --plum:#491E34; --white:#F8F5EE; --black:#2E2D2D; --grey:#5C606B; --lilac:#D0B7D0; --blue:#C8DFE6; --yellow:#FFE1A4; --green:#4A6857; }
      html, body { background:var(--white); color:var(--black); font-family:Inter, Arial, sans-serif; }
      body { padding-bottom:50px; }
      .container-fluid { max-width:1500px; padding:0 24px; }
      .access-shell { min-height:82vh; display:flex; align-items:center; justify-content:center; }
      .access-card { width:min(560px,100%); background:#fff; border:1px solid rgba(73,30,52,.16); border-radius:18px; padding:34px; box-shadow:0 18px 50px rgba(46,45,45,.08); }
      .eyebrow { letter-spacing:.14em; font-size:12px; font-weight:700; color:var(--plum); margin-bottom:10px; }
      h1,h2,h3,h4 { color:var(--plum); font-family:Georgia,'Times New Roman',serif; }
      .access-card h1 { font-size:36px; margin-top:0; margin-bottom:12px; }
      .access-card p { color:var(--grey); font-size:16px; line-height:1.55; }
      .form-control { border-radius:10px; min-height:48px; border-color:rgba(73,30,52,.28); font-size:17px; text-transform:uppercase; letter-spacing:.04em; }
      .btn-primary,.primary-button { background:var(--plum)!important; border-color:var(--plum)!important; border-radius:10px; min-height:44px; padding:10px 18px; }
      .secondary-button { background:transparent!important; color:var(--plum)!important; border:1px solid rgba(73,30,52,.28)!important; border-radius:10px; }
      .access-error { margin-top:14px; color:#8b1e2d; font-weight:600; }
      .pathway-shell { padding-top:28px; }
      .topbar { display:flex; justify-content:space-between; align-items:flex-start; gap:24px; margin-bottom:20px; }
      .topbar h1 { max-width:1050px; margin:0; font-size:clamp(30px,4vw,52px); line-height:1.07; }
      .interest-card { background:var(--plum); color:#fff; border-radius:15px; padding:18px 22px; display:grid; grid-template-columns:auto 1fr; gap:14px; align-items:baseline; margin-bottom:12px; }
      .interest-label { font-weight:700; opacity:.8; }
      .interest-text { font-size:18px; line-height:1.45; }
      .reference-line { margin:10px 2px 24px; color:var(--grey); font-size:14px; }
      .reference-line a { color:var(--plum); text-decoration:underline; }
      .nav-pills { margin-bottom:20px; }
      .nav-pills>li>a { color:var(--plum); border-radius:9px; font-weight:600; }
      .nav-pills>li.active>a,.nav-pills>li.active>a:hover,.nav-pills>li.active>a:focus { background:var(--plum); }
      .tab-copy { color:var(--grey); margin:2px 0 16px; max-width:900px; }
      .compare-scroll { overflow-x:auto; border:1px solid rgba(73,30,52,.14); border-radius:14px; background:#fff; }
      .compare-table { border-collapse:separate; border-spacing:0; min-width:1050px; width:100%; table-layout:fixed; }
      .compare-table th,.compare-table td { border-right:1px solid rgba(73,30,52,.1); border-bottom:1px solid rgba(73,30,52,.1); padding:13px 15px; vertical-align:top; }
      .compare-table thead th { background:var(--plum); color:#fff; border-right-color:rgba(255,255,255,.18); }
      .programme-title { font-size:16px; font-weight:700; }
      .programme-subtitle { font-size:12px; opacity:.78; margin-top:4px; font-weight:400; }
      .block-row th { background:var(--blue); color:var(--plum); font-size:14px; letter-spacing:.02em; padding-top:10px; padding-bottom:10px; }
      .comparison-cell { background:#fff; line-height:1.35; }
      .comparison-cell.emphasis { background:rgba(255,225,164,.36); }
      .empty-cell { background:rgba(92,96,107,.035); }
      .cell-note { color:var(--grey); font-size:12px; margin-top:5px; }
      .schedule-programme { margin:0 0 34px; }
      .schedule-header { border-left:6px solid var(--plum); padding:2px 0 2px 14px; margin-bottom:14px; }
      .schedule-header h3 { margin:0 0 3px; font-size:27px; }
      .schedule-header p { margin:0; color:var(--grey); }
      .semester-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; }
      .semester-card { background:#fff; border:1px solid rgba(73,30,52,.14); border-radius:14px; padding:16px; }
      .semester-card h4 { margin:0 0 2px; font-size:18px; }
      .semester-term { color:var(--grey); font-size:12px; margin-bottom:11px; }
      .semester-courses { display:grid; gap:8px; }
      .course-link { width:100%; text-align:left; background:rgba(200,223,230,.32); border:1px solid rgba(73,30,52,.10); border-radius:9px; padding:10px 11px; cursor:pointer; transition:transform .08s ease,background .12s ease; }
      .course-link:hover,.course-link:focus { background:rgba(208,183,208,.35); transform:translateY(-1px); outline:none; }
      .course-name { color:var(--black); font-weight:650; line-height:1.25; }
      .course-meta { color:var(--grey); font-size:11px; margin-top:3px; }
      .cta-row { display:flex; justify-content:flex-end; margin-top:26px; }
      .primary-cta { display:inline-block; background:var(--plum); color:#fff!important; padding:12px 18px; border-radius:10px; font-weight:700; text-decoration:none!important; }
      .modal-content { border-radius:14px; }
      .modal-title { color:var(--plum); font-family:Georgia,'Times New Roman',serif; }
      .course-description { font-size:15px; line-height:1.6; }
      @media (max-width:980px) { .container-fluid{padding:0 14px;} .topbar{display:block;} .topbar .secondary-button{margin-top:14px;} .interest-card{grid-template-columns:1fr;gap:4px;} .semester-grid{grid-template-columns:1fr;} .access-card{padding:26px 22px;} .access-card h1{font-size:31px;} }
    ")),
    tags$script(HTML("
      $(document).on('click', '.course-link', function() {
        const code = $(this).data('code');
        if (code) Shiny.setInputValue('course_click', String(code), {priority:'event'});
      });
    "))
  ),
  uiOutput("app_body")
)

server <- function(input, output, session) {
  pathway <- reactiveVal(NULL)
  course_cache <- reactiveValues()
  access_error <- reactiveVal(NULL)

  output$app_body <- renderUI({
    current <- pathway()
    if (is.null(current)) {
      return(div(
        class = "access-shell",
        div(
          class = "access-card",
          div(class = "eyebrow", "UCR PATHWAYS"),
          tags$h1("Your pathway"),
          tags$p("Enter the code you received to open your personalised UCR Pathways comparison."),
          textInput("access_code", label = NULL, placeholder = "UCR-XXXX-XXXX-XXXX-XXXX"),
          actionButton("unlock_pathway", "Open my pathway", class = "btn-primary"),
          uiOutput("access_error_ui")
        )
      ))
    }
    render_pathway(current)
  })

  output$access_error_ui <- renderUI({
    if (!nzchar(safe_text(access_error()))) return(NULL)
    div(class = "access-error", safe_text(access_error()))
  })

  observeEvent(input$unlock_pathway, {
    access_error(NULL)
    tryCatch({
      access_map <- fetch_json(paste0(PILOT_DATA_BASE, "/access_codes.json"))
      example_id <- find_example_id(access_map, input$access_code)
      if (is.null(example_id)) {
        access_error("That code was not recognised. Check it and try again.")
        return()
      }
      selected_pathway <- fetch_json(paste0(EXAMPLE_BASE, "/", example_id, ".json"))
      pathway(selected_pathway)
    }, error = function(e) {
      access_error("The pathway data could not be loaded from GitHub. Check your internet connection and try again.")
      message("UCR Pathways pilot load error: ", conditionMessage(e))
    })
  })

  observeEvent(input$reset_pathway, {
    pathway(NULL)
    access_error(NULL)
  })

  observeEvent(input$course_click, {
    code <- safe_text(input$course_click)
    department <- substr(code, 1, 3)
    tryCatch({
      if (is.null(course_cache[[department]])) {
        course_cache[[department]] <- fetch_json(paste0(PILOT_DATA_BASE, "/courses/", department, ".json"))
      }
      description <- course_cache[[department]]$descriptions[[code]]
      if (is.null(description) || !nzchar(safe_text(description))) {
        showModal(modalDialog(title = code, "No course description was found in the current pilot course lookup.", easyClose = TRUE, footer = modalButton("Close")))
        return()
      }
      showModal(modalDialog(title = code, div(class = "course-description", safe_text(description)), easyClose = TRUE, footer = modalButton("Close")))
    }, error = function(e) {
      showModal(modalDialog(title = code, "The course description could not be loaded from GitHub.", easyClose = TRUE, footer = modalButton("Close")))
      message("UCR Pathways pilot course load error: ", conditionMessage(e))
    })
  })
}

shinyApp(ui, server)
