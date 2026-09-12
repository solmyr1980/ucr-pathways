library(shiny)
library(jsonlite)

# Run from the repository root or the app directory; keep brand assets local.
root_candidates <- c(getwd(), file.path(getwd(), ".."), file.path(getwd(), "../.."))
REPO_ROOT <- root_candidates[file.exists(file.path(root_candidates, "assets/css/brand.css"))][1]
if (is.na(REPO_ROOT)) stop("Run this pilot from a complete ucr-pathways repository checkout.")
REPO_ROOT <- normalizePath(REPO_ROOT)
source(file.path(REPO_ROOT, "pilot/shared.R"), local = TRUE)

EXAMPLE_BASE <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/data/examples"
PILOT_DATA_BASE <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/pilot/shiny/data"
ASSET_BASE <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/assets"
UCR_LOGO_URL <- "ucr-assets/brand/ucr-primary-plum.png"
UCR_WEBSITE_URL <- "https://ucr.nl/"
UCR_COURSES_URL <- "https://ucr.nl/education/courses/"
ADMISSIONS_URL <- "https://ucr.nl/about-ucr/connect/meet-with-admissions/"
PROGRAM_BUILDER_URL <- "https://program.ucr.nl/"
DISCLAIMER_PLACEHOLDER <- "[PLACEHOLDER — insert approved student-program disclaimer from the printed butterfly.]"
UCR_COURSE_EC <- 7.5

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0 || identical(x, "")) y else x
}

cache_bust <- function(url) {
  separator <- if (grepl("\\?", url)) "&" else "?"
  paste0(url, separator, "cb=", sprintf("%.0f", as.numeric(Sys.time()) * 1000))
}

fetch_json <- function(url) {
  if (identical(Sys.getenv("UCR_PILOT_LOCAL_DATA"), "true")) {
    prefix <- "https://raw.githubusercontent.com/solmyr1980/ucr-pathways/main/"
    if (startsWith(url, prefix)) return(fromJSON(file.path(REPO_ROOT, substring(url, nchar(prefix) + 1)), simplifyVector = FALSE))
  }
  fromJSON(cache_bust(url), simplifyVector = FALSE)
}

normalize_code <- function(x) {
  gsub("[^A-Z0-9]", "", toupper(trimws(x %||% "")))
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

comparator_meta <- function(record) {
  record$comparator %||% record$referenceProgramme %||% list()
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

brand_header <- function() {
  div(
    class = "ucr-header",
    tags$a(
      href = UCR_WEBSITE_URL,
      target = "_blank",
      rel = "noopener",
      `aria-label` = "University College Roosevelt website",
      tags$img(src = UCR_LOGO_URL, class = "ucr-logo", alt = "University College Roosevelt")
    )
  )
}

render_compare_table <- function(record) {
  programmes <- record$programmes %||% list()
  blocks <- record$blocks %||% list()
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

  body_rows <- list()
  for (block in blocks) {
    body_rows[[length(body_rows) + 1]] <- tags$tr(
      class = "block-row",
      tags$th(colspan = length(programmes), safe_text(block$title))
    )

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
      body_rows[[length(body_rows) + 1]] <- do.call(tags$tr, cells)
    }
  }

  div(
    class = "compare-scroll",
    tags$table(
      class = "compare-table",
      tags$thead(do.call(tags$tr, headers)),
      tags$tbody(do.call(tagList, body_rows))
    )
  )
}

course_button <- function(course) {
  code <- safe_text(course$code)
  ec <- credit_text(course$credits, UCR_COURSE_EC)
  tags$button(
    type = "button",
    class = "course-link",
    `data-code` = code,
    `data-name` = safe_text(course$name),
    div(class = "course-name", safe_text(course$name)),
    div(class = "course-meta", paste(c(course_level(course$level), ec, if (nzchar(code)) code else NULL), collapse = " · "))
  )
}

render_schedule <- function(record, programme) {
  cards <- lapply(programme$schedule$semesters %||% list(), function(semester) {
    tags$section(
      class = "semester-card",
      tags$h4(safe_text(semester$label)),
      if (nzchar(safe_text(semester$term))) div(class = "semester-term", safe_text(semester$term)),
      div(class = "semester-courses", do.call(tagList, lapply(semester$courses %||% list(), course_button)))
    )
  })

  div(
    class = "programme-view",
    div(
      class = "programme-view-heading",
      tags$h2(visible_label(record, programme)),
      tags$a(href = UCR_COURSES_URL, target = "_blank", rel = "noopener", "View UCR courses ↗")
    ),
    div(class = "semester-grid", do.call(tagList, cards)),
    div(class = "disclaimer", tags$strong("Temporary disclaimer placeholder"), tags$p(DISCLAIMER_PLACEHOLDER))
  )
}

student_ucr_programmes <- function(record) {
  roles <- c("ucr-depth", "ucr-balanced", "ucr-thematic")
  programmes <- record$programmes %||% list()
  ordered <- lapply(roles, function(role) {
    matches <- Filter(function(p) identical(p$role, role), programmes)
    if (length(matches)) matches[[1]] else NULL
  })
  Filter(Negate(is.null), ordered)
}

render_programme_options <- function(record) {
  programmes <- student_ucr_programmes(record)
  if (!length(programmes)) return(div(class = "load-error", "No personalized UCR programme options are available in this record."))

  option_tabs <- lapply(programmes, function(programme) {
    tabPanel(visible_label(record, programme), render_schedule(record, programme))
  })

  div(
    class = "programme-options",
    tags$p(class = "tab-copy", "Choose an option below to inspect its complete six-semester programme."),
    do.call(tabsetPanel, c(list(id = "programme_option", type = "tabs"), option_tabs))
  )
}

render_student_record <- function(record) {
  interpretation <- safe_text(record$interestInterpretation)

  fluidRow(
    column(
      width = 12,
      div(
        class = "app-shell",
        brand_header(),
        div(
          class = "intro-row",
          div(
            tags$h1("We are happy to share your personalized programme options."),
            tags$p(class = "lede", "Explore three possible UCR programmes built around your interests, then see how they compare with another Dutch bachelor.")
          ),
          actionButton("reset_pathway", "Use another code", class = "secondary-button")
        ),
        div(
          class = "input-summary",
          div(
            class = "summary-panel",
            tags$h3("You told us that…"),
            tags$p(safe_text(record$interests))
          ),
          div(
            class = "summary-panel interpretation",
            tags$h3("For us, this means that…"),
            if (nzchar(interpretation)) tags$p(interpretation) else tags$p(class = "pilot-placeholder", "[Academic interpretation will be stored here for production student records.]")
          )
        ),
        tabsetPanel(
          id = "student_view",
          type = "pills",
          tabPanel(
            "View my personalized programme options",
            render_programme_options(record)
          ),
          tabPanel(
            "See how these options compare",
            tags$p(class = "tab-copy", "This comparison shows another Dutch bachelor alongside your three UCR programme options, from the closest match to broader ways of combining relevant subjects."),
            render_compare_table(record),
            render_comparison_notes(record),
            tags$p(class = "source-note", "Blank cells indicate that no sufficiently comparable named component is shown in that position. These are illustrative UCR programmes, not official tracks or guaranteed future schedules.")
          )
        ),
        div(
          class = "next-step",
          tags$h2("Would you like to find out more?"),
          div(
            class = "cta-row",
            tags$a(class = "secondary-cta", href = ADMISSIONS_URL, target = "_blank", rel = "noopener", "Speak to Admissions ↗"),
            tags$a(class = "primary-cta", href = PROGRAM_BUILDER_URL, target = "_blank", rel = "noopener", "Tweak this programme to your liking ↗")
          )
        )
      )
    )
  )
}

ui <- fluidPage(
  tags$head(
    tags$meta(name = "viewport", content = "width=device-width, initial-scale=1"),
    tags$title("Your personalized UCR programme options"),
    tags$style(HTML("
      html, body { margin:0; background:var(--white); color:var(--black); font-family:Inter,Arial,sans-serif; }
      body::before { content:''; display:block; height:24px; background:var(--plum); }
      .container-fluid { max-width:1500px; padding:0 28px 52px; }
      h1,h2,h3,h4 { color:var(--plum); font-family:IvyMode,Georgia,serif; font-weight:400; }
      .ucr-header { padding:24px 0 20px; }
      .ucr-logo { width:auto; max-width:245px; max-height:68px; object-fit:contain; }
      .access-shell { min-height:75vh; display:flex; align-items:center; justify-content:center; }
      .access-card { width:min(600px,100%); background:#fff; border:1px solid rgba(73,30,52,.14); border-radius:18px; padding:34px; box-shadow:0 18px 50px rgba(46,45,45,.08); }
      .access-card h1 { font-size:38px; margin:0 0 12px; }
      .access-card p,.lede,.tab-copy { color:var(--grey); line-height:1.55; }
      .form-control { min-height:48px; border-radius:10px; border-color:rgba(73,30,52,.28); font-size:17px; text-transform:uppercase; }
      .btn-primary,.primary-button { background:var(--plum)!important; border-color:var(--plum)!important; border-radius:10px; min-height:44px; font-weight:700; }
      .secondary-button { background:transparent!important; color:var(--plum)!important; border:1px solid rgba(73,30,52,.28)!important; border-radius:10px; }
      .access-error,.load-error { margin-top:14px; color:#8b1e2d; font-weight:700; }
      .intro-row { display:flex; align-items:flex-start; justify-content:space-between; gap:28px; margin-bottom:18px; }
      .intro-row h1 { margin:0; font-size:clamp(32px,3vw,46px); line-height:1.08; max-width:930px; }
      .lede { max-width:850px; font-size:16px; }
      .input-summary { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:18px 0 24px; }
      .summary-panel { background:var(--plum); color:#fff; border-radius:15px; padding:20px; min-height:126px; }
      .summary-panel.interpretation { background:#fff; color:var(--black); border:1px solid rgba(73,30,52,.16); }
      .summary-panel h3 { color:inherit; margin:0 0 9px; font-size:21px; }
      .summary-panel p { margin:0; line-height:1.5; font-size:17px; }
      .pilot-placeholder { color:var(--grey); font-style:italic; }
      .nav-pills { margin-bottom:20px; }
      .nav-pills>li>a { color:var(--plum); border-radius:9px; font-weight:700; }
      .nav-pills>li.active>a,.nav-pills>li.active>a:hover,.nav-pills>li.active>a:focus { background:var(--plum); }
      .programme-options .nav-tabs { margin-bottom:18px; }
      .programme-options .nav-tabs>li>a { color:var(--plum); font-weight:700; }
      .programme-view-heading { display:flex; align-items:baseline; justify-content:space-between; gap:18px; border-left:6px solid var(--plum); padding:3px 0 3px 15px; margin-bottom:15px; }
      .programme-view-heading h2 { margin:0; font-size:29px; }
      .programme-view-heading a,.programme-source { color:var(--plum); text-decoration:underline; font-size:12px; }
      .semester-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; }
      .semester-card { background:#fff; border:1px solid rgba(73,30,52,.14); border-radius:14px; padding:16px; }
      .semester-card h4 { margin:0 0 3px; font-size:19px; }
      .semester-term { color:var(--grey); font-size:12px; margin-bottom:10px; }
      .semester-courses { display:grid; gap:8px; }
      .course-link { width:100%; text-align:left; background:rgba(200,223,230,.34); border:1px solid rgba(73,30,52,.10); border-radius:9px; padding:10px 11px; cursor:pointer; }
      .course-name { font-weight:700; line-height:1.25; }
      .course-meta { color:var(--grey); font-size:11px; margin-top:4px; }
      .disclaimer { margin:18px 0 26px; padding:13px 15px; border:1px dashed rgba(139,30,45,.55); background:#fff; color:#8b1e2d; border-radius:10px; font-size:13px; }
      .disclaimer p { margin:5px 0 0; }
      .compare-scroll { overflow-x:auto; border:1px solid rgba(73,30,52,.14); border-radius:14px; background:#fff; }
      .compare-table { border-collapse:separate; border-spacing:0; min-width:1120px; width:100%; table-layout:fixed; }
      .compare-table th,.compare-table td { border-right:1px solid rgba(73,30,52,.1); border-bottom:1px solid rgba(73,30,52,.1); padding:13px 15px; vertical-align:top; }
      .compare-table thead th { background:var(--plum); color:#fff; border-right-color:rgba(255,255,255,.18); }
      .programme-title { font-size:16px; font-weight:700; }
      .programme-title a,.programme-source { color:inherit; }
      .programme-source { display:inline-block; margin-top:5px; color:#fff; opacity:.82; }
      .block-row th { background:var(--blue); color:var(--plum); font-size:14px; font-weight:700; }
      .comparison-cell { background:#fff; line-height:1.35; }
      .comparison-cell.emphasis { background:rgba(255,225,164,.36); }
      .empty-cell { background:rgba(92,96,107,.035); }
      .ec-badge { display:inline-block; margin-top:6px; padding:2px 6px; border-radius:999px; background:rgba(73,30,52,.08); color:var(--grey); font-size:11px; }
      .cell-note { color:var(--grey); font-size:12px; margin-top:5px; }
      .next-step { margin-top:34px; border-top:1px solid rgba(73,30,52,.18); padding-top:22px; }
      .next-step h2 { margin-top:0; }
      .cta-row { display:flex; flex-wrap:wrap; gap:12px; }
      .primary-cta,.secondary-cta { display:inline-block; padding:12px 18px; border-radius:10px; font-weight:700; text-decoration:none!important; }
      .primary-cta { background:var(--plum); color:#fff!important; }
      .secondary-cta { color:var(--plum)!important; border:1px solid rgba(73,30,52,.3); background:#fff; }
      .modal-content { border-radius:14px; }
      .modal-title { color:var(--plum); font-family:IvyMode,Georgia,serif; }
      .course-description { font-size:15px; line-height:1.6; }
      @media(max-width:980px){ .container-fluid{padding:0 14px 40px}.intro-row{display:block}.intro-row .secondary-button{margin-top:12px}.input-summary{grid-template-columns:1fr}.semester-grid{grid-template-columns:1fr}.programme-view-heading{display:block}.programme-view-heading a{display:inline-block;margin-top:7px}.ucr-logo{max-width:210px}.access-card{padding:26px 22px} }
    ")),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/brand.css"),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/shiny.css"),
    tags$script(HTML("
      $(document).on('click', '.course-link', function() {
        const code = $(this).data('code');
        const name = $(this).data('name');
        if (code) Shiny.setInputValue('course_click', {code:String(code), name:String(name||'')}, {priority:'event'});
      });
    "))
  ),
  uiOutput("app_body")
)

server <- function(input, output, session) {
  record <- reactiveVal(NULL)
  course_cache <- reactiveValues()
  access_error <- reactiveVal(NULL)

  output$app_body <- renderUI({
    current <- record()
    if (is.null(current)) {
      return(div(
        class = "access-shell",
        div(
          class = "access-card",
          brand_header(),
          tags$h1("Your personalized programme options"),
          tags$p("Enter the code you received to open the three UCR programme options prepared around your interests."),
          textInput("access_code", label = "Your access code", placeholder = "UCR-XXXX-XXXX-XXXX-XXXX"),
          actionButton("unlock_pathway", "Open my programme options", class = "btn-primary"),
          uiOutput("access_error_ui")
        )
      ))
    }
    render_student_record(current)
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
      selected <- fetch_json(paste0(EXAMPLE_BASE, "/", example_id, ".json"))
      if (is.null(selected$origin)) selected$origin <- "student"
      record(selected)
    }, error = function(e) {
      access_error("The programme data could not be loaded. Check your internet connection and try again.")
      message("Student pilot load error: ", conditionMessage(e))
    })
  })

  observeEvent(input$reset_pathway, {
    record(NULL)
    access_error(NULL)
  })

  observeEvent(input$course_click, {
    code <- safe_text(input$course_click$code)
    course_name <- safe_text(input$course_click$name)
    department <- substr(code, 1, 3)
    tryCatch({
      if (is.null(course_cache[[department]])) {
        course_cache[[department]] <- fetch_json(paste0(PILOT_DATA_BASE, "/courses/", department, ".json"))
      }
      description <- course_cache[[department]]$descriptions[[code]]
      if (is.null(description) || !nzchar(safe_text(description))) {
        showModal(modalDialog(title = if (nzchar(course_name)) course_name else code, "No course description was found in the current pilot course lookup.", easyClose = TRUE, footer = modalButton("Close")))
        return()
      }
      showModal(modalDialog(title = if (nzchar(course_name)) course_name else code, div(class = "course-description", safe_text(description)), easyClose = TRUE, footer = modalButton("Close")))
    }, error = function(e) {
      showModal(modalDialog(title = if (nzchar(course_name)) course_name else code, "The course description could not be loaded.", easyClose = TRUE, footer = modalButton("Close")))
      message("Student pilot course load error: ", conditionMessage(e))
    })
  })
}

shinyApp(ui, server)