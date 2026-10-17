library(shiny)
library(jsonlite)

# Run from the repository root or the app directory; keep code, assets and data in one deployed release.
root_candidates <- c(getwd(), file.path(getwd(), ".."), file.path(getwd(), "../.."))
REPO_ROOT <- root_candidates[file.exists(file.path(root_candidates, "assets/css/brand.css"))][1]
if (is.na(REPO_ROOT)) stop("Run this app from a complete ucr-pathways repository checkout or deployment bundle.")
REPO_ROOT <- normalizePath(REPO_ROOT)
source(file.path(REPO_ROOT, "pilot/shared.R"), local = TRUE)

COUNSELOR_DATA_DIR <- file.path(REPO_ROOT, "data", "counselor")
PRESENTATION_FILE <- file.path(COUNSELOR_DATA_DIR, "presentation-overrides.json")
PRODUCTION_PROGRAMME_FILE <- file.path(COUNSELOR_DATA_DIR, "programmes.json")
PRODUCTION_INTEREST_FILE <- file.path(COUNSELOR_DATA_DIR, "interests.json")
REVIEW_PROGRAMME_FILE <- file.path(COUNSELOR_DATA_DIR, "review-programmes.json")
REVIEW_INTEREST_FILE <- file.path(COUNSELOR_DATA_DIR, "review-interests.json")
PILOT_PROGRAMME_FILE <- file.path(COUNSELOR_DATA_DIR, "pilot-programmes.json")
PILOT_INTEREST_FILE <- file.path(COUNSELOR_DATA_DIR, "pilot-interests.json")
PRODUCTION_COMPARISON_DIR <- file.path(COUNSELOR_DATA_DIR, "comparisons")
PILOT_COMPARISON_DIR <- file.path(REPO_ROOT, "data", "examples")

HAS_PRODUCTION_INDEX <- file.exists(PRODUCTION_PROGRAMME_FILE) && file.exists(PRODUCTION_INTEREST_FILE)
HAS_REVIEW_INDEX <- file.exists(REVIEW_PROGRAMME_FILE) && file.exists(REVIEW_INTEREST_FILE)
DATA_MODE <- if (HAS_PRODUCTION_INDEX) "production" else if (HAS_REVIEW_INDEX) "review" else "pilot"
PROGRAMME_FILE <- switch(DATA_MODE,
  production = PRODUCTION_PROGRAMME_FILE,
  review = REVIEW_PROGRAMME_FILE,
  pilot = PILOT_PROGRAMME_FILE
)
INTEREST_FILE <- switch(DATA_MODE,
  production = PRODUCTION_INTEREST_FILE,
  review = REVIEW_INTEREST_FILE,
  pilot = PILOT_INTEREST_FILE
)
COMPARISON_DIR <- if (identical(DATA_MODE, "pilot")) PILOT_COMPARISON_DIR else PRODUCTION_COMPARISON_DIR
IS_PILOT_DATA <- identical(DATA_MODE, "pilot")
IS_REVIEW_DATA <- identical(DATA_MODE, "review")

UCR_LOGO_URL <- "ucr-assets/brand/ucr-primary-plum.png"
UCR_WEBSITE_URL <- "https://ucr.nl/"
UCR_COURSES_URL <- "https://ucr.nl/education/courses/"
PROGRAM_BUILDER_URL <- "https://program.ucr.nl/"
UCR_COURSE_EC <- 7.5
COURSE_DESCRIPTION_UNAVAILABLE <- "A course description is not currently available."
COURSE_DESCRIPTION_DIR <- file.path(REPO_ROOT, "pilot", "shiny", "data", "courses")
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

read_presentation_settings <- function(path) {
  if (!file.exists(path)) stop("Missing counselor presentation settings: ", path)
  settings <- read_json_file(path)
  if (!is.list(settings) || !is.numeric(settings$schemaVersion) ||
      length(settings$schemaVersion) != 1L || settings$schemaVersion != 1 ||
      !is.list(settings$cases)) {
    stop("Invalid counselor presentation settings header.")
  }

  cases <- settings$cases
  if (length(cases) && (is.null(names(cases)) ||
      any(!grepl("^cp-[0-9]{6}$", names(cases))) || anyDuplicated(names(cases)))) {
    stop("Counselor presentation settings must be keyed by permanent cp- IDs.")
  }
  for (id in names(cases)) {
    entry <- cases[[id]]
    if (!is.list(entry) || !is.character(entry$mode) ||
        length(entry$mode) != 1L ||
        !entry$mode %in% c("normal", "caution", "external-only")) {
      stop("Invalid presentation mode for ", id, ".")
    }
    if (!is.null(entry$message) &&
        (!is.character(entry$message) || length(entry$message) != 1L ||
         !nzchar(trimws(entry$message)))) {
      stop("Invalid presentation message for ", id, ".")
    }
    if (identical(entry$mode, "caution") && is.null(entry$message)) {
      stop("Caution mode requires a case-specific message for ", id, ".")
    }
  }
  cases
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

# Display controls never change canonical academic records or indexed statuses.
COUNSELOR_PRESENTATION <- read_presentation_settings(PRESENTATION_FILE)

presentation_setting <- function(id) {
  COUNSELOR_PRESENTATION[[id]] %||% list(mode = "normal")
}

presentation_mode <- function(id) {
  safe_text(presentation_setting(id)$mode)
}

comparison_id <- function(programme) {
  id <- safe_text(programme$comparisonId)
  if (!nzchar(id)) id <- safe_text(programme$exampleId)
  if (!nzchar(id)) id <- safe_text(programme$programmeProviderId)
  id
}

comparison_path <- function(id) {
  path <- file.path(COMPARISON_DIR, paste0(id, ".json"))
  if (!file.exists(path)) stop("No local comparison record found for ", id)
  path
}

programme_for_comparison <- function(id) {
  matches <- Filter(function(programme) identical(comparison_id(programme), id), COUNSELOR_DATA$programmes)
  if (length(matches)) matches[[1]] else NULL
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

course_description_dialog <- function(code, course_name, description) {
  modalDialog(
    title = if (nzchar(course_name)) course_name else code,
    if (is.null(description) || !nzchar(safe_text(description))) COURSE_DESCRIPTION_UNAVAILABLE
    else div(class = "course-description", safe_text(description)),
    easyClose = TRUE, footer = modalButton("Close")
  )
}

ucr_programmes_for_summary <- function(record) {
  Filter(is_ucr_programme, record$programmes %||% list())
}

# Only explicit audience content can authorize narrative display. Internal fields
# remain in the canonical record and are never used as display fallbacks.
audience_content <- function(record) {
  a <- record$audience
  if (!is.list(a) || !identical(a$schemaVersion, "1.0")) return(list())
  a
}

audience_text <- function(record, field) safe_text(audience_content(record)[[field]])

curriculum_view <- function(record) {
  c <- audience_content(record)$curriculum
  all <- comparator_meta(record)$components %||% list()
  empty <- list(status = "unreviewed", components = list(), year = "", route = "",
                limitation = "Curriculum details are awaiting review. Consult the official programme source for current requirements.")
  if (!is.list(c) || !safe_text(c$status) %in% c("complete", "partial", "unresolved")) return(empty)
  ids <- unlist(c$componentIds, use.names = FALSE)
  known <- vapply(all, function(x) safe_text(x$id), character(1))
  if (anyDuplicated(ids) || !all(ids %in% known)) return(empty)
  if (identical(c$status, "complete") &&
      (identical(record$exception$type, "external-programme-unresolved") ||
       length(ids) != length(known) || abs(sum(vapply(all, function(x) as.numeric(x$credits), numeric(1))) - 180) > .001)) return(empty)
  if (identical(c$status, "partial") && (!length(ids) || !nzchar(safe_text(c$limitation)))) return(empty)
  if (identical(c$status, "unresolved") && (length(ids) || !nzchar(safe_text(c$limitation)))) return(empty)
  list(status = c$status, components = Filter(function(x) safe_text(x$id) %in% ids, all),
       year = if (grepl("^20[0-9]{2}[–-]20[0-9]{2}$", safe_text(c$yearLabel))) safe_text(c$yearLabel) else "",
       route = if (nchar(safe_text(c$routeLabel)) <= 180) safe_text(c$routeLabel) else "",
       limitation = safe_text(c$limitation))
}

render_audience_context <- function(record) {
  view <- curriculum_view(record)
  div(class = "audience-context",
    if (nzchar(audience_text(record, "programmeDescription"))) tags$p(audience_text(record, "programmeDescription")),
    if (nzchar(audience_text(record, "comparisonExplanation"))) tags$p(class = "audience-limitation", audience_text(record, "comparisonExplanation")),
    if (nzchar(view$year)) tags$p("Academic year: ", view$year),
    if (nzchar(view$route)) div(class = "route-note", tags$strong("External pathway: "), view$route),
    if (nzchar(view$limitation)) tags$p(class = "curriculum-status", view$limitation)
  )
}

render_audience_notes <- function(record) {
  a <- audience_content(record)
  notes <- Filter(function(n) safe_text(n$type) %in% unlist(a$noteTypes, use.names = FALSE), record$notes %||% list())
  do.call(tagList, lapply(notes, function(n) tags$p(class = "source-note", safe_text(n$text))))
}

audience_cell_note <- function(record, programme_id, cell) {
  reference <- safe_text(cell$courseCode %||% cell$componentId %||% cell$elementId)
  notes <- Filter(function(n) identical(safe_text(n$programmeId), programme_id) && identical(safe_text(n$reference), reference), audience_content(record)$cellNotes %||% list())
  if (length(notes) == 1) safe_text(notes[[1]]$text) else ""
}

render_comparison_summary <- function(record) {
  programmes <- ucr_programmes_for_summary(record)
  if (!length(programmes)) return(NULL)
  meta <- comparator_meta(record)
  route <- curriculum_view(record)$route
  comparator_name <- safe_text(meta$name)
  comparator_institution <- safe_text(meta$institution)
  comparator_label <- paste(c(comparator_name, if (nzchar(comparator_institution)) paste0("at ", comparator_institution)), collapse = " ")

  cards <- lapply(seq_along(programmes), function(index) {
    programme <- programmes[[index]]
    rationale <- alternative_rationale_for(record, programme$id)
    concept <- if (is.null(rationale) || !programme$id %in% unlist(audience_content(record)$conceptProgrammeIds, use.names = FALSE)) "" else safe_text(rationale$concept)
    div(
      class = "summary-card",
      div(class = "summary-kicker", if (index == 1) "Closest UCR match" else "Additional UCR option"),
      tags$h3(visible_label(record, programme)),
      if (nzchar(concept)) tags$p(concept)
    )
  })

  div(
    class = "comparison-summary", id = "comparison-overview",
    render_audience_context(record),
    div(
      class = "summary-heading",
      tags$h2("What this comparison shows"),
      tags$p(paste0(
        "A curriculum-level comparison of ", comparator_label, " with ", length(programmes),
        if (length(programmes) == 1) " illustrative UCR study composition." else " illustrative UCR study compositions."
      ))
    ),
    div(class = "summary-grid", do.call(tagList, cards)),
    div(
      class = "equivalence-note",
      tags$strong("Important limitation"),
      tags$p("This is a curriculum comparison. A UCR composition is not the same disciplinary degree and does not by itself establish a professional qualification or automatic eligibility for a particular master’s programme.")
    )
  )
}

render_compare_table <- function(record) {
  programmes <- record$programmes %||% list()
  meta <- comparator_meta(record)

  headers <- lapply(programmes, function(programme) {
    label <- visible_label(record, programme)
    if (is_comparator_programme(programme) && nzchar(safe_text(meta$primarySourceUrl))) {
      title <- tags$a(href = meta$primarySourceUrl, target = "_blank", rel = "noopener", paste0(label, " ↗"))
    } else {
      title <- label
    }
    tags$th(scope = "col",
      div(class = "programme-title", title),
      if (is_ucr_programme(programme)) {
        tags$a(class = "programme-source", href = UCR_COURSES_URL, target = "_blank", rel = "noopener", "UCR courses ↗")
      }
    )
  })

  rows <- list()
  for (block in record$blocks %||% list()) {
    rows[[length(rows) + 1]] <- tags$tr(class = "block-row", tags$th(colspan = length(programmes), tags$span(class = "block-title", safe_text(block$title))))
    for (row in block$rows %||% list()) {
      cells <- lapply(programmes, function(programme) {
        value <- cell_value(row$cells[[programme$id]])
        if (is.null(value)) return(tags$td(class = "empty-cell", "\u00A0"))
        ec <- credit_text(value$credits, if (is_ucr_programme(programme)) UCR_COURSE_EC else NULL)
        code <- if (is_ucr_programme(programme)) safe_text(value$courseCode) else ""
        name <- safe_text(value$text)
        tags$td(
          class = if (isTRUE(value$emphasis)) "comparison-cell emphasis" else "comparison-cell",
          div(class = "cell-text", if (nzchar(code)) {
            tags$button(type = "button", class = "course-link", `data-code` = code, `data-name` = name, name)
          } else name),
          if (nzchar(ec)) div(class = "ec-badge", ec),
          if (nzchar(audience_cell_note(record, programme$id, value))) div(class = "cell-note", audience_cell_note(record, programme$id, value))
        )
      })
      rows[[length(rows) + 1]] <- do.call(tags$tr, cells)
    }
  }

  labels <- vapply(programmes, function(p) visible_label(record, p), character(1))
  div(class = "compare-view", `data-count` = length(programmes),
    tags$p(class = "comparison-legend", "Rows show curricular relationships, including partial matches, rather than course equivalence. A blank cell means there is no closely comparable component in that row. Optional independent research is additional to the displayed 180 EC."),
    div(class = "comparison-navigation", role = "navigation", `aria-label` = "Comparison columns",
      tags$button(type = "button", class = "column-previous secondary-button", "← Previous"),
      tags$label("Programme column", tags$select(class = "column-select", `aria-label` = "Programme column",
        do.call(tagList, lapply(seq_along(labels), function(i) tags$option(value = i - 1, labels[[i]]))))),
      tags$button(type = "button", class = "column-next secondary-button", "Next →"),
      tags$span(class = "column-position", `aria-live` = "polite", paste("1 of", length(programmes))),
      tags$span(class = "column-name", labels[[1]]),
      tags$a(href = "#comparison-overview", "Back to overview")
    ),
    div(class = "compare-scroll", tabindex = "0", role = "region", `aria-label` = "Curriculum comparison; scroll horizontally to compare columns",
      tags$table(class = "compare-table", style = paste0("--programme-count:", length(programmes)),
        tags$thead(do.call(tags$tr, headers)), tags$tbody(do.call(tagList, rows))))
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
            paste(unique(vapply(matches, function(x) safe_text(x$interest), character(1))), collapse = " · ")
          )
        }
      ),
      tags$button(type = "button", class = "open-comparison", `data-id` = comparison_id(programme),
        if (identical(safe_text(programme$recordStatus), "exception") ||
            identical(presentation_mode(comparison_id(programme)), "external-only"))
          "View programme" else "Compare with UCR")
    )
  }))
}

render_exception <- function(record, presentation_only = FALSE, display_note = "") {
  meta <- comparator_meta(record)
  view <- curriculum_view(record)
  status_copy <- if (presentation_only)
    "Only the external programme is shown. A prepared UCR comparison has been withheld from presentation."
    else if (identical(safe_text(record$exception$type), "no-defensible-ucr-match"))
    "UCR currently cannot construct a sufficiently close programme for a meaningful curriculum comparison."
    else if (identical(safe_text(record$exception$type), "ucr-assessment-pending"))
    "A comparison with UCR is awaiting assessment."
    else "A reliable curriculum comparison is currently unavailable. The external curriculum has unresolved requirements; no complete degree pathway is certified here."
  div(class = "comparison-shell",
    brand_header(),
    div(class = "comparison-head",
      div(tags$h1(safe_text(meta$name)), tags$p(safe_text(meta$institution))),
      actionButton("back_to_search", "← Back to search", class = "secondary-button")),
    div(class = "comparison-summary", id = "comparison-overview",
      tags$h2("About this programme"), tags$p(class = "comparison-status", status_copy),
      render_audience_context(record),
      if (!nzchar(audience_text(record, "programmeDescription"))) tags$p("A programme description is awaiting review. Use the official source to explore the programme."),
      tags$a(href = safe_text(meta$primarySourceUrl), target = "_blank", rel = "noopener", "Official programme source ↗")),
    if (length(view$components)) div(class = "external-curriculum",
      tags$h2(if (identical(view$status, "complete")) "Complete external curriculum — 180 EC" else "Verified partial curriculum — incomplete degree pathway"),
      if (identical(view$status, "partial")) tags$p("Only the verified components listed below are shown. They do not constitute a complete degree programme."),
      div(class = "compare-scroll", tags$table(class = "compare-table external-table",
        tags$thead(tags$tr(tags$th("External programme components"))),
        tags$tbody(do.call(tagList, lapply(view$components, function(component) {
          note <- safe_text(audience_content(record)$componentNotes[[safe_text(component$id)]])
          tags$tr(tags$td(class = "comparison-cell", div(class = "cell-text", safe_text(component$name)),
            div(class = "ec-badge", credit_text(component$credits)),
            if (nzchar(note)) div(class = "cell-note", note)))
        })))))),
    render_audience_notes(record))
}

render_comparison <- function(record) {
  if (identical(safe_text(record$recordStatus), "exception")) return(render_exception(record))
  setting <- presentation_setting(safe_text(record$id))
  if (identical(setting$mode, "external-only") || curriculum_view(record)$status %in% c("partial", "unresolved")) {
    return(render_exception(record, presentation_only = TRUE,
                            display_note = ""))
  }
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
    if (identical(setting$mode, "caution")) {
      div(class = "presentation-caution",
        tags$strong("Important: limited disciplinary correspondence"),
        tags$p("UCR offers related academic study, but specialist subjects or forms of training may differ substantially. This comparison does not establish degree equivalence."))
    },
    render_comparison_summary(record),
    render_compare_table(record),
    render_audience_notes(record),
    div(class = "cta-row", tags$a(class = "primary-cta", href = PROGRAM_BUILDER_URL, target = "_blank", rel = "noopener", "Explore the UCR Program Builder ↗"))
  )
}

render_search_shell <- function(search_text = "") {
  div(
    brand_header(),
    div(
      class = "hero",
      tags$h1("Explore bachelor’s programmes and study options at UCR"),
      tags$p("Search in English by bachelor’s programme or by what your student is interested in. Select a programme to see the available UCR comparison or a clear explanation when a meaningful comparison is not possible.")
    ),
    div(
      class = "search-box",
      div(
        class = "search-grid",
        textInput("search_text", "Search in English by programme or interest", value = search_text, placeholder = "e.g. Psychology, climate change, artificial intelligence…"),
        uiOutput("institution_filter"),
        uiOutput("language_filter")
      ),
      if (IS_REVIEW_DATA) {
        div(class = "pilot-note", paste0("Review mode: this search currently contains ", length(COUNSELOR_DATA$programmes), " production records. These records are being reviewed before the full counselor corpus is released."))
      } else if (IS_PILOT_DATA) {
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
      .comparison-summary{margin:0 0 20px;background:#fff;border:1px solid rgba(73,30,52,.14);border-radius:14px;padding:18px}.summary-heading h2{margin:0 0 5px;font-size:27px}.summary-heading p{margin:0;color:var(--grey);line-height:1.5}.route-note{margin-top:12px;padding:10px 12px;border-radius:9px;background:rgba(185,217,235,.32);color:var(--plum)}.summary-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin-top:14px}.summary-card{border:1px solid rgba(73,30,52,.14);border-radius:11px;padding:14px;background:rgba(255,255,255,.96)}.summary-card h3{font-family:Inter,Arial,sans-serif;font-size:17px;font-weight:700;margin:3px 0 7px;color:var(--plum)}.summary-card p{margin:0;color:var(--grey);font-size:14px;line-height:1.48}.summary-kicker{text-transform:uppercase;letter-spacing:.055em;font-size:11px;font-weight:800;color:var(--grey)}.equivalence-note{margin-top:14px;border-left:5px solid var(--plum);padding:11px 14px;background:rgba(255,225,164,.28);color:var(--grey);line-height:1.5}.equivalence-note p{margin:4px 0 0}
      .presentation-caution{margin:0 0 20px;padding:18px 20px;border:2px solid #995e24;border-radius:12px;background:#fff1d6;color:#593711;font-size:16px;line-height:1.55}.presentation-caution strong{display:block;font-size:18px}.presentation-caution p{margin:7px 0 0}
      .compare-scroll{overflow-x:auto;border:1px solid rgba(73,30,52,.14);border-radius:14px;background:#fff}.compare-table{border-collapse:separate;border-spacing:0;min-width:min(1120px,100%);width:100%;table-layout:fixed}.compare-table th,.compare-table td{border-right:1px solid rgba(73,30,52,.1);border-bottom:1px solid rgba(73,30,52,.1);padding:13px 15px;vertical-align:top}.compare-table thead th{background:var(--plum);color:#fff;border-right-color:rgba(255,255,255,.18)}.programme-title{font-size:16px;font-weight:700}.programme-title a,.programme-source{color:inherit}.programme-source{display:inline-block;margin-top:5px;color:#fff;opacity:.82;font-size:12px}.block-row th{background:var(--blue);color:var(--plum);font-size:14px;font-weight:700}.comparison-cell{background:#fff;line-height:1.35}.comparison-cell.emphasis{background:rgba(255,225,164,.36)}.empty-cell{background:rgba(92,96,107,.035)}.ec-badge{display:inline-block;margin-top:6px;padding:2px 6px;border-radius:999px;background:rgba(73,30,52,.08);color:var(--grey);font-size:11px}.cell-note{color:var(--grey);font-size:12px;margin-top:5px}.transparency-note{margin-top:18px;background:#fff;border-left:5px solid var(--plum);padding:14px 17px;color:var(--grey);line-height:1.5}.transparency-note p{margin:5px 0 0}.cta-row{display:flex;justify-content:flex-end;margin-top:20px}.primary-cta{display:inline-block;background:var(--plum);color:#fff!important;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none!important}
      .cell-text,.programme-title,.cell-note{overflow-wrap:anywhere}.course-link{max-width:100%;overflow-wrap:anywhere;padding:0;border:0;background:none;color:var(--plum);font:inherit;text-align:left;text-decoration:underline;cursor:pointer}.course-link:hover,.course-link:focus-visible{color:var(--black)}.modal-content{border-radius:14px}.modal-title{color:var(--plum);font-family:IvyMode,Georgia,serif}.course-description{font-size:15px;line-height:1.6}
      .comparison-navigation{display:none}.comparison-legend{font-size:14px;color:var(--grey);line-height:1.5}.curriculum-status,.audience-limitation{border-left:4px solid var(--plum);padding:8px 12px;background:rgba(255,225,164,.28)}
      @media(max-width:700px){.comparison-navigation{display:flex;position:sticky;top:0;z-index:10;gap:8px;flex-wrap:wrap;align-items:center;background:var(--white);padding:10px 0;border-bottom:2px solid var(--plum)}.comparison-navigation label{width:100%;order:-1;margin:0;font-size:13px}.column-select{display:block;width:100%;max-width:100%;min-height:44px;border:1px solid var(--plum);border-radius:7px;background:white;font-size:15px}.comparison-navigation button{min-height:44px;padding:7px 10px}.column-position,.comparison-navigation a{font-size:13px}.compare-view .compare-table{width:calc(var(--programme-count) * (100vw - 30px));min-width:calc(var(--programme-count) * (100vw - 30px))}.block-title{position:sticky;left:15px;display:block;width:calc(100vw - 60px);max-width:calc(100vw - 60px)}.column-name{width:100%;font-size:14px;font-weight:700;overflow-wrap:anywhere}.summary-grid{grid-template-columns:1fr}.external-table{min-width:100%}}
      @media(max-width:900px){.container-fluid{padding:0 14px 40px}.search-grid{grid-template-columns:1fr}.result-card{display:block}.open-comparison{margin-top:13px}.comparison-head{display:block}.comparison-head .secondary-button{margin-top:10px}.ucr-logo{max-width:210px}}
    ")),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/brand.css"),
    tags$link(rel = "stylesheet", href = "ucr-assets/css/shiny.css"),
    tags$script(HTML("
      function selectColumn(view, index) {
        const scroll = view.querySelector('.compare-scroll');
        const count = Number(view.dataset.count);
        index = Math.max(0, Math.min(count - 1, index));
        scroll.scrollLeft = index * scroll.querySelector('table').getBoundingClientRect().width / count;
        if (scroll.onscroll) scroll.onscroll();
      }
      $(document).on('change', '.column-select', function(){ selectColumn(this.closest('.compare-view'), Number(this.value)); });
      $(document).on('click', '.column-previous,.column-next', function(){
        const view = this.closest('.compare-view');
        selectColumn(view, Number(view.querySelector('.column-select').value) + (this.classList.contains('column-next') ? 1 : -1));
      });
      $(document).on('shiny:value', function(){
        requestAnimationFrame(function(){ document.querySelectorAll('.compare-view').forEach(function(view){
          const scroll = view.querySelector('.compare-scroll');
          const update = function(){
            const count = Number(view.dataset.count);
            const width = scroll.querySelector('table').getBoundingClientRect().width / count;
            const index = Math.max(0, Math.min(count-1, Math.round(scroll.scrollLeft / width)));
            view.querySelector('.column-select').value = index;
            view.querySelector('.column-name').textContent = view.querySelector('.column-select').options[index].textContent;
            view.querySelector('.column-position').textContent = (index+1) + ' of ' + count;
            view.querySelector('.column-previous').disabled = index === 0;
            view.querySelector('.column-next').disabled = index === count-1;
          };
          scroll.onscroll = update; update();
        }); });
      });
      $(document).on('click', '.open-comparison' , function(){
        Shiny.setInputValue('open_comparison', String($(this).data('id')), {priority:'event'});
      });
      $(document).on('click', '.course-link', function(){
        const code = $(this).data('code');
        const name = $(this).data('name');
        if (code) Shiny.setInputValue('course_click', {code:String(code), name:String(name||'')}, {priority:'event'});
      });
    "))
  ),
  uiOutput("app_body")
)

server <- function(input, output, session) {
  selected <- reactiveVal(NULL)
  course_cache <- reactiveValues()
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
      programme <- programme_for_comparison(id)
      display_name <- if (is.null(programme)) "" else safe_text(programme$displayName)
      if (nzchar(display_name)) {
        if (!is.null(record$comparator)) record$comparator$name <- display_name
        if (!is.null(record$referenceProgramme)) record$referenceProgramme$name <- display_name
      }
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

  observeEvent(input$course_click, {
    code <- safe_text(input$course_click$code)
    course_name <- safe_text(input$course_click$name)
    if (!grepl("^[A-Za-z0-9]+$", code)) return()
    department <- substr(code, 1, 3)
    title <- if (nzchar(course_name)) course_name else code
    tryCatch({
      if (is.null(course_cache[[department]])) {
        course_cache[[department]] <- read_json_file(file.path(COURSE_DESCRIPTION_DIR, paste0(department, ".json")))
      }
      description <- course_cache[[department]]$descriptions[[code]]
      showModal(course_description_dialog(code, course_name, description))
    }, error = function(e) {
      showModal(modalDialog(title = title, "The course description could not be loaded.", easyClose = TRUE, footer = modalButton("Close")))
      message("Counselor course load error: ", conditionMessage(e))
    })
  })
}

shinyApp(ui, server)
