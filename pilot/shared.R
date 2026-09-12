# Shared presentation helpers for both pilots. Loaded from the repository checkout.
shiny::addResourcePath("ucr-assets", file.path(REPO_ROOT, "assets"))

visible_label <- function(record, programme) {
  meta <- record$comparator %||% record$referenceProgramme %||% list()
  if (identical(programme$role, "comparator")) return(paste0(meta$name, " at ", meta$institution))
  label <- programme$label %||% ""
  if (nzchar(label) && !grepl("^(UCR[[:space:]]*[—–-]|Disciplinary[[:space:]])", label)) {
    return(if (identical(record$origin, "counselor")) sub("your interests", "related interests", label, fixed = TRUE) else label)
  }
  if (identical(programme$role, "ucr-depth")) return(paste0("Closest match to ", meta$name))
  if (identical(programme$role, "ucr-balanced")) return(paste0(meta$name, " + related subjects"))
  if (identical(record$origin, "counselor")) "A broader programme around related interests" else "A broader programme around your interests"
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
