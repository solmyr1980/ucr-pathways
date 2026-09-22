library(shiny)
library(jsonlite)

# Run from the repository root or the app directory; keep brand assets local.
root_candidates <- c(getwd(), file.path(getwd(), ".."), file.path(getwd(), "../.."))
REPO_ROOT <- root_candidates[file.exists(file.path(root_candidates, "assets/css/brand.css"))][1]
if (is.na(REPO_ROOT)) stop("Run this pilot from a complete ucr-pathways repository checkout.")
REPO_ROOT <- normalizePath(REPO_ROOT)
source(file.path(REPO_ROOT, "pilot/shared.R"), local = TRUE)

UCR_LOGO_URL <- "ucr-assets/brand/ucr-primary-plum.png"
UCR_WEBSITE_URL <- "https://ucr.nl/?utm_source=shinyapps&utm_medium=landing_page&utm_campaign=your_curriculum&utm_content=logo"
UCR_COURSES_URL <- "https://ucr.nl/education/courses/"
ADMISSIONS_URL <- "https://ucr.nl/about-ucr/connect/meet-with-admissions/?utm_source=shinyapps&utm_medium=landing_page&utm_campaign=your_curriculum&utm_content=button_admissions"
PROGRAM_BUILDER_URL <- "https://program.ucr.nl/?utm_source=shinyapps&utm_medium=landing_page&utm_campaign=your_curriculum&utm_content=button_program_builder"
STUDENT_DISCLAIMER <- paste(
  "We’ve done our best to make sure this program is as complete and accurate a match to your interests as possible.",
  "But since our curriculum is as flexible and responsive as our students, things may change after you read this.",
  "By the time you start building your program online (or in Middelburg), some courses may have shifted, been added, or taken a well-deserved break.",
  "In short: things change and no rights may be derived from this document."
)
COURSE_DESCRIPTION_UNAVAILABLE <- "A course description is not currently available."
UCR_COURSE_EC <- 7.5

`%||%` <- function(x, y) {
  if (is.null(x) || length(x) == 0 || identical(x, "")) y else x
}

source(file.path(REPO_ROOT, "pilot/shiny/student-data.R"), local = TRUE)
STUDENT_DATA_CONFIG <- load_student_data_config(REPO_ROOT)

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

cta_buttons <- function(location_class) {
  div(
    class = paste("cta-row", location_class),
    tags$a(class = "secondary-cta", href = ADMISSIONS_URL, target = "_blank", rel = "noopener", "Speak to Admissions ↗"),
    tags$a(class = "primary-cta", href = PROGRAM_BUILDER_URL, target = "_blank", rel = "noopener", "Build your own UCR program ↗")
  )
}

render_compare_table <- function(record) {
  programmes <- record$programmes %||% list()
  blocks <- record$blocks %||% list()
  meta <- comparator_meta(record)

  headers <- lapply(programmes, function(programme) {
    label <- visible_label(record, programme)
    if (is_comparator_programme(programme) && nzchar(safe_text(meta$primarySourceUrl))) {
      title <- tags$a(href = meta$primarySourceUrl, target = "_blank", rel = "noopener", paste0(label, " ↗"))
    } else {
      title <- label
    }
    tags$th(
      div(class = "programme-title", title),
      if (is_ucr_programme(programme)) {
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
        ec <- credit_text(value$credits, if (is_ucr_programme(programme)) UCR_COURSE_EC else NULL)
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
    class = "compare-scroll desktop-comparison",
    tags$table(
      class = "compare-table",
      tags$thead(do.call(tags$tr, headers)),
      tags$tbody(do.call(tagList, body_rows))
    )
  )
}

render_mobile_comparison <- function(record) {
  programmes <- record$programmes %||% list()
  blocks <- record$blocks %||% list()
  meta <- comparator_meta(record)

  cards <- lapply(seq_along(programmes), function(index) {
    programme <- programmes[[index]]
    label <- visible_label(record, programme)
    source_url <- if (is_comparator_programme(programme)) safe_text(meta$primarySourceUrl) else UCR_COURSES_URL
    source_label <- if (is_comparator_programme(programme)) "Official program ↗" else "UCR courses ↗"

    sections <- lapply(blocks, function(block) {
      items <- Filter(Negate(is.null), lapply(block$rows %||% list(), function(row) {
        value <- cell_value(row$cells[[programme$id]])
        if (is.null(value)) return(NULL)
        ec <- credit_text(value$credits, if (is_ucr_programme(programme)) UCR_COURSE_EC else NULL)
        tags$li(
          class = if (isTRUE(value$emphasis)) "mobile-comparison-item emphasis" else "mobile-comparison-item",
          div(class = "cell-text", safe_text(value$text)),
          if (nzchar(ec)) div(class = "ec-badge", ec),
          if (nzchar(safe_text(value$note))) div(class = "cell-note", safe_text(value$note))
        )
      }))
      if (!length(items)) return(NULL)
      tags$section(
        class = "mobile-comparison-section",
        tags$h3(safe_text(block$title)),
        tags$ul(do.call(tagList, items))
      )
    })

    tags$article(
      class = paste(c(
        "mobile-comparison-card",
        if (is_comparator_programme(programme)) "comparator" else NULL,
        if (index == 1) "active" else NULL
      ), collapse = " "),
      `data-comparison-index` = index - 1,
      hidden = if (index != 1) "hidden" else NULL,
      div(
        class = "mobile-comparison-header",
        tags$h2(label),
        if (nzchar(source_url)) tags$a(href = source_url, target = "_blank", rel = "noopener", source_label)
      ),
      do.call(tagList, sections)
    )
  })

  dots <- lapply(seq_along(programmes), function(index) {
    tags$button(
      type = "button",
      class = paste(c("mobile-comparison-dot", if (index == 1) "active" else NULL), collapse = " "),
      `data-comparison-dot` = index - 1,
      `aria-label` = paste("Program", index, visible_label(record, programmes[[index]])),
      `aria-current` = if (index == 1) "true" else "false"
    )
  })

  div(
    class = "mobile-comparison",
    `data-comparison-count` = length(programmes),
    tabindex = "0",
    `aria-label` = "Program comparison carousel",
    div(
      class = "mobile-comparison-nav",
      tags$button(type = "button", class = "mobile-comparison-button previous", `aria-label` = "Previous program", disabled = "disabled", "←"),
      div(
        class = "mobile-comparison-position",
        div(class = "mobile-comparison-position-title", paste("1 of", length(programmes))),
        div(class = "mobile-comparison-dots", do.call(tagList, dots))
      ),
      tags$button(type = "button", class = "mobile-comparison-button next", `aria-label` = "Next program", disabled = if (length(programmes) == 1) "disabled" else NULL, "→")
    ),
    div(class = "mobile-comparison-cards", do.call(tagList, cards)),
    tags$p(class = "mobile-comparison-hint", "Swipe horizontally to view each program.")
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

render_schedule <- function(record, programme, show_return = FALSE) {
  rationale <- alternative_rationale_for(record, programme$id)
  concept <- if (is.null(rationale)) "" else safe_text(rationale$concept)
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
    if (nzchar(concept)) tags$p(class = "programme-concept", concept),
    div(class = "semester-grid", do.call(tagList, cards)),
    div(class = "disclaimer", tags$p(STUDENT_DISCLAIMER)),
    if (show_return) tags$a(
      href = "#programme-selection",
      class = "program-selection-return secondary-button",
      `data-return-to-programs` = "true",
      "Back to program selection ↑"
    )
  )
}

student_ucr_programmes <- function(record) {
  Filter(is_ucr_programme, record$programmes %||% list())
}

render_programme_options <- function(record) {
  programmes <- student_ucr_programmes(record)
  if (!length(programmes)) return(div(class = "load-error", "No UCR programs are available."))

  option_tabs <- lapply(programmes, function(programme) {
    tabPanel(visible_label(record, programme), render_schedule(record, programme, show_return = length(programmes) > 1))
  })

  div(
    id = "programme-selection",
    class = "programme-options",
    tags$p(
      class = "tab-copy",
      if (length(programmes) == 1) {
        "Explore the complete six-semester program below. Click any course to view its description."
      } else {
        "Choose a program below to explore its complete six-semester plan. Click any course to view its description."
      }
    ),
    do.call(tabsetPanel, c(list(id = "programme_option", type = "tabs"), option_tabs))
  )
}

student_experience_copy <- function(record) {
  programmes <- student_ucr_programmes(record)
  count <- length(programmes)
  comparator <- Filter(is_comparator_programme, record$programmes %||% list())
  comparator_label <- if (length(comparator)) {
    visible_label(record, comparator[[1]])
  } else {
    "a relevant bachelor elsewhere in the Netherlands"
  }

  if (count == 1) {
    return(list(
      lede = paste0(
        "We interpreted your interests in academic terms. Explore the complete program semester by semester, ",
        "or compare it with ", comparator_label, "."
      ),
      programme_tab = "Explore my UCR program",
      comparison_intro = paste0(
        "This view compares your UCR program with ", comparator_label,
        ". It shows where the curricula overlap and where they differ."
      ),
      source_note = paste0(
        "A blank cell means there is no closely comparable course or component in that row. ",
        "This UCR program shows one possible way of studying at UCR; it is not an official track or guaranteed future schedule."
      )
    ))
  }

  list(
    lede = paste0(
      "We interpreted your interests in academic terms. Explore each complete program semester by semester, ",
      "or compare the programs with ", comparator_label, "."
    ),
    programme_tab = "Explore my UCR programs",
    comparison_intro = paste0(
      "This view compares your UCR programs with ", comparator_label,
      ". It shows where the curricula overlap and where they differ."
    ),
    source_note = paste0(
      "A blank cell means there is no closely comparable course or component in that row. ",
      "These UCR programs show possible ways of studying at UCR; they are not official tracks or guaranteed future schedules."
    )
  )
}

render_student_record <- function(record) {
  interpretation <- safe_text(record$interestInterpretation)
  copy <- student_experience_copy(record)

  fluidRow(
    column(
      width = 12,
      div(
        class = "app-shell",
        brand_header(),
        div(
          class = "top-actions",
          cta_buttons("desktop-cta"),
          actionButton("reset_pathway", "Use another code", class = "secondary-button")
        ),
        tags$p(class = "lede intro-lede", copy$lede),
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
            if (nzchar(interpretation)) tags$p(interpretation) else tags$p(class = "missing-copy", "An academic interpretation is not currently available.")
          )
        ),
        tabsetPanel(
          id = "student_view",
          type = "pills",
          tabPanel(
            copy$programme_tab,
            render_programme_options(record)
          ),
          tabPanel(
            "Compare with a Dutch bachelor",
            tags$p(class = "tab-copy", copy$comparison_intro),
            render_compare_table(record),
            render_mobile_comparison(record),
            render_comparison_notes(record),
            tags$p(class = "source-note", copy$source_note)
          )
        ),
        cta_buttons("mobile-cta")
      )
    )
  )
}

ui <- fluidPage(
  tags$head(
    tags$meta(name = "viewport", content = "width=device-width, initial-scale=1"),
    tags$title("Your UCR study possibilities"),
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
      .top-actions { display:flex; align-items:center; justify-content:space-between; gap:28px; margin-bottom:14px; }
      .lede { max-width:850px; font-size:16px; }
      .intro-lede { margin:0 0 18px; }
      .input-summary { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:18px 0 24px; }
      .summary-panel { background:var(--plum); color:#fff; border-radius:15px; padding:20px; min-height:126px; }
      .summary-panel.interpretation { background:#fff; color:var(--black); border:1px solid rgba(73,30,52,.16); }
      .summary-panel h3 { color:inherit; margin:0 0 9px; font-size:21px; }
      .summary-panel p { margin:0; line-height:1.5; font-size:17px; }
      .missing-copy { color:var(--grey); font-style:italic; }
      .nav-pills { margin-bottom:20px; }
      .nav-pills>li>a { color:var(--plum); border-radius:9px; font-weight:700; }
      .nav-pills>li.active>a,.nav-pills>li.active>a:hover,.nav-pills>li.active>a:focus { background:var(--plum); }
      .programme-options .nav-tabs { margin-bottom:18px; }
      .programme-options .nav-tabs>li>a { color:var(--plum); font-weight:700; }
      .programme-view-heading { display:flex; align-items:baseline; justify-content:space-between; gap:18px; border-left:6px solid var(--plum); padding:3px 0 3px 15px; margin-bottom:15px; }
      .programme-view-heading h2 { margin:0; font-size:29px; }
      .programme-view-heading a,.programme-source { color:var(--plum); text-decoration:underline; font-size:12px; }
      .programme-concept { max-width:920px; margin:0 0 18px 21px; color:var(--grey); font-size:16px; line-height:1.55; }
      .semester-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; }
      .semester-card { background:#fff; border:1px solid rgba(73,30,52,.14); border-radius:14px; padding:16px; }
      .semester-card h4 { margin:0 0 3px; font-size:19px; }
      .semester-term { color:var(--grey); font-size:12px; margin-bottom:10px; }
      .semester-courses { display:grid; gap:8px; }
      .course-link { width:100%; text-align:left; background:rgba(200,223,230,.34); border:1px solid rgba(73,30,52,.10); border-radius:9px; padding:10px 11px; cursor:pointer; }
      .course-name { font-weight:700; line-height:1.25; }
      .course-meta { color:var(--grey); font-size:11px; margin-top:4px; }
      .disclaimer { margin:18px 0 26px; padding:13px 15px; border:1px solid rgba(73,30,52,.14); background:rgba(92,96,107,.035); color:var(--grey); border-radius:10px; font-size:13px; line-height:1.5; }
      .disclaimer p { margin:0; }
      .program-selection-return { display:none; width:max-content; margin:0 auto 26px; padding:10px 14px; align-items:center; text-decoration:none!important; }
      .compare-scroll { overflow-x:auto; border:1px solid rgba(73,30,52,.14); border-radius:14px; background:#fff; }
      .compare-table { border-collapse:separate; border-spacing:0; min-width:min(1120px, 100%); width:100%; table-layout:fixed; }
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
      .mobile-comparison { display:none; }
      .mobile-comparison-nav { display:grid; grid-template-columns:44px minmax(0,1fr) 44px; align-items:center; gap:8px; margin:4px 0 12px; }
      .mobile-comparison-button { width:42px; height:42px; border-radius:50%; border:1px solid rgba(73,30,52,.22); background:#fff; color:var(--plum); font-size:22px; line-height:1; }
      .mobile-comparison-button:disabled { opacity:.25; }
      .mobile-comparison-position { text-align:center; }
      .mobile-comparison-position-title { color:var(--black); font-size:13px; font-weight:700; }
      .mobile-comparison-dots { display:flex; justify-content:center; gap:7px; margin-top:7px; }
      .mobile-comparison-dot { width:8px; height:8px; padding:0; border:0; border-radius:50%; background:var(--lilac); }
      .mobile-comparison-dot.active { background:var(--plum); transform:scale(1.2); }
      .mobile-comparison-card { overflow:hidden; border:1px solid rgba(73,30,52,.14); border-radius:14px; background:#fff; box-shadow:0 12px 32px rgba(73,30,52,.09); touch-action:pan-y; }
      .mobile-comparison-card[hidden] { display:none; }
      .mobile-comparison-header { padding:18px 16px 16px; background:var(--green); color:#fff; text-align:center; }
      .mobile-comparison-card.comparator .mobile-comparison-header { background:var(--plum); }
      .mobile-comparison-header h2 { margin:0; color:inherit; font-size:23px; line-height:1.1; }
      .mobile-comparison-header a { display:inline-block; margin-top:7px; color:inherit; font-size:12px; text-decoration:underline; }
      .mobile-comparison-section { border-top:1px solid rgba(73,30,52,.1); }
      .mobile-comparison-section h3 { margin:0; padding:10px 14px; background:var(--blue); color:var(--black); font-family:Inter,Arial,sans-serif; font-size:13px; font-weight:700; }
      .mobile-comparison-section ul { margin:0; padding:0; list-style:none; }
      .mobile-comparison-item { padding:10px 14px; border-top:1px solid rgba(73,30,52,.1); line-height:1.35; }
      .mobile-comparison-item:first-child { border-top:0; }
      .mobile-comparison-item.emphasis { background:rgba(255,225,164,.36); }
      .mobile-comparison-hint { margin:10px 0 0; color:var(--grey); font-size:11px; text-align:center; }
      .cta-row { display:flex; flex-wrap:wrap; gap:12px; }
      .mobile-cta { display:none; }
      .primary-cta,.secondary-cta { display:inline-block; padding:12px 18px; border-radius:10px; font-weight:700; text-decoration:none!important; }
      .primary-cta { background:var(--plum); color:#fff!important; }
      .secondary-cta { color:var(--plum)!important; border:1px solid rgba(73,30,52,.3); background:#fff; }
      .modal-content { border-radius:14px; }
      .modal-title { color:var(--plum); font-family:IvyMode,Georgia,serif; }
      .course-description { font-size:15px; line-height:1.6; }
      @media(max-width:980px){ .container-fluid{padding:0 14px 40px}.top-actions{align-items:flex-start;flex-direction:column}.desktop-cta{display:none}.mobile-cta{display:flex;margin-top:26px}.input-summary{grid-template-columns:1fr}.semester-grid{grid-template-columns:1fr}.programme-view-heading{display:block}.programme-view-heading a{display:inline-block;margin-top:7px}.programme-concept{margin-left:0}.ucr-logo{max-width:210px}.access-card{padding:26px 22px}.program-selection-return{display:flex}.desktop-comparison{display:none}.mobile-comparison{display:block} }
    ")),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/brand.css"),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/shiny.css"),
    tags$script(HTML("
      $(document).on('click', '.course-link', function() {
        const code = $(this).data('code');
        const name = $(this).data('name');
        if (code) Shiny.setInputValue('course_click', {code:String(code), name:String(name||'')}, {priority:'event'});
      });

      function showMobileComparison(root, requestedIndex) {
        const count = Number(root.dataset.comparisonCount || 0);
        const index = Math.max(0, Math.min(count - 1, requestedIndex));
        root.dataset.currentComparison = String(index);
        root.querySelectorAll('.mobile-comparison-card').forEach((card, cardIndex) => {
          const active = cardIndex === index;
          card.hidden = !active;
          card.classList.toggle('active', active);
        });
        root.querySelectorAll('.mobile-comparison-dot').forEach((dot, dotIndex) => {
          const active = dotIndex === index;
          dot.classList.toggle('active', active);
          dot.setAttribute('aria-current', String(active));
        });
        root.querySelector('.mobile-comparison-position-title').textContent = `${index + 1} of ${count}`;
        root.querySelector('.mobile-comparison-button.previous').disabled = index === 0;
        root.querySelector('.mobile-comparison-button.next').disabled = index === count - 1;
      }

      $(document).on('click', '.mobile-comparison-button.previous, .mobile-comparison-button.next, .mobile-comparison-dot', function() {
        const root = this.closest('.mobile-comparison');
        const current = Number(root.dataset.currentComparison || 0);
        const requested = this.hasAttribute('data-comparison-dot')
          ? Number(this.dataset.comparisonDot)
          : current + (this.classList.contains('next') ? 1 : -1);
        showMobileComparison(root, requested);
      });

      $(document).on('keydown', '.mobile-comparison', function(event) {
        if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
        const current = Number(this.dataset.currentComparison || 0);
        showMobileComparison(this, current + (event.key === 'ArrowRight' ? 1 : -1));
      });

      $(document).on('touchstart', '.mobile-comparison-card', function(event) {
        this.closest('.mobile-comparison').dataset.touchStartX = String(event.originalEvent.changedTouches[0].clientX);
      });

      $(document).on('touchend', '.mobile-comparison-card', function(event) {
        const root = this.closest('.mobile-comparison');
        const start = Number(root.dataset.touchStartX);
        delete root.dataset.touchStartX;
        if (!Number.isFinite(start)) return;
        const distance = event.originalEvent.changedTouches[0].clientX - start;
        if (Math.abs(distance) < 45) return;
        const current = Number(root.dataset.currentComparison || 0);
        showMobileComparison(root, current + (distance < 0 ? 1 : -1));
      });

      $(document).on('click', '[data-return-to-programs]', function(event) {
        event.preventDefault();
        const target = document.getElementById('programme-selection');
        if (target) target.scrollIntoView({behavior:'smooth', block:'start'});
      });
    "))
  ),
  uiOutput("app_body")
)

make_student_server <- function(data_config) function(input, output, session) {
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
          tags$h1("Explore your UCR study possibilities"),
          tags$p("Enter the code you received to open the program information prepared around your interests."),
          textInput("access_code", label = "Your access code", placeholder = "UCR-XXXX-XXXX-XXXX-XXXX"),
          actionButton("unlock_pathway", "Open my UCR overview", class = "btn-primary"),
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
      selected <- load_student_record_for_code(data_config, input$access_code)
      if (is.null(selected)) {
        access_error("That code was not recognized. Check it and try again.")
        return()
      }
      record(selected)
    }, error = function(e) {
      access_error("The program data could not be loaded. Please try again later.")
      message("Student app load error: ", conditionMessage(e))
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
        course_cache[[department]] <- read_student_json(
          student_course_file(data_config, department),
          paste("course descriptions for", department)
        )
      }
      description <- course_cache[[department]]$descriptions[[code]]
      if (is.null(description) || !nzchar(safe_text(description))) {
        showModal(modalDialog(title = if (nzchar(course_name)) course_name else code, COURSE_DESCRIPTION_UNAVAILABLE, easyClose = TRUE, footer = modalButton("Close")))
        return()
      }
      showModal(modalDialog(title = if (nzchar(course_name)) course_name else code, div(class = "course-description", safe_text(description)), easyClose = TRUE, footer = modalButton("Close")))
    }, error = function(e) {
      showModal(modalDialog(title = if (nzchar(course_name)) course_name else code, "The course description could not be loaded.", easyClose = TRUE, footer = modalButton("Close")))
      message("Student pilot course load error: ", conditionMessage(e))
    })
  })
}

server <- make_student_server(STUDENT_DATA_CONFIG)

shinyApp(ui, server)
