e <- new.env()
source('pilot/counselor-shiny/app.R', local=e)
f <- tempfile(fileext='.json')
Sys.setenv(UCR_ACCEPTANCE_FIXTURE_OUTPUT=f)
stopifnot(system2('node','scripts/test-counselor-acceptance.mjs') == 0)
Sys.unsetenv('UCR_ACCEPTANCE_FIXTURE_OUTPUT')
r <- jsonlite::fromJSON(f,simplifyVector=FALSE)
stopifnot(e$qualified_comparison(r))
html <- as.character(e$render_comparison(r))
stopifnot(grepl('qualified-scope',html),grepl('Unknown requirements are not open electives',html),grepl('column-select',html),grepl('course-link',html))
for (kind in c('missing-adverse','missing-scope','unresolved','missing-evidence','exception','missing-schedule')) {
 x <- r
 if(kind=='missing-adverse')x$acceptance$uncertainties[[1]]$adverseResolutions <- list()
 if(kind=='missing-scope')x$audience$comparisonScope <- NULL
 if(kind=='unresolved')x$audience$curriculum$status <- 'unresolved'
 if(kind=='missing-evidence')x$acceptance$challengeEvidenceRefs <- list()
 if(kind=='exception')x$recordStatus <- 'exception'
 if(kind=='missing-schedule')x$programmes[[2]]$schedule <- NULL
 stopifnot(!e$qualified_comparison(x),!grepl('class="compare-view"',as.character(e$render_comparison(x)),fixed=TRUE))
}
e$COUNSELOR_PRESENTATION[[r$id]] <- list(mode='external-only')
stopifnot(!grepl('class="compare-view"',as.character(e$render_comparison(r)),fixed=TRUE))
unlink(f)
cat('Qualified rendering and fail-closed fallback checks passed.\n')
