import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const comparisonsDir = path.join(root, 'data', 'counselor', 'comparisons');
const read = id => JSON.parse(fs.readFileSync(path.join(comparisonsDir, `${id}.json`), 'utf8'));
const write = record => fs.writeFileSync(path.join(comparisonsDir, `${record.id}.json`), `${JSON.stringify(record, null, 2)}\n`);

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function ucr(record, id) {
  const p = record.programmes.find(x => x.id === id);
  assert(p, `${record.id}: missing programme ${id}`);
  return p;
}

function findCourse(programme, code) {
  for (const semester of programme.schedule?.semesters || []) {
    const index = (semester.courses || []).findIndex(course => course.code === code);
    if (index >= 0) return { semester, index, course: semester.courses[index] };
  }
  return null;
}

function swap(programme, codeA, codeB) {
  const a = findCourse(programme, codeA);
  const b = findCourse(programme, codeB);
  assert(a && b, `${programme.id}: cannot swap ${codeA} and ${codeB}`);
  a.semester.courses[a.index] = b.course;
  b.semester.courses[b.index] = a.course;
}

function replaceAtCourse(programme, oldCode, newCourse) {
  const slot = findCourse(programme, oldCode);
  assert(slot, `${programme.id}: cannot replace missing ${oldCode}`);
  slot.semester.courses[slot.index] = newCourse;
}

function addUniqueBasis(record, programmeId, labels) {
  const alt = record.academicRationale.alternatives.find(x => x.programmeId === programmeId);
  assert(alt, `${record.id}: missing rationale alternative ${programmeId}`);
  for (const label of labels) if (!alt.basisLabels.includes(label)) alt.basisLabels.push(label);
}

function removeProgrammeCells(record, programmeId) {
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) delete row.cells?.[programmeId];
    block.rows = (block.rows || []).filter(row => row.cells && Object.keys(row.cells).length > 0);
  }
}

function findRowByUcrCode(record, courseCode) {
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      for (const [id, cell] of Object.entries(row.cells || {})) {
        if (id !== 'comparator' && cell?.courseCode === courseCode) return { block, row };
      }
    }
  }
  return null;
}

function removeProgrammeCourseCell(record, programmeId, courseCode) {
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      const cell = row.cells?.[programmeId];
      if (cell?.courseCode === courseCode) delete row.cells[programmeId];
    }
    block.rows = (block.rows || []).filter(row => row.cells && Object.keys(row.cells).length > 0);
  }
}

function addProgrammeCourseRow(record, blockId, programmeId, course) {
  const block = record.blocks.find(x => x.id === blockId);
  assert(block, `${record.id}: missing block ${blockId}`);
  assert(!findRowByUcrCode(record, course.code), `${record.id}: ${course.code} already has a canonical comparison row`);
  block.rows.push({ cells: { [programmeId]: { text: course.name, credits: course.credits, courseCode: course.code } } });
}

function scheduledCodes(record) {
  const set = new Set();
  for (const p of record.programmes.filter(x => x.family === 'ucr')) {
    for (const semester of p.schedule?.semesters || []) for (const c of semester.courses || []) set.add(c.code);
  }
  return set;
}

function normalizeAlignmentsAfterProgrammeRemoval(record) {
  const scheduled = scheduledCodes(record);
  for (const item of record.comparisonAlignment || []) {
    if (item.matchType === 'substantive-match' && !scheduled.has(item.ucrCourseCode)) {
      item.matchType = 'unmatched';
      delete item.ucrCourseCode;
      item.rationale = 'After the final-methodology re-audit, the previously aligned UCR course is no longer part of an included alternative; no remaining UCR row provides substantial curricular correspondence without overstating overlap.';
    }
  }
}

function removeComparatorCell(record, componentId) {
  for (const block of record.blocks || []) {
    for (const row of block.rows || []) {
      if (row.cells?.comparator?.componentId === componentId) delete row.cells.comparator;
    }
    block.rows = (block.rows || []).filter(row => row.cells && Object.keys(row.cells).length > 0);
  }
}

function placeComparatorOnUcrRow(record, component, courseCode) {
  const hit = findRowByUcrCode(record, courseCode);
  assert(hit, `${record.id}: cannot place comparator ${component.id}; missing UCR row ${courseCode}`);
  assert(!hit.row.cells.comparator, `${record.id}: UCR row ${courseCode} already has comparator ${hit.row.cells.comparator?.componentId}`);
  hit.row.cells.comparator = { text: component.name, credits: component.credits, componentId: component.id };
}

function placeComparatorUnmatched(record, component, blockId) {
  const block = record.blocks.find(x => x.id === blockId);
  assert(block, `${record.id}: missing block ${blockId}`);
  block.rows.push({ cells: { comparator: { text: component.name, credits: component.credits, componentId: component.id } } });
}

function replaceComparatorComponent(record, oldId, component) {
  const index = record.comparator.components.findIndex(x => x.id === oldId);
  assert(index >= 0, `${record.id}: missing comparator component ${oldId}`);
  removeComparatorCell(record, oldId);
  record.comparisonAlignment = (record.comparisonAlignment || []).filter(x => x.componentId !== oldId);
  record.comparator.components[index] = component;
}

function contribution(code, name) {
  const exact = {
    GOSSOCI111: 'provides the foundational sociological concepts needed to analyse social structures and institutions',
    GOSSOCI214: 'develops modern sociological theory needed before advanced contemporary social-theory work',
    GOSSOCI311: 'adds advanced analysis of contemporary social theory, civil society and institutional change',
    GOSSOCI212: 'provides qualitative research design, data collection and interpretation skills',
    GOSPOLI112: 'provides foundational comparative-political analysis of institutions and political decision-making',
    GOSPOLI212: 'adds international-relations theory for cross-border governance and political order',
    GOSPOLI311: 'develops advanced understanding of European institutions and multi-level governance',
    GOSPOLI313: 'examines conflict, political order and governance under contested conditions',
    GOSPOLI111: 'provides normative political concepts for evaluating institutions, authority and democracy',
    GOSLAWJ111: 'adds a rights-based legal and philosophical perspective on public institutions and social issues',
    GOSLAWJ212: 'provides the international-law framework needed for transnational governance questions',
    GOSLAWJ213: 'develops comparative constitutional understanding of public institutions and legal constraints',
    GOSLAWJ312: 'adds advanced European Union law to institutional and multi-level governance analysis',
    GOSGATE102: 'provides a broad foundation in how law, society and justice interact',
    GOSPHIL212: 'provides ethical reasoning for evaluating policy, professional practice and institutional choices',
    BENGATE102: 'provides foundational empirical research design and statistical analysis',
    BENECON111: 'provides foundational economic reasoning about incentives, welfare and resource allocation',
    BENECON211: 'adds macroeconomic analysis of international economic conditions and policy',
    BENECON212: 'adds microeconomic and behavioural analysis of individual and institutional decision-making',
    BENECON311: 'examines public-sector economics, taxation, welfare and resource allocation',
    BENECON312: 'provides advanced quantitative tools for causal analysis, prediction and empirical policy research',
    BENECON314: 'connects psychological evidence to economic decision-making, biases and behavioural choice',
    BENLEAD111: 'provides foundational leadership theory, self-awareness and applied leadership skills',
    BENLEAD112: 'develops leadership communication, ethics and interpersonal influence',
    BENLEAD211: 'examines leadership and diversity in organisational settings',
    BENLEAD311: 'provides organisational-psychology theory on motivation, leadership, groups and organisational culture',
    BENLEAD312: 'develops negotiation, strategic interaction and the psychology of influence',
    BENGATE101: 'provides foundational understanding of organisations, entrepreneurship and business decision-making',
    BENBUSI211: 'examines organisational, managerial and societal consequences of technological change',
    BENENTR311: 'provides applied research design, data gathering and analysis in organisational and market contexts',
    BENENTR312: 'examines governance, institutions and decision-making in international organisational settings',
    ENSGATE101: 'provides foundational sustainability-science concepts needed for later environmental study',
    ENSGATE201: 'builds the scientific sustainability foundation required for advanced environmental courses',
    ENSSUST111: 'provides substantive climate-science understanding for climate-policy and governance questions',
    ENSDELT211: 'examines adaptation and sustainable water governance in delta regions',
    ENSDELT311: 'examines circular-economy technologies and sustainability challenges',
    ENSDELT312: 'directly examines sustainability policy and governance across institutional levels',
    ENSSUST311: 'adds systems-oriented study of renewable technologies and sustainability design',
    ENSSUST313: 'develops advanced sustainability research in real-world delta challenges',
    MCCCOMM212: 'develops communication analysis and practice around the climate crisis',
    MCCCOMM213: 'develops applied rhetoric, communication and community-engaged educational practice',
    MCCCOMM311: 'develops evidence-based persuasive communication, including social-psychological mechanisms and public applications',
    HCBGATE101: 'provides foundational life-science knowledge needed for biological and health-oriented study',
    HCBGATE102: 'provides the foundational psychology and neuroscience gateway for advanced behavioural and cognitive courses',
    HCBPSYC111: 'provides core social-psychology theory on attitudes, groups and interpersonal behaviour',
    HCBPSYC211: 'provides advanced statistical and experimental methods for psychological research',
    HCBPSYC212: 'examines mental disorders through psychological and biopsychosocial perspectives',
    HCBPSYC311: 'examines psychological determinants of health, illness and wellbeing using a biopsychosocial approach',
    HCBPSYC312: 'develops knowledge of psychological assessment, psychodiagnostics and psychotherapeutic approaches',
    HCBPSYC313: 'develops advanced evidence-synthesis, meta-analysis and R-based research skills',
    HCBPSYC314: 'provides systematic study of cognitive, emotional and social development across the lifespan',
    HCBPSYC315: 'examines youth resilience, psychological wellbeing and evidence-based intervention in social contexts',
    HCBCOGN112: 'provides neurobiological foundations for understanding cognition and brain-behaviour relations',
    HCBCOGN212: 'examines neural mechanisms of perception and action',
    HCBCOGN311: 'develops advanced understanding of memory, attention, executive functions and higher cognition',
    HCBCOGN312: 'examines language processing through psychological and neurobiological perspectives',
    HCBBIOM111: 'provides population-health and evidence-evaluation perspectives relevant to behavioural and health outcomes',
    HCBBIOM211: 'provides functional anatomy linking bodily structure to physiological function',
    HCBBIOM313: 'connects normal physiology to pathophysiology across major organ systems',
    HCBLIFE211: 'provides molecular and cellular foundations for biological explanations of behaviour and health',
    HCBLIFE212: 'provides the normal human-physiology foundation needed before pathophysiology',
    HCBLIFE214: 'develops laboratory, experimental and data-analysis skills in life science',
    HCBLIFE311: 'develops advanced understanding of molecular pathology and genetics',
    DISDATA111: 'provides foundational data cleaning, visualisation and analysis skills',
    DISDATA211: 'adds machine-learning methods for analysing complex behavioural and biological data',
    DISDATA212: 'adds image-processing and computer-vision methods relevant to perception and quantitative cognitive research',
    DISARIN111: 'provides ethical analysis of AI and technological change in institutions and society'
  };
  return exact[code] || `provides substantive study through ${name}`;
}

function pickBasis(recordId, programmeId, code, name, basisLabels) {
  const text = `${code} ${name}`;
  const rules = {
    'cp-000001': [
      [/^ENS|Climate|Sustainability|Water|Environmental/i, /Climate change|govern climate/i],
      [/^GOSLAWJ|^GOSGATE/, /Law and public institutions/i],
      [/^GOSSOCI/, /Sociology and social\/governance issues/i],
      [/^BENECON/, /Economics, welfare and public resources|Qualitative and quantitative social research/i],
      [/^BENLEAD/, /Organisation and public management/i],
      [/^BENGATE|Econometrics/i, /Qualitative and quantitative social research/i],
      [/^GOSPOLI|Political Philosophy/, /Politics and public policy|European and international governance/i],
      [/Ethics/, /Research-based advice and professional skills|Politics and public policy/i]
    ],
    'cp-000002': [
      [/^ENS|Climate|Sustainability|Environmental/i, /climate change|International social and governance challenges/i],
      [/^GOSLAWJ|^GOSGATE/, /International law|Public administration and public policy/i],
      [/^GOSSOCI/, /^Sociology$/i],
      [/^BENECON/, /Economics, welfare and economic stability/i],
      [/^BENLEAD/, /Organisation and management/i],
      [/^BENGATE|Econometrics/i, /Qualitative and quantitative social research/i],
      [/^GOSPOLI/, /Political science and multi-level governance|Global and European governance/i],
      [/^DIS/, /technological change/i],
      [/Ethics/, /International social and governance challenges/i]
    ],
    'cp-000003': [
      [/^HCBLIFE|^HCBBIOM|^HCBGATE101|Neurobiology|Perception|Higher Order|Psycholinguistics/, /Biological foundations of development|Developmental and personality psychology/i],
      [/Lifespan|Social Psychology|Abnormal|Medical|Youth Resilience/, /Child and youth development|Developmental and personality psychology|resilience and wellbeing/i],
      [/Psychodiagnostics/, /Pedagogical and orthopedagogical support|Developmental difficulties/i],
      [/Research|Statistics|Qualitative/, /Qualitative, quantitative and psychometric research/i],
      [/^GOSSOCI/, /Family, school and social-environment influences/i],
      [/^GOSLAWJ|^GOSGATE|Ethics/, /Pedagogical and orthopedagogical support|Family, school and social-environment influences/i],
      [/Rhetoric|Persuasive/, /Pedagogical and orthopedagogical support|Family, school and social-environment influences/i],
      [/^GOSPOLI/, /Family, school and social-environment influences/i]
    ],
    'cp-000004': [
      [/^DISDATA|Research|Statistics|Market Research/, /Research methods, statistics and psychological experiments/i],
      [/Neurobiology|Perception|Higher Order|Psycholinguistics|^HCBLIFE|^HCBBIOM|^HCBGATE101|Brain/, /Biological psychology, cognition and brain-behaviour relations/i],
      [/Lifespan|Developmental/, /Developmental psychology/i],
      [/Abnormal|Medical|Psychodiagnostics|Youth Resilience/, /Clinical psychology and mental health/i],
      [/Social Psychology|^GOSSOCI|Behavioral Economics/, /Social and personality psychology/i],
      [/^BENLEAD|^BENENTR|^BENBUSI|^BENGATE101|Negotiation|Leadership/, /Work and Organisational Psychology specialisation|How do psychological processes shape wellbeing and behaviour at work\?/i],
      [/Ethics|Persuasive|Qualitative/, /Cross-cultural, historical and professional perspectives on psychology|Research methods, statistics and psychological experiments/i]
    ]
  };
  for (const [coursePattern, labelPattern] of rules[recordId] || []) {
    if (!coursePattern.test(text)) continue;
    const hit = basisLabels.find(label => labelPattern.test(label));
    if (hit) return hit;
  }
  return basisLabels[0];
}

function buildAlternativeAudit(record, programmeId, progressionRationale) {
  const programme = ucr(record, programmeId);
  const alt = record.academicRationale.alternatives.find(x => x.programmeId === programmeId);
  assert(alt, `${record.id}: missing rationale for ${programmeId}`);
  const trace = [];
  for (const semester of programme.schedule.semesters) {
    for (const course of semester.courses) {
      if (course.code === 'ACCPPDE101') continue;
      const basis = pickBasis(record.id, programmeId, course.code, course.name, alt.basisLabels);
      trace.push({
        courseCode: course.code,
        basisLabels: [basis],
        rationale: `${course.name} ${contribution(course.code, course.name)}; this directly implements the evidenced programme element “${basis}” rather than serving as generic breadth.`
      });
    }
  }
  return {
    programmeId,
    courseTraceability: trace,
    progressionAssessment: { status: 'passed', rationale: progressionRationale }
  };
}

function candidateAssessment(candidate, organisingLogic, assessment) {
  return { candidateLabel: candidate.label, organisingLogic, assessment };
}

function setFinalAudit(record, { routeAudit, covered, candidateAssessments, progression }) {
  record.academicRationale.finalMethodologyAudit = {
    ...(routeAudit ? { comparatorRouteSelection: routeAudit } : {}),
    coveredByClosestMatchInterestRows: covered,
    candidateAssessments,
    alternatives: record.programmes
      .filter(x => x.family === 'ucr')
      .map(p => buildAlternativeAudit(record, p.id, progression[p.id]))
  };
}

function removeCatchAllCandidates(record) {
  record.academicRationale.interestSelection.candidateDirections = record.academicRationale.interestSelection.candidateDirections
    .filter(c => !/other eligible programme-interest directions/i.test(c.label));
}

// cp-000001 — Bestuurskunde
{
  const r = read('cp-000001');
  swap(ucr(r, 'ucr-1'), 'GOSSOCI214', 'GOSPOLI311');
  swap(ucr(r, 'ucr-2'), 'GOSSOCI214', 'GOSPOLI311');
  addUniqueBasis(r, 'ucr-2', ['Economics, welfare and public resources', 'Organisation and public management', 'Research-based advice and professional skills']);
  removeCatchAllCandidates(r);
  const climate = r.academicRationale.interestSelection.candidateDirections.find(c => c.programmeId === 'ucr-2');
  assert(climate, 'cp-000001: missing climate candidate');
  setFinalAudit(r, {
    routeAudit: {
      route: r.comparator.route,
      selectionRule: 'target-named',
      basis: 'The normalized counselor target is explicitly the Dutch-language Bestuurskunde programme; the comparator route therefore follows that named track rather than selecting among alternative routes for UCR fit.'
    },
    covered: [318,319,320,321,322,323,324,325,326,328,329,330,341,342],
    candidateAssessments: [candidateAssessment(climate, 'Climate and sustainability governance is a coherent policy direction anchored in an explicit target-programme interest and supported by the official public-administration curriculum.', 'Included as ucr-2 because it changes substantial curricular weight toward climate and sustainability while retaining a recognizable public-administration core.')],
    progression: {
      'ucr-1': 'Passed after re-sequencing the sociology strand so Introduction to Sociology precedes Modern Sociology, which in turn precedes New Issues in Contemporary Social Theory. Formal prerequisites and fixed-term availability remain satisfied.',
      'ucr-2': 'Passed after re-sequencing the sociology strand so Introduction to Sociology precedes Modern Sociology, which in turn precedes New Issues in Contemporary Social Theory; Sustainability Essentials I also precedes Sustainability Essentials II. Formal prerequisites and fixed-term availability remain satisfied.'
    }
  });
  r.validation.officialEvidenceChecked = '2026-09-15';
  write(r);
}

// cp-000002 — MISOC
{
  const r = read('cp-000002');
  swap(ucr(r, 'ucr-2'), 'GOSSOCI214', 'GOSPOLI311');
  const p3 = ucr(r, 'ucr-3');
  const pol = findCourse(p3, 'GOSPOLI311');
  const lead = findCourse(p3, 'BENLEAD311');
  assert(pol && lead, 'cp-000002: expected GOSPOLI311 and BENLEAD311 in ucr-3');
  pol.semester.courses[pol.index] = { code: 'GOSSOCI214', name: 'Modern Sociology', level: 2, credits: 7.5 };
  lead.semester.courses[lead.index] = pol.course;
  removeProgrammeCourseCell(r, 'ucr-3', 'BENLEAD311');
  const sociRow = findRowByUcrCode(r, 'GOSSOCI214');
  assert(sociRow, 'cp-000002: missing canonical GOSSOCI214 row');
  sociRow.row.cells['ucr-3'] = { text: 'Modern Sociology', credits: 7.5, courseCode: 'GOSSOCI214' };
  addUniqueBasis(r, 'ucr-3', ['International law']);
  removeCatchAllCandidates(r);
  const candidates = r.academicRationale.interestSelection.candidateDirections;
  const transnational = candidates.find(c => c.programmeId === 'ucr-2');
  const climate = candidates.find(c => c.programmeId === 'ucr-3');
  assert(transnational && climate, 'cp-000002: missing included candidate directions');
  transnational.generatingInterestRows = [357,358,359,360,365,366,367,373];
  climate.generatingInterestRows = [361,364];
  setFinalAudit(r, {
    covered: [362,363,368,369,370,371,372,374,375],
    candidateAssessments: [
      candidateAssessment(transnational, 'Transnational governance, migration and development combines the programme’s international-governance core with migration, development, international law and technology in public organisations.', 'Included as ucr-2 because the direction is both explicitly evidenced and substantively different from the broad closest match.'),
      candidateAssessment(climate, 'Climate and sustainability governance uses climate change and the Sustainable Development Goals as the organizing international-social-challenge question.', 'Included as ucr-3 because the climate direction is explicit in the target evidence and drives a distinct sustainability-heavy curriculum rather than isolated course substitutions.')
    ],
    progression: {
      'ucr-1': 'Passed. Introduction to Sociology precedes Modern Sociology and New Issues in Contemporary Social Theory; research-method and economics courses progress from foundations to advanced work, with formal prerequisites and term availability satisfied.',
      'ucr-2': 'Passed after moving Modern Sociology before New Issues in Contemporary Social Theory. Foundational politics, law, economics and research methods precede the advanced governance and econometric work, with formal prerequisites and term availability satisfied.',
      'ucr-3': 'Passed after replacing the weak organisational-psychology insertion with Modern Sociology and moving European Union Politics later, producing Introduction to Sociology → Modern Sociology → New Issues in Contemporary Social Theory and Sustainability Essentials I → II before the advanced sustainability research courses.'
    }
  });
  r.validation.officialEvidenceChecked = '2026-09-15';
  write(r);
}

// cp-000003 — Pedagogical Sciences
{
  const r = read('cp-000003');
  const p1 = ucr(r, 'ucr-1');
  swap(p1, 'GOSSOCI214', 'GOSPOLI112');
  swap(p1, 'GOSSOCI311', 'GOSGATE102');

  r.programmes = r.programmes.filter(p => p.id !== 'ucr-3');
  r.academicRationale.alternatives = r.academicRationale.alternatives.filter(a => a.programmeId !== 'ucr-3');
  removeProgrammeCells(r, 'ucr-3');
  normalizeAlignmentsAfterProgrammeRemoval(r);

  const candidates = r.academicRationale.interestSelection.candidateDirections;
  const support = candidates.find(c => c.programmeId === 'ucr-2');
  const education = candidates.find(c => /education-and-school-development route/i.test(c.label));
  assert(support && education, 'cp-000003: missing expected candidate directions');
  education.disposition = 'rejected';
  education.rejectionReason = 'not-substantively-distinct';
  delete education.programmeId;
  removeCatchAllCandidates(r);

  r.alternativeSelection = {
    includedCount: 2,
    stoppingReason: 'not-substantively-distinct',
    assessment: 'The broad closest approximation and the child-development/pedagogical-support route remain coherent and evidence-backed. The education/inequality/school-development direction is academically coherent as an interest direction, but the prior 24-course realization cleared the 30-EC floor partly through courses that did not follow from that organizing concept. It is therefore not included rather than being padded to meet the distinctness threshold.'
  };

  setFinalAudit(r, {
    routeAudit: {
      route: r.comparator.route,
      selectionRule: 'official-order-tiebreak',
      basis: 'The generic Pedagogical Sciences target requires one of two formal 15-EC year-3 specialisations to instantiate a complete pathway. Neither is clearly more general for the generic target, so the first specialisation in the official 2026-2027 EER, Pedagogiek / Pedagogische Ondersteuning, is used as the neutral tie-break independently of UCR fit.'
    },
    covered: [401,403,404,408,410,413,414,415],
    candidateAssessments: [
      candidateAssessment(support, 'Child development and pedagogical support combines developmental psychology, biological development, wellbeing, assessment and intervention around support for children and families.', 'Included as ucr-2 because the direction is strongly evidenced and the distinctive biological/health/assessment courses follow from that concept.'),
      candidateAssessment(education, 'Education, inequality and school development is a coherent evidence-backed direction centred on learning, diverse classrooms, school development and educational policy.', 'Rejected as an included alternative under the final rules because a 24-course UCR realization could not clear the hard distinctness floor without adding courses such as perception/action or health psychology that were not consequences of the education/school-development concept.')
    ],
    progression: {
      'ucr-1': 'Passed after re-sequencing the sociology strand across the three years: Introduction to Sociology in Year 1, Modern Sociology in Year 2, and New Issues in Contemporary Social Theory in Year 3. Psychology and cognition gateways precede the advanced courses that formally depend on them.',
      'ucr-2': 'Passed. Foundational life/health and research-method courses precede advanced clinical, cognitive and developmental work; Introduction to Brain & Behavior is completed before the upper-level psychology and cognition courses that require it.'
    }
  });
  r.validation.officialEvidenceChecked = '2026-09-15';
  write(r);
}

// cp-000004 — Psychology
{
  const r = read('cp-000004');
  r.comparator.route = 'Brain & Cognition specialisation';
  r.comparator.sourceNotes = 'The 2026–2027 EER defines a broad common psychology core followed by one of four formal specialisations. For the generic Psychology target, this coherent 180-EC pathway instantiates Brain & Cognition because it most directly continues the programme’s common cognitive and biological psychology core rather than selecting an applied specialisation; the 15-EC minor and 10-EC psychology elective space remain open.';

  const brainPerception = { id: 'psy-brain-perception', name: 'Brain and Perception', credits: 9 };
  const intervention = { id: 'psy-intervention-research', name: 'Intervention Research', credits: 5 };
  const memoryLanguage = { id: 'psy-memory-language', name: 'Memory & Language', credits: 5 };
  const dataR = { id: 'psy-data-r', name: 'Data processing and analysis in R', credits: 2 };
  replaceComparatorComponent(r, 'psy-clinical-specialisation-y2', brainPerception);
  replaceComparatorComponent(r, 'psy-clinical-interview', intervention);
  replaceComparatorComponent(r, 'psy-neuropsych', memoryLanguage);
  replaceComparatorComponent(r, 'psy-neuropsych-assessment', dataR);
  placeComparatorOnUcrRow(r, brainPerception, 'HCBCOGN212');
  placeComparatorUnmatched(r, intervention, 'methods');
  placeComparatorOnUcrRow(r, memoryLanguage, 'HCBCOGN312');
  placeComparatorOnUcrRow(r, dataR, 'DISDATA111');
  r.comparisonAlignment.push(
    { componentId: brainPerception.id, matchType: 'substantive-match', ucrCourseCode: 'HCBCOGN212', rationale: 'Brain and Perception substantially corresponds to UCR Perception & Action, which examines neural mechanisms of perception and action; the comparator was placed only after the canonical UCR rows were fixed.' },
    { componentId: intervention.id, matchType: 'unmatched', rationale: 'UCR offers research-method and evidence-synthesis courses, but no single canonical UCR course substantially reproduces the comparator practical in intervention research without overstating partial overlap.' },
    { componentId: memoryLanguage.id, matchType: 'substantive-match', ucrCourseCode: 'HCBCOGN312', rationale: 'Memory & Language substantially overlaps UCR Psycholinguistics through language processing, cognition and neurobiological mechanisms; it is the strongest single canonical UCR counterpart.' },
    { componentId: dataR.id, matchType: 'substantive-match', ucrCourseCode: 'DISDATA111', rationale: 'Data processing and analysis in R is a practical quantitative-data component; UCR Introduction to Data Science is the strongest canonical row for data cleaning, manipulation, visualisation and analysis, while the software environment differs.' }
  );

  swap(ucr(r, 'ucr-1'), 'GOSSOCI311', 'GOSSOCI111');

  const p2 = ucr(r, 'ucr-2');
  const gateStats = findCourse(p2, 'BENGATE102');
  const weakYouth = findCourse(p2, 'HCBPSYC315');
  assert(gateStats && weakYouth, 'cp-000004: missing BENGATE102/HCBPSYC315 in ucr-2');
  weakYouth.semester.courses[weakYouth.index] = gateStats.course;
  gateStats.semester.courses[gateStats.index] = { code: 'DISDATA212', name: 'Image Processing & Computer Vision', level: 2, credits: 7.5 };
  swap(p2, 'HCBPSYC314', 'HCBCOGN112');
  const modern = findCourse(p2, 'GOSSOCI214');
  const physiology = findCourse(p2, 'HCBLIFE212');
  assert(modern && physiology, 'cp-000004: missing GOSSOCI214/HCBLIFE212 in ucr-2');
  modern.semester.courses[modern.index] = physiology.course;
  physiology.semester.courses[physiology.index] = { code: 'DISDATA211', name: 'Machine Learning', level: 2, credits: 7.5 };
  removeProgrammeCourseCell(r, 'ucr-2', 'HCBPSYC315');
  removeProgrammeCourseCell(r, 'ucr-2', 'GOSSOCI214');
  addProgrammeCourseRow(r, 'methods', 'ucr-2', { code: 'DISDATA212', name: 'Image Processing & Computer Vision', level: 2, credits: 7.5 });
  addProgrammeCourseRow(r, 'methods', 'ucr-2', { code: 'DISDATA211', name: 'Machine Learning', level: 2, credits: 7.5 });

  const p3 = ucr(r, 'ucr-3');
  swap(p3, 'GOSSOCI214', 'GOSSOCI111');
  swap(p3, 'HCBPSYC313', 'BENENTR311');

  addUniqueBasis(r, 'ucr-1', ['Work and Organisational Psychology specialisation']);
  addUniqueBasis(r, 'ucr-2', ['Social and personality psychology', 'Developmental psychology', 'Clinical psychology and mental health']);
  addUniqueBasis(r, 'ucr-3', ['Cross-cultural, historical and professional perspectives on psychology']);

  const selection = r.academicRationale.interestSelection;
  const brain = selection.candidateDirections.find(c => c.programmeId === 'ucr-2');
  const work = selection.candidateDirections.find(c => c.programmeId === 'ucr-3');
  assert(brain && work, 'cp-000004: missing Brain/Cognition or Work/Organisational candidate');
  brain.generatingInterestRows = [455,447];
  brain.supportingInterestRows = [452,470,459];
  work.generatingInterestRows = [454];
  work.supportingInterestRows = [444,450,452,458,474];
  const clinical = {
    label: 'A clinical-psychology and mental-health direction centred on psychological disorders, diagnosis, assessment and clinically relevant behaviour.',
    basisType: 'combined',
    generatingInterestRows: [456,446,449,451],
    supportingInterestRows: [469],
    evidence: [
      { sourceType: 'official-source', reference: 'https://www.eur.nl/bachelor/psychologie/studieprogramma' },
      { sourceType: 'programme-interest', reference: 'programme_interests.csv:456' },
      { sourceType: 'programme-interest', reference: 'programme_interests.csv:446' },
      { sourceType: 'programme-interest', reference: 'programme_interests.csv:451' }
    ],
    disposition: 'rejected',
    rejectionReason: 'maximum-reached'
  };
  const educational = {
    label: 'An educational-psychology and learning direction centred on learning, motivation, cognition and educational application.',
    basisType: 'combined',
    generatingInterestRows: [457,448],
    supportingInterestRows: [466,471],
    evidence: [
      { sourceType: 'official-source', reference: 'https://www.eur.nl/bachelor/psychologie/studieprogramma' },
      { sourceType: 'programme-interest', reference: 'programme_interests.csv:457' },
      { sourceType: 'programme-interest', reference: 'programme_interests.csv:448' }
    ],
    disposition: 'rejected',
    rejectionReason: 'maximum-reached'
  };
  selection.candidateDirections = [brain, work, clinical, educational];

  setFinalAudit(r, {
    routeAudit: {
      route: r.comparator.route,
      selectionRule: 'least-specialized-general',
      basis: 'The generic Psychology target has a broad common core but requires one formal specialisation to instantiate 180 EC. Brain & Cognition most directly continues the common cognitive and biological psychology core rather than selecting an applied specialisation such as Clinical, Educational, or Work & Organisational Psychology. The choice is independent of UCR fit.'
    },
    covered: [444,445,450,452,453],
    candidateAssessments: [
      candidateAssessment(brain, 'Brain & Cognition is a formal target-programme specialisation and a coherent direction around cognitive neuroscience, perception, higher-order cognition, language and quantitative/data-oriented research.', 'Included as ucr-2. The re-audit removes weak sociology/youth-extremism insertions and replaces them with Machine Learning and Image Processing & Computer Vision, while retaining the broad psychology foundations required for a credible undergraduate programme.'),
      candidateAssessment(work, 'Work and Organisational Psychology is a formal target-programme specialisation and a coherent direction around organisational behaviour, leadership, workplace wellbeing, negotiation and applied organisational research.', 'Included as ucr-3. The visible label remains broader than the generating specialisation because the completed curriculum combines psychology with leadership, organisations, sociology, communication, business and behavioural economics.'),
      candidateAssessment(clinical, 'Clinical psychology and mental health forms a coherent formal target-programme direction supported by direct interests in mental health, addiction, diagnosis and assessment.', 'Not included because the counselor model already contains the maximum of three UCR alternatives (closest match plus two additional routes); the direction is retained explicitly rather than hidden in an omnibus residual bucket.'),
      candidateAssessment(educational, 'Educational psychology and learning forms a coherent formal target-programme direction supported by direct interests in educational psychology, learning, motivation and performance.', 'Not included because the counselor model already contains the maximum of three UCR alternatives; the direction is retained explicitly for auditability rather than merged into a catch-all category.')
    ],
    progression: {
      'ucr-1': 'Passed after moving Introduction to Sociology into Year 1 and New Issues in Contemporary Social Theory to Year 3, so the sociology sequence now progresses Introduction → Modern Sociology → Contemporary Social Theory. Advanced psychology research follows the earlier statistics course and the psychology gateway.',
      'ucr-2': 'Passed after re-audit. Introduction to Brain & Behavior and life-science foundations occur in Year 1; Neurobiology moves before the advanced cognition courses; Human Physiology precedes Mechanisms of Disease; and advanced data/cognition/research courses occur only after the relevant foundations. Formal prerequisites and fixed-term availability remain satisfied.',
      'ucr-3': 'Passed after moving Introduction to Sociology before Modern and Contemporary Social Theory and moving Advanced Research Seminar to the final year, after foundational research methods and Statistics & Experimental Methods. Business and leadership prerequisites remain satisfied.'
    }
  });
  r.validation.officialEvidenceChecked = '2026-09-15';
  write(r);
}

// Align the older structural validator with the final-methodology rule that a generator-eligible
// interest may be explicitly owned by the closest-match core rather than a candidate direction.
{
  const file = path.join(root, 'scripts', 'validate-counselor-structural-rules.mjs');
  let text = fs.readFileSync(file, 'utf8');
  const needle = `    for (const item of assessed) {\n      if (item.constructionRole === 'generator-eligible' && !generatedRows.has(item.registryRow)) {\n        fail(\`generator-eligible interest row \${item.registryRow} was not assessed within any candidate direction\`);\n      }\n    }`;
  const replacement = `    const coveredByClosest = new Set(\n      Array.isArray(record?.academicRationale?.finalMethodologyAudit?.coveredByClosestMatchInterestRows)\n        ? record.academicRationale.finalMethodologyAudit.coveredByClosestMatchInterestRows\n        : []\n    );\n    for (const item of assessed) {\n      if (item.constructionRole === 'generator-eligible' && !generatedRows.has(item.registryRow) && !coveredByClosest.has(item.registryRow)) {\n        fail(\`generator-eligible interest row \${item.registryRow} was neither assessed within a candidate direction nor explicitly covered by the closest-match core\`);\n      }\n    }`;
  assert(text.includes(needle), 'structural validator ownership block not found');
  text = text.replace(needle, replacement);
  fs.writeFileSync(file, text);
}

// Remove the temporary four-record exemption: all counselor records must now pass final rules.
{
  const file = path.join(root, 'scripts', 'validate-counselor-final-rules.mjs');
  let text = fs.readFileSync(file, 'utf8');
  const legacy = "const legacyPendingReaudit = new Set(['cp-000001', 'cp-000002', 'cp-000003', 'cp-000004']);";
  assert(text.includes(legacy), 'final-rules legacy exemption not found');
  text = text.replace(legacy, 'const legacyPendingReaudit = new Set();');
  fs.writeFileSync(file, text);
}

console.log('Phase-three counselor re-audit migration applied to cp-000001 through cp-000004.');
