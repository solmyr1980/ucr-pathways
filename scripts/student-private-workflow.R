# Shared safety checks for the local student-private workflow.

assert_private_tree_ignored <- function(repo_root) {
  ignore_path <- file.path(repo_root, ".gitignore")
  if (!file.exists(ignore_path)) {
    stop("Missing repository .gitignore; refusing to use private student data.")
  }

  rules <- readLines(ignore_path, warn = FALSE, encoding = "UTF-8")
  rules <- sub("\r$", "", rules)
  private_rule <- "/private/"
  private_positions <- which(rules == private_rule)
  if (!length(private_positions)) {
    stop(
      "The repository .gitignore must contain the root-anchored rule ",
      private_rule,
      " before private student data can be used."
    )
  }

  # Requiring the canonical rule after every negation keeps this check simple
  # and prevents a later broad ! pattern from weakening the private boundary.
  private_position <- max(private_positions)
  later_rules <- if (private_position < length(rules)) rules[(private_position + 1L):length(rules)] else character()
  later_negations <- later_rules[startsWith(later_rules, "!")]
  if (length(later_negations)) {
    stop(
      "The /private/ ignore rule must appear after all .gitignore negation rules; ",
      "a later negation could weaken the private-data boundary."
    )
  }

  invisible(TRUE)
}
