# Shared presentation helpers for both pilots. Loaded from the repository checkout.
shiny::addResourcePath("ucr-assets", file.path(REPO_ROOT, "assets"))

is_comparator_programme <- function(programme) {
  identical(programme$role, "comparator") || identical(programme$family, "comparator")
}

is_ucr_programme <- function(programme) {
  if (identical(programme$family, "ucr")) return(TRUE)
  programme$role %in% c("ucr-alternative", "ucr-depth", "ucr-balanced", "ucr-thematic")
}

visible_label <- function(record, programme) {
  meta <- record$comparator %||% record$referenceProgramme %||% list()
  if (is_comparator_programme(programme)) return(paste0(meta$name, " at ", meta$institution))

  label <- programme$label %||% ""
  if (nzchar(label) && !grepl("^(UCR[[:space:]]*[—–-]|Disciplinary[[:space:]])", label)) {
    return(if (identical(record$origin, "counselor")) sub("your interests", "related interests", label, fixed = TRUE) else label)
  }

  kind <- programme$alternativeKind %||% programme$alternative_kind %||% ""
  if (identical(kind, "closest-match") || identical(programme$role, "ucr-depth")) return(paste0("Closest match to ", meta$name))
  if (identical(kind, "related-direction") || identical(programme$role, "ucr-balanced")) return(paste0(meta$name, " + related subjects"))
  if (identical(kind, "question-led") || identical(programme$role, "ucr-thematic")) {
    return(if (identical(record$origin, "counselor")) "A broader programme around related interests" else "A broader programme around your interests")
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
