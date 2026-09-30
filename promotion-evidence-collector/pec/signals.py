"""Deterministic text signals shared by the rule engine and the guardrails.

The guardrails apply these signals to every candidate, whichever extraction
engine produced it, so that an LLM cannot raise a level that the source
passage does not support.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .extract import normalize_text as normalize

# ---------------------------------------------------------------------------
# Document genre


SELF_GENRES = {"cv", "reflective", "biography", "application"}

GENRE_PATTERNS: list[tuple[str, str, str]] = [
    # (genre, filename pattern, text pattern)
    ("cv", r"\b(cv|resume|curriculum[ _-]?vitae|vita)\b", r"\bcurriculum vitae\b|\bresum[eé]\b"),
    ("reflective", r"reflect|portfolio|teaching[ _-]statement|teaching[ _-]philosophy|personal[ _-]statement|self[ _-]?(evaluation|assessment)|narrative",
     r"\breflective statement\b|\bteaching statement\b|\bteaching philosophy\b|\bpersonal statement\b|\bself-evaluation\b"),
    ("biography", r"\bbio(graphy)?\b", r"^\s*(dr\.?|prof\.?)?\s*[A-Z][a-z]+ [A-Z][a-z]+ is an? (assistant|associate|professor|lecturer)"),
    ("application", r"application|promotion[ _-]request|motivation|cover[ _-]letter|sollicitatie",
     r"\bapplication for\b|\bletter of motivation\b|\bI am applying\b|\bI would like to apply\b|\bapply for the\b"),
    ("certificate", r"certificat|diploma|\bsutq\b|\bsko\b|\bbko\b|\butq\b", r"\bcertif(y|ies|icate)\b|\bhas successfully completed\b|\bis hereby awarded\b"),
    ("minutes", r"minutes|notulen", r"\bminutes of\b|\bpresent:\s|\bapologies:\s|\baction points?\b"),
    ("handbook", r"handbook|manual|guide", r"\bhandbook\b"),
    ("policy", r"policy|regulation|\boer\b|\bter\b|rules", r"\bthis policy\b|\bregulations?\b"),
    ("report", r"report|verslag|findings", r"\bexecutive summary\b|\bfindings\b|\brecommendations\b"),
    ("evaluation", r"evaluation|evals?\b|feedback|survey|appraisal|review|p&d|r&o|observation",
     r"\bcourse evaluation\b|\bstudent evaluations?\b|\bpeer observation\b|\bperformance review\b|\bannual review\b|\bappraisal\b"),
    ("letter", r"letter|appointment|email|e-mail|\.msg", r"^\s*dear\b|\bwe are pleased to\b|\byours sincerely\b|\bkind regards\b|^\s*(from|to|subject):"),
    ("proposal", r"proposal|plan\b|grant[ _-]application", r"\bresearch question\b|\bproposal\b|\baims? of (this|the) project\b"),
    ("publication", r"article|paper|chapter|journal|preprint", r"\babstract\b.*\bkeywords\b|\bdoi\b|\bjournal of\b"),
    ("course_material", r"syllabus|course[ _-]?(guide|manual|outline)|reader|lecture|slides|rubric", r"\blearning outcomes\b|\bsyllabus\b|\bcourse description\b"),
]


def detect_genre(filename: str, text: str) -> str:
    name = filename.lower()
    head = text[:3000]
    application_text = next(p[2] for p in GENRE_PATTERNS if p[0] == "application")
    for genre, fname_pat, _ in GENRE_PATTERNS:
        if re.search(fname_pat, name, re.I):
            # A letter the candidate wrote to apply for something is the
            # candidate's own account, not an independent letter.
            if genre == "letter" and re.search(application_text, head, re.I | re.M):
                return "application"
            return genre
    for genre, _, text_pat in GENRE_PATTERNS:
        if re.search(text_pat, head, re.I | re.M):
            return genre
    return "other"


# ---------------------------------------------------------------------------
# Passage segmentation

BULLET = re.compile(r"^\s*([-*•▪●‣]|\d+[.)])\s+")
DATE_LINE = re.compile(r"^\s*(\d{4}|[A-Z][a-z]{2,8}\.? \d{4})")
MAX_PASSAGE = 700
WRAP_WIDTH = 55  # a line at least this long is treated as wrapped prose
TARGET_WINDOW = 480


def _split_long(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text)
    out, buf = [], ""
    for sentence in sentences:
        if buf and len(buf) + len(sentence) > TARGET_WINDOW:
            out.append(buf.strip())
            buf = ""
        buf += (" " if buf else "") + sentence
    if buf.strip():
        out.append(buf.strip())
    return out


def segment(page_text: str) -> list[str]:
    """Split a page into passages that keep CV entries and bullet lists
    together while breaking long prose into sentence windows."""
    blocks = re.split(r"\n\s*\n", page_text)
    passages: list[str] = []
    for block in blocks:
        lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        joined = "\n".join(lines)
        if len(joined) <= MAX_PASSAGE:
            passages.append(joined)
            continue
        # Rebuild paragraphs. A full-width line (PDF line wrap) continues the
        # paragraph. A short line ends it. Bullets attach to a short heading
        # line such as a CV entry title.
        paras: list[str] = []
        for line in lines:
            if not paras:
                paras.append(line)
                continue
            prev = paras[-1]
            last_line = prev.split("\n")[-1]
            if BULLET.match(line):
                if len(prev) < 120 and "\n" not in prev and not BULLET.match(prev):
                    paras[-1] = prev + "\n" + line
                else:
                    paras.append(line)
            elif len(last_line.strip()) >= WRAP_WIDTH:
                paras[-1] = prev + " " + line.strip()
            else:
                paras.append(line)
        for para in paras:
            if len(para) <= MAX_PASSAGE:
                passages.append(para)
            else:
                passages.extend(_split_long(re.sub(r"\s*\n\s*", " ", para)))
    return [p.strip() for p in passages if len(re.sub(r"\W", "", p)) >= 12]


# ---------------------------------------------------------------------------
# Dates

YEAR = r"(?:19[89]\d|20[0-4]\d)"
RANGE_RE = re.compile(
    rf"(?:(?:since|from)\s+)?\b({YEAR})\s*(?:-|–|—|to|until|till)\s*({YEAR}|present|now|current|today)\b",
    re.I,
)
SINCE_RE = re.compile(rf"\bsince\s+(?:[A-Z][a-z]+\s+)?({YEAR})\b", re.I)
YEAR_RE = re.compile(rf"\b({YEAR})\b")
FULL_DATE_RE = re.compile(
    rf"\b(\d{{1,2}})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+({YEAR})\b"
    rf"|\b({YEAR})-(\d{{2}})-(\d{{2}})\b"
    rf"|\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{{1,2}}),?\s+({YEAR})\b",
    re.I,
)
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], start=1)}


def date_range(text: str) -> tuple[str, str]:
    match = RANGE_RE.search(text)
    if match:
        end = match.group(2)
        return match.group(1), "present" if not end[0].isdigit() else end
    match = SINCE_RE.search(text)
    if match:
        return match.group(1), "present"
    years = YEAR_RE.findall(text)
    if years:
        return years[0], years[0]
    return "", ""


def first_full_date(text: str) -> str:
    match = FULL_DATE_RE.search(text)
    if not match:
        return ""
    g = match.groups()
    if g[0]:
        return f"{g[2]}-{MONTHS[g[1].lower()]:02d}-{int(g[0]):02d}"
    if g[3]:
        return f"{g[3]}-{g[4]}-{g[5]}"
    return f"{g[8]}-{MONTHS[g[6].lower()]:02d}-{int(g[7]):02d}"


# ---------------------------------------------------------------------------
# Known entities: roles, bodies and projects. Order sets priority when a
# passage mentions more than one.


@dataclass(frozen=True)
class Entity:
    key: str
    pattern: str
    title: str
    l3a_title: str
    kind: str  # senior_role, coordination, membership, governance, project, qualification
    domains: tuple[int, ...]


ENTITIES: list[Entity] = [
    Entity("head_tutor", r"\bhead\s+tutor\b", "Head Tutor role",
           "Leadership of UCR tutoring and advising system", "senior_role", (3, 4)),
    Entity("interim_head_social_sciences", r"\b(interim\s+)?head\s+of\s+(the\s+)?social\s+sciences?(\s+department)?\b",
           "Interim Head of Social Sciences role", "Leadership of the Social Sciences department", "senior_role", (5, 4)),
    Entity("extended_executive_board", r"\bextended\s+executive\s+board\b", "Extended Executive Board membership",
           "Institutional decision-making in the Extended Executive Board", "membership", (5,)),
    Entity("board_of_studies", r"\bboard\s+of\s+studies\b", "Board of Studies membership",
           "Curriculum governance through the Board of Studies", "membership", (5,)),
    Entity("works_council", r"\bworks\s+council\b|\bondernemingsraad\b", "Works Council role",
           "Works Council role", "governance", (4,)),
    Entity("programme_committee", r"\bprogr?am(me)?\s+committee\b|\bopleidingscommissie\b", "Programme Committee membership",
           "Programme quality work through the Programme Committee", "membership", (5, 2)),
    Entity("film_media_track", r"\bfilm\s+(and|&)\s+media(\s+studies)?(\s+track)?\b", "Film and Media Studies Track coordination",
           "Development of the Film and Media Studies Track", "coordination", (5,)),
    Entity("first_year_english", r"\bfirst[-\s]year\s+english(\s+programme|\s+program)?\b", "First-Year English Programme coordination",
           "Coordination of the First-Year English Programme across UCR", "coordination", (5, 1, 2)),
    Entity("salvaged_semiotics", r"\bsalvaged\s+semiotics\b", "Salvaged Semiotics educational innovation project",
           "Salvaged Semiotics educational innovation project", "project", (1, 2)),
    Entity("interdisciplinary_education", r"\binterdisciplinary\s+educat\w*\s+(programme|program|intervention)\b|\binterdisciplinary\s+education\b",
           "Interdisciplinary educational intervention", "Interdisciplinary educational intervention", "project", (5, 6)),
    Entity("sutq", r"\bsenior\s+(university\s+)?teaching\s+qualification\b|\bSU?TQ\b|\bSKO\b", "Senior Teaching Qualification",
           "Senior Teaching Qualification", "qualification", (4,)),
    Entity("utq", r"\b(?<!senior\s)university\s+teaching\s+qualification\b|\bUTQ\b|\bBKO\b", "University Teaching Qualification",
           "University Teaching Qualification", "qualification", (4,)),
    Entity("jrf_archive", r"\bJRF\b", "JRF student archival research project",
           "JRF student archival research project", "project", (1,)),
    Entity("international_exchange", r"\b(international\s+)?(student\s+)?exchange\s+(programme|program|agreement|partnership)s?\b",
           "International exchange development", "Development of UCR international exchange arrangements", "project", (5,)),
    Entity("nvao", r"\bNVAO\b|\baccreditation\b", "Accreditation work", "Institutional accreditation work", "project", (5, 6)),
]

GENERIC_ENTITY_RE = re.compile(
    r"\b((?:[A-Z][\w'-]+\s+)(?:(?:[A-Z][\w'-]+|and|of|for|the|in|&)\s+){0,5}"
    r"(?:Project|Programme|Program|Grant|Initiative|Fund|Award|Prize|Fellowship|Track|Minor|Module|Course|Lab|Laboratory))\b"
)
GENERIC_STOP = {"The", "This", "Our", "A", "An", "Each", "Every", "UCR"}


def match_entity(text: str) -> Entity | None:
    for entity in ENTITIES:
        if re.search(entity.pattern, text, re.I):
            return entity
    return None


def generic_entity(text: str) -> str:
    for match in GENERIC_ENTITY_RE.finditer(text):
        name = match.group(1).strip()
        words = name.split()
        while words and words[0] in GENERIC_STOP:
            words = words[1:]
        if len(words) >= 2:
            return " ".join(words)
    return ""


# ---------------------------------------------------------------------------
# Domain lexicon

DOMAIN_TERMS: dict[int, list[tuple[str, int]]] = {
    1: [(r"\bteach(es|ing)?\b|\btaught\b", 2), (r"\blectur(e|es|ed|ing)\b", 1), (r"\bcourses?\b", 1),
        (r"\bseminars?\b|\bclass(es|room)?\b", 1), (r"\bstudent learning\b", 3), (r"\bpedagog", 2),
        (r"\b(capstone|thesis|theses)\b", 1), (r"\b(student|undergraduate)[-\s]research\b", 3),
        (r"\b(with|and) (a |two |three )?(former )?(student|students|undergraduates?)\b", 2),
        (r"\bresearch[-\s]led teaching\b", 2), (r"\bsupervis\w+ (student|thesis|capstone|undergraduate)", 2),
        (r"\bstudents?\b", 1)],
    2: [(r"\bassess(ment|ments|ed|ing)?\b", 2), (r"\brubrics?\b", 3), (r"\bfeedback\b", 2), (r"\bgrading\b|\bgrades?\b", 1),
        (r"\bexam(s|ination|inations)?\b", 1), (r"\blearning (outcomes|objectives|goals)\b", 2),
        (r"\bcourse design\b|\bdesign(ed|ing)? (a |the |new )?(course|module|assignment)", 3),
        (r"\bsyllab(us|i)\b", 2), (r"\bconstructive alignment\b", 3), (r"\bassignments?\b", 1)],
    3: [(r"\btutor(s|ing|ed|ial)?\b", 3), (r"\bhead tutor\b", 3), (r"\badvis(ing|ed|e|ees?|ors?|er|ers)\b", 2),
        (r"\bacademic advising\b", 3), (r"\bstudy advice\b", 2), (r"\bportfolios?\b", 1), (r"\bbelonging\b", 2),
        (r"\bstudent (development|wellbeing|well-being|support)\b", 2), (r"\bpastoral\b", 2), (r"\btutees?\b", 3)],
    4: [(r"\b(faculty|teacher|staff|professional) development\b", 3), (r"\bprofessional learning\b", 3),
        (r"\btrain(ing|ed|s)? (of |for )?(new )?(tutors|staff|faculty|teachers|colleagues)\b", 3),
        (r"\bmentor(ing|ed|s)? (of )?(new )?(colleagues|faculty|staff|teachers|tutors|junior)\b", 3),
        (r"\bpeer (observation|review of teaching|learning)\b", 3), (r"\bworkshops? (for|with) (staff|colleagues|faculty|teachers)\b", 3),
        (r"\bcommunity of practice\b|\bcollegial\b|\bcollective reflection\b", 3),
        (r"\bteaching qualification\b|\b(SU?TQ|UTQ)\b|\bSKO\b|\bBKO\b", 3), (r"\bappraise[sd]?\b|\bappraisals?\b", 2),
        (r"\bsupervis\w+ (of )?(faculty|tutors|staff|colleagues|advisors|teachers)\b", 3), (r"\bonboarding\b", 2),
        (r"\bworks council\b", 1)],
    5: [(r"\bcurricul(um|a|ar)\b(?!\s+vitae)", 3), (r"\bprogr?am(me)?s?\b", 1), (r"\btracks?\b", 1), (r"\b(major|minor)s?\b", 1),
        (r"\bdepartment(s|al)?\b", 1), (r"\bclusters?\b", 1), (r"\binterdisciplinar", 2), (r"\bexchange\b", 1),
        (r"\bstudy abroad\b", 2), (r"\baccreditation\b|\bNVAO\b", 3), (r"\bboard of studies\b", 2),
        (r"\bprogr?am(me)? committee\b", 2), (r"\bfirst[-\s]year\b", 1), (r"\b(student )?pathways?\b", 1),
        (r"\bprogression\b", 1), (r"\bcourse offering\b", 2), (r"\bnew course(s)?\b", 1)],
    6: [(r"\beducational (research|inquiry|innovation|evaluation|literature)\b", 3), (r"\bhigher education\b", 2),
        (r"\bscholarship of teaching\b|\bSoTL\b", 3), (r"\b(institutional|survey|evaluation) data\b", 3),
        (r"\bevidence[-\s]based\b|\bevidence-informed\b", 2), (r"\bresearch question\b", 2), (r"\bfindings\b", 1),
        (r"\bsurveys?\b|\bquestionnaires?\b|\bfocus groups?\b|\binterviews\b", 1), (r"\binquiry\b", 1),
        (r"\beducational innovation\b", 2)],
}


def domain_scores(text: str) -> dict[int, int]:
    scores = {}
    for domain, terms in DOMAIN_TERMS.items():
        total = 0
        for pattern, weight in terms:
            hits = len(re.findall(pattern, text, re.I))
            total += weight * min(hits, 2)
        scores[domain] = total
    return scores


def pick_domains(scores: dict[int, int], hint: tuple[int, ...] = ()) -> list[int]:
    boosted = dict(scores)
    for i, d in enumerate(hint):
        boosted[d] = boosted.get(d, 0) + (3 if i == 0 else 1)
    top = max(boosted.values()) if boosted else 0
    if top <= 0:
        return []
    chosen = [d for d, s in sorted(boosted.items(), key=lambda x: (-x[1], x[0])) if s >= max(2, 0.6 * top)]
    return chosen[:3] or [max(boosted, key=boosted.get)]


# ---------------------------------------------------------------------------
# Level signals

ACTION_RE = re.compile(
    r"\b(overs(aw|ee|ees|eeing|een)|coordinat\w*|develop(ed|s|ing)?|design(ed|s|ing)?|implement\w*|introduc\w*|"
    r"establish\w*|(?<!was )led\b|lead(s|ing)?\b|chair(ed|s|ing)?\b|manag(ed|es|ing)|restructur\w*|revis(ed|es|ing)|"
    r"reform\w*|apprais(ed|es|ing)|appraise|train(ed|s|ing)|supervis(ed|es|ing)|organi[sz](ed|es|ing)|initiat\w*|"
    r"draft(ed|s|ing)|wrote|author(ed)|launch\w*|set up|buil[dt]\w*|creat(ed|es|ing)|redesign\w*|"
    r"report(ed|s|ing)? (findings|recommendations|to the)|ensur(ed|es|ing)|responsible for|advis(ed|es) the (board|executive)|"
    r"negotiat\w*|spearhead\w*|convened?|rolled out|embedded|integrat(ed|es|ing)|conduct(ed|s|ing)|mentor(ed|ing))\b",
    re.I,
)

SCOPE_RE = re.compile(
    r"\b(across (ucr|the college|the institution|all|clusters|departments|programmes|programs|tracks|the curriculum|disciplines)|"
    r"ucr[-\s]wide|college[-\s]wide|institution(al|[-\s]wide)|campus[-\s]wide|university[-\s]wide|faculty[-\s]wide|"
    r"all (students|tutors|faculty|staff|departments|first[-\s]year|teachers|lecturers|advisors|courses|programmes|tracks)|"
    r"whole college|entire (college|curriculum|faculty)|board of studies|executive board|dean|"
    r"(the|social sciences?|humanities|sciences?|arts|academic core) department|"
    r"(tutoring|advising|mentoring|assessment|curriculum|feedback|quality assurance|training) (system|structure|framework|policy|policies|guidelines|procedures)|"
    r"accreditation|nvao|self[-\s]evaluation report|teaching quality|"
    r"(\d+|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty)\s+"
    r"(faculty\s+|academic\s+)?(tutors|faculty|advisors|advisers|staff|teachers|lecturers|colleagues|members of staff|instructors)|"
    r"departmental (strategy|curriculum|budgets?|structures?|policy)|across (the )?(social sciences|humanities|sciences|academic core|department))\b",
    re.I,
)

MEMBERSHIP_RE = re.compile(r"\b(member(ship)?|served on|sat on|seat on|participant|participated in|attended|elected to)\b", re.I)
LEADERSHIP_WORD_RE = re.compile(r"\b(chair(ed|s|ing)?|vice[-\s]chair|president|convenor|head|director|lead|coordinator)\b", re.I)
COORDINATION_RE = re.compile(r"\bcoordinat(or|ion|ed|ing)\b", re.I)
SENIOR_TITLE_RE = re.compile(r"\b(head tutor|(interim )?head of|director|dean|vice[-\s]dean|programme director|chair of the board|extended executive board)\b", re.I)

EDU_OBJECT_RE = re.compile(
    r"\b(teaching|pedagog\w*|curricul\w*|higher education|student learning|learning outcomes|assessment|"
    r"classroom|tutoring|advising|educational|education(al)? (practice|research|innovation|intervention)|"
    r"students'? (learning|experience|engagement|progression|belonging|development|feedback)|feedback|course design|"
    r"teacher development|mentoring|peer learning)\b",
    re.I,
)

INQUIRY_PATTERNS = {
    "question": r"\bresearch questions?\b|\bto what extent\b|\bwe (asked|investigated|examined|explored)\b|"
                r"\b(this|the) (study|project|inquiry) (asks|investigates|examines|explores)\b|\bhow (does|do|can|did)\b.*\?|\bhypothes[ie]s\b|\baims? to (investigate|examine|assess|evaluate|explore)\b",
    "method": r"\bmethod(s|ology)?\b|\bsurveys?\b|\bquestionnaires?\b|\binterviews?\b|\bfocus groups?\b|\bpre[-\s]?(and|/)\s*post\b|"
              r"\bcontrol group\b|\bmixed[-\s]methods\b|\bthematic analysis\b|\bcoding\b|\bsampl(e|ing)\b|\brespondents\b|\bparticipants\b",
    "evidence": r"\bdata\b|\bresponses\b|\b\d+\s*(students|respondents|participants)\b|\bn\s*=\s*\d+\b|\bevaluation results\b|\bscores\b",
    "findings": r"\bfindings\b|\bresults (show|showed|indicate|indicated|suggest)\b|\bwe found\b|\bfound that\b|\banalysis (showed|shows|revealed)\b|\bstatistically\b|\bsignificant(ly)? (improv|increas|differ)",
    "use": r"\b(informed|led to|resulted in|used to (revise|redesign|improve|change))\b|\b(revised|redesigned|adjusted|changed) (the )?(course|curriculum|assessment|programme|program|approach|practice)\b|"
           r"\bimplemented (the )?(recommendations|changes)\b|\bsubsequent (practice|iterations?|years?)\b|\bas a result\b",
}

PUBLICATION_RE = re.compile(
    r"\b(article|journal|chapter|monograph|book|edited volume|published|publication|peer[-\s]reviewed|special issue|"
    r"forthcoming|in press|doi|isbn|proceedings)\b",
    re.I,
)
PRESENTATION_RE = re.compile(r"\b(conference|symposium|keynote|panel|paper presented|presented at|presentation|invited talk)\b", re.I)
DISCIPLINARY_RE = re.compile(
    r"\b(literature|literary|poet(ry|ics|s)?|novel(s|ist)?|fiction|film(s)?\b(?!\s+and\s+media\s+studies\s+track)|cinema|beat generation|beats?\b|"
    r"di prima|kerouac|ginsberg|burroughs|ecocriti\w*|environmental humanities|media studies|archiv\w*|semiotic\w*|"
    r"modernis\w*|american studies|cultural studies|countercultur\w*|anthropocene)\b",
    re.I,
)
STUDENT_COAUTHOR_RE = re.compile(r"\b(co[-\s]?author\w*|together|with)\b.{0,40}\b(former )?(student|undergraduate|alumn\w+)\b|\b(student|undergraduate)[-\s](faculty|staff)\s+(research\s+)?collaboration\b", re.I)
QUALIFICATION_RE = re.compile(r"\bteaching qualification\b|\b(SU?TQ|UTQ)\b|\bSKO\b|\bBKO\b|\bUTQ\b|\bcertificate\b|\bcertified\b|\bdiploma\b", re.I)
AWARD_RE = re.compile(r"\b(award(ed)?|prize|nominated|nomination|honou?r(ed)?|fellowship)\b", re.I)
GRANT_RE = re.compile(r"\b(grant(s|ed)?|funding|funded|fund)\b", re.I)
EDU_GRANT_RE = re.compile(r"\b(educational|teaching|education|innovation|comenius|senior fellow|teaching fellow)\b", re.I)
PD_GRANT_RE = re.compile(r"\bprofessional[-\s]development\b", re.I)
PEER_REVIEW_RE = re.compile(r"\b(peer[-\s]review(er|ed|ing)? for|reviewer for|journal reviewer|editor(ial)?\b|edited|advisory roles?|conference organi[sz]ation|organi[sz]ed (international )?(conferences|symposia)|referee for|reviewed (manuscripts|articles|for)|editorial board|external examiner|external reviewer|advisory board|panel member)\b", re.I)
EXTERNAL_RE = re.compile(r"\b(national|international|external(ly)?|other universities|beyond ucr|dutch universities|european)\b", re.I)
GOVERNANCE_RE = re.compile(r"\bworks council\b|\bondernemingsraad\b|\bstaff council\b|\bunion\b|\bemployee (participation|representation)\b", re.I)
REFLECTIVE_RE = re.compile(r"\b(i (learned|learnt|realised|realized|reflect\w*|came to|now see|believe)|my (approach|philosophy|development|aim) |reflect(ion|ive|ing)|looking back|in retrospect|lessons? learned)\b", re.I)
WORK_RE = re.compile(r"\b(handbook|course materials?|syllab(us|i)|curriculum proposal|proposal|policy|polic(ies)|guidelines?|template|rubric|report|training (materials?|sessions?|programme)|workshop|teaching resources?|programme plan|program plan|reader|module|course design|framework|assessment (system|plan|matrix)|advising system|toolkit|website|guide|manual)\b", re.I)
EVAL_RE = re.compile(r"\b(student evaluations?|course evaluations?|evaluation (scores?|results|report)|peer observation|observed|reviewer comments?|formal feedback|accreditation (feedback|panel|report)|committee evaluation|performance review|annual review|appraisal|p&d|r&o|mean score|average score|rated|satisfaction)\b", re.I)
USE_RE = re.compile(r"\b(implemented|adopted|in use|continue[sd]? to be used|still used|rolled out|became (standard|established|the norm)|established practice|used by (colleagues|all|other)|embedded in|institutionali[sz]ed|now used|has been used|standard practice|taken up|incorporated into)\b", re.I)
RECOGNITION_RE = re.compile(r"\b(award(ed)?|prize|competitive|invited|keynote|selected|fellowship|nominated|external adoption|grant(ed)?)\b", re.I)
INTENT_RE = re.compile(
    r"\b(I|we)\s+(will|would|shall|plan to|intend to|hope to|aim to|seek to|expect to|look forward to|can imagine|foresee)\b"
    r"|\bif (appointed|selected|successful)\b|\bmy (basic )?idea is to\b|\bthe (ambitious )?goal of (my|this) project\b|\b(this|the) (project|intervention|course|programme|program) (will|seeks to|aims to)\b",
    re.I,
)
COURSE_DEV_RE = re.compile(r"\b(develop|design|creat|build|buil)\w*\b[^.;]{0,60}\bcourses?\b|\bcourse creator\b", re.I)
BROAD_REACH_RE = re.compile(r"\bacross (ucr|the college|the curriculum|departments|clusters|programmes|programs)\b|\b(ucr|college|curriculum)[-\s]wide\b", re.I)
SELF_ASSESSMENT_RE = re.compile(r"\blevel\s*3\s*[ab]?\b|\bL3[AB]?\b|\b(3A|3B) criteria\b", re.I)
ACTIVITY_RE = re.compile(
    r"\b(taught|teach(es|ing)?|lectur\w+|tutor(ed|ing|s)?|advis(ed|ing|or|ors)|supervis\w+|mentor\w*|guided|coordinat\w+|"
    r"grad(ed|ing)|assess(ed|ing)|design(ed|ing)|develop(ed|ing)|organi[sz]ed|presented|evaluat\w+|served|chair\w*|managed|led)\b",
    re.I,
)
PAST_ACTION_RE = re.compile(r"(ed|\bled|oversaw|wrote|built|set up|rolled out|began|ran)$", re.I)
FIRST_PERSON_RE = re.compile(r"\b(I|my|me)\b")
SECOND_PERSON_RE = re.compile(r"\b(you|your)\b", re.I)


@dataclass
class Signals:
    domain_scores: dict[int, int] = field(default_factory=dict)
    action: bool = False
    action_count: int = 0
    scope: bool = False
    membership_only: bool = False
    leadership_word: bool = False
    coordination: bool = False
    senior_title: bool = False
    edu_object: bool = False
    inquiry: set[str] = field(default_factory=set)
    publication: bool = False
    presentation: bool = False
    disciplinary: bool = False
    student_coauthor: bool = False
    qualification: bool = False
    award: bool = False
    grant: bool = False
    edu_grant: bool = False
    pd_grant: bool = False
    peer_review: bool = False
    external: bool = False
    governance: bool = False
    intent_only: bool = False  # states intentions or plans without a completed action
    completed_action: bool = False
    course_development: bool = False
    broad_reach: bool = False
    self_assessment: bool = False
    activity: bool = False
    heading: bool = False
    first_person: bool = False
    second_person: bool = False
    types: set[str] = field(default_factory=set)

    @property
    def total_domain_score(self) -> int:
        return sum(self.domain_scores.values())


def compute(text: str) -> Signals:
    s = Signals()
    s.domain_scores = domain_scores(text)
    actions = ACTION_RE.findall(text)
    s.action_count = len(actions)
    s.action = s.action_count > 0
    completed = any(PAST_ACTION_RE.search(m.group(0)) for m in ACTION_RE.finditer(text))
    s.completed_action = completed
    s.intent_only = bool(INTENT_RE.search(text)) and not completed
    s.course_development = bool(COURSE_DEV_RE.search(text))
    s.broad_reach = bool(BROAD_REACH_RE.search(text))
    s.self_assessment = bool(SELF_ASSESSMENT_RE.search(text))
    s.activity = bool(ACTIVITY_RE.search(text))
    words = [w for w in re.findall(r"[A-Za-z][\w'-]*", text) if len(w) > 3]
    s.heading = (len(text) < 90 and "\n" not in text.strip() and not re.search(r"[.:;]", text) and not YEAR_RE.search(text)
                 and bool(words) and sum(w[0].isupper() for w in words) / len(words) >= 0.6)
    s.scope = bool(SCOPE_RE.search(text))
    s.leadership_word = bool(LEADERSHIP_WORD_RE.search(text))
    s.membership_only = bool(MEMBERSHIP_RE.search(text)) and not s.leadership_word and s.action_count == 0
    s.coordination = bool(COORDINATION_RE.search(text))
    s.senior_title = bool(SENIOR_TITLE_RE.search(text))
    s.edu_object = bool(EDU_OBJECT_RE.search(text))
    s.inquiry = {k for k, pat in INQUIRY_PATTERNS.items() if re.search(pat, text, re.I)}
    s.publication = bool(PUBLICATION_RE.search(text))
    s.presentation = bool(PRESENTATION_RE.search(text))
    s.disciplinary = bool(DISCIPLINARY_RE.search(text))
    s.student_coauthor = bool(STUDENT_COAUTHOR_RE.search(text))
    s.qualification = bool(QUALIFICATION_RE.search(text))
    s.award = bool(AWARD_RE.search(text))
    s.grant = bool(GRANT_RE.search(text))
    s.edu_grant = s.grant and bool(EDU_GRANT_RE.search(text))
    s.pd_grant = s.grant and bool(PD_GRANT_RE.search(text))
    s.peer_review = bool(PEER_REVIEW_RE.search(text))
    s.external = bool(EXTERNAL_RE.search(text))
    s.governance = bool(GOVERNANCE_RE.search(text))
    s.first_person = bool(FIRST_PERSON_RE.search(text))
    s.second_person = bool(SECOND_PERSON_RE.search(text))
    if REFLECTIVE_RE.search(text):
        s.types.add("REFLECTIVE")
    if WORK_RE.search(text):
        s.types.add("W")
    if EVAL_RE.search(text):
        s.types.add("E")
    if USE_RE.search(text):
        s.types.add("U")
    if RECOGNITION_RE.search(text) and (s.award or s.grant or s.external or "invited" in text.lower()):
        s.types.add("R")
    return s


def educational_inquiry(s: Signals) -> bool:
    """True when the passage contains an educational question or inquiry
    markers about an educational object, as opposed to disciplinary work."""
    return s.edu_object and "question" in s.inquiry


def surname(name: str) -> str:
    parts = [p for p in re.split(r"\s+", name.strip()) if p and not p.endswith(".")]
    return parts[-1] if parts else ""


def mentions_person(text: str, candidate_name: str) -> bool:
    if not candidate_name.strip():
        return False
    last = surname(candidate_name)
    if len(last) < 3:
        return False
    return bool(re.search(rf"\b{re.escape(last)}\b", text, re.I))
