# Shared presentation helpers for both pilots. Loaded from the repository checkout.
shiny::addResourcePath("ucr-assets", file.path(REPO_ROOT, "assets"))

is_comparator_programme <- function(programme) {
  identical(programme$role, "comparator") || identical(programme$family, "comparator")
}

is_ucr_programme <- function(programme) {
  if (identical(programme$family, "ucr")) return(TRUE)
  programme$role %in% c("ucr-alternative", "ucr-depth", "ucr-balanced", "ucr-thematic")
}

alternative_rationale_for <- function(record, programme_id) {
  alternatives <- record$academicRationale$alternatives
  if (!is.list(alternatives)) return(NULL)
  target_id <- as.character(programme_id %||% "")
  matches <- Filter(function(item) {
    identical(as.character(item$programmeId %||% ""), target_id)
  }, alternatives)
  if (length(matches)) matches[[1]] else NULL
}

visible_label <- function(record, programme) {
  meta <- record$comparator %||% record$referenceProgramme %||% list()
  if (is_comparator_programme(programme)) return(paste0(meta$name, " at ", meta$institution))

  label <- programme$label %||% ""
  if (nzchar(label) && !grepl("^(UCR[[:space:]]*[—–-]|Disciplinary[[:space:]])", label)) {
    return(if (identical(record$origin, "counselor")) sub("your interests", "related interests", label, fixed = TRUE) else label)
  }

  if (!identical(record$origin, "counselor")) {
    ucr_programmes <- Filter(is_ucr_programme, record$programmes %||% list())
    if (length(ucr_programmes) == 1) return("Your UCR program")
    programme_ids <- vapply(ucr_programmes, function(item) item$id %||% "", character(1))
    programme_index <- match(programme$id %||% "", programme_ids)
    if (!is.na(programme_index)) return(paste("UCR program", programme_index))
    return("UCR program")
  }

  kind <- programme$alternativeKind %||% programme$alternative_kind %||% ""
  if (identical(kind, "closest-match") || identical(programme$role, "ucr-depth")) return(paste0("Closest match to ", meta$name))
  if (identical(kind, "related-direction") || identical(programme$role, "ucr-balanced")) return(paste0(meta$name, " + related subjects"))
  if (identical(kind, "question-led") || identical(programme$role, "ucr-thematic")) {
    return("A broader programme around related interests")
  }
  "Another UCR programme option"
}

render_comparison_notes <- function(record) {
  notes <- Filter(function(note) {
    (is.null(note$placement) || identical(note$placement, "comparison")) && nzchar(note$text %||% "")
  }, record$notes %||% list())
  do.call(shiny::tagList, lapply(notes, function(note) shiny::tags$p(class = "source-note", note$text)))
}

course_level <- function(level) {
  value <- suppressWarnings(as.numeric(level))
  if (length(value) != 1 || is.na(value)) return("")
  if (value < 10) value <- value * 100
  paste0(value, "-level")
}
