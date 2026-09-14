import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const masterFile = path.join(root, 'docs', 'UCR_Pathways_Master_Specification.md');
const productionFile = path.join(root, 'docs', 'UCR_Pathways_Production_Instructions.md');
const schemaFile = path.join(root, 'data', 'schema', 'counselor-comparison.schema.json');
const packageFile = path.join(root, 'package.json');
const interestsFile = path.join(root, 'data', 'registry', 'programme_interests.csv');
const comparisonsDir = path.join(root, 'data', 'counselor', 'comparisons');
const targetIds = ['cp-000001', 'cp-000002', 'cp-000003', 'cp-000004'];

function write(file, content) {
  fs.writeFileSync(file, content.endsWith('\n') ? content : `${content}\n`);
}

function insertAfter(text, anchor, addition, marker) {
  if (marker && text.includes(marker)) return text;
  if (!text.includes(anchor)) throw new Error(`Required documentation anchor not found: ${anchor.slice(0, 100)}`);
  return text.replace(anchor, `${anchor}\n\n${addition}`);
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = '';
  let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i += 1;
        } else quoted = false;
      } else field += ch;
      continue;
    }
    if (ch === '"') quoted = true;
    else if (ch === ',') {
      row.push(field);
      field = '';
    } else if (ch === '\n') {
      row.push(field.replace(/\r$/, ''));
      rows.push(row);
      row = [];
      field = '';
    } else field += ch;
  }
  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ''));
    rows.push(row);
  }
  const headers = rows[0].map((value, index) => index === 0 ? value.replace(/^\uFEFF/, '') : value);
  return rows.slice(1)
    .filter(values => values.some(value => String(value).trim()))
    .map((values, index) => ({
      ...Object.fromEntries(headers.map((header, column) => [header, values[column] ?? ''])),
      __registryRow: index + 2
    }));
}

function expectedConstructionRole(row) {
  if (row.target_mapping_status === 'inherited-across-split-targets') return 'excluded-inherited';
  switch (row.interest_relationship) {
    case 'Direct programme interest':
    case 'Stable study direction': return 'generator-eligible';
    case 'Curricular topic': return 'support-only';
    case 'Illustrative or temporary topic':
    case 'Outcome or individual trajectory': return 'search-only';
    default: throw new Error(`Unsupported interest relationship: ${row.interest_relationship}`);
  }
}

function allEvidenceItems(record) {
  const map = new Map();
  for (const section of ['coreField', 'adjacentDirections', 'questionsApplications']) {
    for (const item of record?.academicRationale?.[section] || []) map.set(item.label, item);
  }
  return map;
}

function resolveInterestRowsFromEvidence(evidence, targetRows) {
  const resolved = new Set();
  const byRegistry = new Map(targetRows.map(row => [row.__registryRow, row]));
  const bySourceExcel = new Map(targetRows.map(row => [Number(row.source_interest_excel_row), row]));
  for (const item of evidence || []) {
    if (item?.sourceType !== 'programme-interest') continue;
    const ref = String(item.reference || '');
    let match = ref.match(/programme_interests\.csv:(\d+)/i);
    if (match && byRegistry.has(Number(match[1]))) {
      resolved.add(Number(match[1]));
      continue;
    }
    match = ref.match(/source_interest_excel_row\s+(\d+)/i);
    if (match) {
      const row = bySourceExcel.get(Number(match[1]));
      if (row) resolved.add(row.__registryRow);
    }
  }
  return resolved;
}

function interestEvidence(targetRows, rowIds) {
  const byId = new Map(targetRows.map(row => [row.__registryRow, row]));
  return rowIds.map(rowId => {
    const row = byId.get(rowId);
    return {
      sourceType: 'programme-interest',
      reference: `programme_interests.csv:${rowId}`,
      note: `${row.interest_relationship}: ${row.student_interest}`
    };
  });
}

function buildInterestSelection(record, targetRows) {
  const assessedInterests = targetRows.map(row => ({
    registryRow: row.__registryRow,
    sourceInterestExcelRow: Number(row.source_interest_excel_row),
    studentInterest: row.student_interest,
    interestRelationship: row.interest_relationship,
    targetMappingStatus: row.target_mapping_status || '',
    constructionRole: expectedConstructionRole(row)
  }));
  const roleByRow = new Map(assessedInterests.map(item => [item.registryRow, item.constructionRole]));
  const generatorRows = assessedInterests.filter(item => item.constructionRole === 'generator-eligible').map(item => item.registryRow);
  const mapItems = allEvidenceItems(record);
  const coreInterestRows = new Set();
  for (const item of record?.academicRationale?.coreField || []) {
    for (const rowId of resolveInterestRowsFromEvidence(item.evidence, targetRows)) coreInterestRows.add(rowId);
  }

  const candidateDirections = [];
  const usedGeneratorRows = new Set();
  for (const alternative of (record?.academicRationale?.alternatives || []).slice(1)) {
    const evidence = [...(alternative.evidence || [])];
    for (const basisLabel of alternative.basisLabels || []) {
      const item = mapItems.get(basisLabel);
      if (item) evidence.push(...(item.evidence || []));
    }
    const referenced = [...resolveInterestRowsFromEvidence(evidence, targetRows)];
    const generating = referenced.filter(rowId => roleByRow.get(rowId) === 'generator-eligible');
    const supporting = referenced.filter(rowId => roleByRow.get(rowId) === 'support-only');
    generating.forEach(rowId => usedGeneratorRows.add(rowId));
    const hasOfficial = evidence.some(item => item?.sourceType === 'official-source');
    candidateDirections.push({
      label: alternative.concept,
      basisType: generating.length ? (hasOfficial ? 'combined' : 'programme-interest-cluster') : 'official-structure',
      generatingInterestRows: generating,
      supportingInterestRows: supporting,
      evidence: evidence.filter((item, index, array) => item && array.findIndex(other => JSON.stringify(other) === JSON.stringify(item)) === index),
      disposition: 'included',
      programmeId: alternative.programmeId
    });
  }

  const uncoveredGenerators = generatorRows.filter(rowId => !usedGeneratorRows.has(rowId));
  const coveredByClosest = uncoveredGenerators.filter(rowId => coreInterestRows.has(rowId));
  const remaining = uncoveredGenerators.filter(rowId => !coreInterestRows.has(rowId));
  if (coveredByClosest.length) {
    candidateDirections.push({
      label: 'Core programme interests already represented by the closest match',
      basisType: 'programme-interest-cluster',
      generatingInterestRows: coveredByClosest,
      supportingInterestRows: [],
      evidence: interestEvidence(targetRows, coveredByClosest),
      disposition: 'rejected',
      rejectionReason: 'covered-by-closest-match'
    });
  }
  if (remaining.length) {
    const stop = record?.alternativeSelection?.stoppingReason;
    const rejectionReason = stop === 'maximum-reached' ? 'maximum-reached'
      : stop === 'not-feasible' ? 'not-feasible'
        : stop === 'insufficient-evidence' ? 'insufficient-evidence'
          : 'not-substantively-distinct';
    candidateDirections.push({
      label: 'Other eligible programme-interest directions',
      basisType: 'programme-interest-cluster',
      generatingInterestRows: remaining,
      supportingInterestRows: [],
      evidence: interestEvidence(targetRows, remaining),
      disposition: 'rejected',
      rejectionReason
    });
  }
  return { assessedInterests, candidateDirections };
}

function migrateBlocks(record) {
  const ucrProgrammes = (record.programmes || []).filter(programme => programme?.family === 'ucr');
  const programmeOrder = new Map(ucrProgrammes.map((programme, index) => [programme.id, index]));
  const oldCellByProgrammeCode = new Map();
  const occurrences = new Map();

  for (const [blockIndex, block] of (record.blocks || []).entries()) {
    for (const [rowIndex, row] of (block.rows || []).entries()) {
      for (const programme of ucrProgrammes) {
        const cell = row?.cells?.[programme.id];
        const code = String(cell?.courseCode || '').trim();
        if (!code) continue;
        oldCellByProgrammeCode.set(`${programme.id}:${code}`, structuredClone(cell));
        if (!occurrences.has(code)) occurrences.set(code, []);
        occurrences.get(code).push({ programmeId: programme.id, programmeIndex: programmeOrder.get(programme.id), blockIndex, rowIndex });
      }
    }
  }

  const scheduleCellByProgrammeCode = new Map();
  for (const programme of ucrProgrammes) {
    for (const semester of programme?.schedule?.semesters || []) {
      for (const course of semester?.courses || []) {
        scheduleCellByProgrammeCode.set(`${programme.id}:${course.code}`, {
          text: course.name,
          credits: course.credits,
          courseCode: course.code
        });
        if (!occurrences.has(course.code)) occurrences.set(course.code, []);
      }
    }
  }

  const canonical = new Map();
  for (const [code, items] of occurrences) {
    if (!items.length) throw new Error(`${record.id}: scheduled course ${code} has no existing comparison placement`);
    const chosen = [...items].sort((a, b) => a.programmeIndex - b.programmeIndex || a.blockIndex - b.blockIndex || a.rowIndex - b.rowIndex)[0];
    canonical.set(code, chosen);
  }

  function mergedCourseCells(code) {
    const cells = {};
    for (const programme of ucrProgrammes) {
      const key = `${programme.id}:${code}`;
      const cell = oldCellByProgrammeCode.get(key) || scheduleCellByProgrammeCode.get(key);
      if (cell) cells[programme.id] = structuredClone(cell);
    }
    return cells;
  }

  const newBlocks = [];
  for (const [blockIndex, block] of (record.blocks || []).entries()) {
    const rows = [];
    const createdCodes = new Set();
    const codesForBlock = [...canonical.entries()]
      .filter(([, location]) => location.blockIndex === blockIndex)
      .sort((a, b) => a[1].rowIndex - b[1].rowIndex || a[1].programmeIndex - b[1].programmeIndex || a[0].localeCompare(b[0]));
    const byAnchorRow = new Map();
    for (const [code, location] of codesForBlock) {
      if (!byAnchorRow.has(location.rowIndex)) byAnchorRow.set(location.rowIndex, []);
      byAnchorRow.get(location.rowIndex).push(code);
    }

    for (const [rowIndex, oldRow] of (block.rows || []).entries()) {
      const comparator = oldRow?.cells?.comparator ? structuredClone(oldRow.cells.comparator) : null;
      const anchoredCodes = byAnchorRow.get(rowIndex) || [];
      if (!anchoredCodes.length) {
        if (comparator) rows.push({ cells: { comparator } });
        continue;
      }
      let comparatorAttached = false;
      for (const code of anchoredCodes) {
        const cells = mergedCourseCells(code);
        if (comparator && !comparatorAttached) {
          cells.comparator = comparator;
          comparatorAttached = true;
        }
        rows.push({ cells });
        createdCodes.add(code);
      }
    }
    for (const [code] of codesForBlock) {
      if (!createdCodes.has(code)) rows.push({ cells: mergedCourseCells(code) });
    }
    if (rows.length) newBlocks.push({ ...block, rows });
  }
  record.blocks = newBlocks;
}

function addLabelRationales(record) {
  const ucrProgrammes = (record.programmes || []).filter(programme => programme?.family === 'ucr');
  if (record.id === 'cp-000004') {
    const work = ucrProgrammes.find(programme => programme.id === 'ucr-3');
    if (work) work.label = 'Psychology, leadership & organisations';
  }
  for (const [index, alternative] of (record?.academicRationale?.alternatives || []).entries()) {
    const programme = ucrProgrammes[index];
    if (!programme) continue;
    if (record.id === 'cp-000004' && programme.id === 'ucr-3') {
      alternative.labelRationale = 'The generating concept concerns work and organisational psychology, but the completed 24-course curriculum combines psychology with leadership, organisations, sociology, communication, business and behavioural economics. The broader visible label describes the actual programme without presenting one psychology strand as the whole curriculum.';
    } else if (index === 0) {
      alternative.labelRationale = `The visible label was reviewed after completion of the 24-course curriculum and accurately presents this option as the closest feasible UCR response to ${record.comparator?.name || 'the comparator'}, rather than as a narrower subfield.`;
    } else {
      alternative.labelRationale = `The visible label was reviewed after completion of the 24-course curriculum and describes its substantive organising direction without treating the generating concept as an official UCR track or overstating one strand of the programme.`;
    }
  }
}

// 1. Durable decisions in the Master Specification.
let master = fs.readFileSync(masterFile, 'utf8');
master = insertAfter(
  master,
  'Do not expose internal implementation names such as `ucr-alternative`, `closest-match`, `related-direction` or `question-led` as user-facing product taxonomy unless a later design decision explicitly does so.',
  'For every UCR alternative, distinguish the **generating concept** from the **visible programme label**. The concept records why the alternative was constructed. Assign the final visible label only after the complete UCR curriculum has been built and validated. The label must describe the actual curricular composition broadly enough that it does not present one strand as though it defined the whole programme.',
  'distinguish the **generating concept** from the **visible programme label**'
);
master = insertAfter(
  master,
  'Where `target_mapping_status=inherited-across-split-targets`, the inherited interest record is provenance/general discovery evidence only. It is not target-specific academic evidence unless independently corroborated for that exact normalized target.',
  'For counselor programme construction, programme-interest evidence is stricter than discovery search. All target-linked programme-interest rows must be assessed. `Direct programme interest` and `Stable study direction` rows may generate candidate directions; `Curricular topic` rows may support but not independently generate a direction; `Illustrative or temporary topic` and `Outcome or individual trajectory` rows remain discovery evidence and do not generate UCR alternatives. Eligible interests must be considered as evidence-backed substantive directions rather than selected ad hoc as isolated rows.',
  'programme-interest evidence is stricter than discovery search'
);
master = insertAfter(
  master,
  'Blocks classify and align programme components; they do not replace them with selective summaries. Preserve meaningful blank cells and structural differences, and do not force row-by-row symmetry, equal block sizes, identical credit allocations or one-to-one course equivalence. The number and size of blocks should follow the curricula rather than a fixed template. Do not use numerical depth/breadth scores.',
  'Within one comparison, **exact UCR course identity is the only basis for sharing a UCR comparison row**. A UCR course code has one canonical row and one canonical block. Every included UCR alternative containing that exact code populates that row; alternatives not containing it remain blank. Different UCR course codes occupy different rows even when their content is closely related. This identity rule does not require symmetry between different courses or between UCR and the external comparator.',
  'exact UCR course identity is the only basis for sharing a UCR comparison row'
);
write(masterFile, master);

// 2. Operational procedure in Production Instructions.
let production = fs.readFileSync(productionFile, 'utf8');
production = insertAfter(
  production,
  'Programme-interest data describe interests associated with the target programme. They do **not** establish that an imagined individual student also has unrelated additional interests. Use them to identify defensible academic directions, not to invent a fictional personal profile.',
  'For construction, retrieve **every** `programme_interests` row linked to the exact `counselor_programme_id` and assign it one construction role before defining additional alternatives:\n\n- `Direct programme interest` and `Stable study direction` → **generator-eligible**: may generate a candidate direction;\n- `Curricular topic` → **support-only**: may strengthen or enrich a direction but may not generate one by itself;\n- `Illustrative or temporary topic` and `Outcome or individual trajectory` → **search-only**: retain for discovery but do not use to generate UCR alternatives;\n- `target_mapping_status=inherited-across-split-targets` → **excluded-inherited** for construction unless the same substantive direction is independently corroborated for the exact target by current official evidence.\n\nDo not select a convenient subset of generator-eligible rows. Cluster all generator-eligible interests into coherent substantive directions before choosing an additional alternative. Record all assessed rows and the exact generating/supporting rows for every candidate direction so that inclusion and rejection decisions are auditable.',
  'generator-eligible**: may generate a candidate direction'
);
production = insertAfter(
  production,
  'Adjacent directions and questions/applications may legitimately be empty. Absence of evidence is a reason to stop generating alternatives, not a reason to fill the map from the UCR catalogue.',
  'When programme-interest rows are available, the evidence map must reflect the complete construction assessment described in Section 4.2. Build candidate directions from substantive clusters of generator-eligible interests, using support-only rows only as supplementary evidence. A single isolated interest row may define a candidate only when it is itself a coherent substantive direction. Search-only and excluded-inherited rows must not enter candidate construction. Preserve the exact interest-row provenance and disposition of each candidate direction in `academicRationale.interestSelection`.',
  'Preserve the exact interest-row provenance and disposition of each candidate direction'
);
production = insertAfter(
  production,
  'If it fails any gate, stop at two and record the stopping reason. If it passes, include three and record `maximum-reached` as the stopping state.',
  '### Step 6A — Finalize visible UCR labels\n\nAfter every included 24-course UCR curriculum has been selected, scheduled and validated, review its visible label against the completed curriculum. Preserve the generating `concept` separately in the academic rationale. The final `label` must describe what the completed programme actually contains and must not let one motivating strand masquerade as the whole programme. Use a single-field label only when the completed curriculum is genuinely dominated by that field; otherwise use an accurate combination or question/application label. Record a concise `labelRationale` for each UCR alternative.',
  '### Step 6A — Finalize visible UCR labels'
);
production = insertAfter(
  production,
  '- one comparison cell represents one canonical course/component; do not combine several UCR courses into a prose bundle;',
  '- for the UCR alternatives, exact `courseCode` identity is the **only** basis for sharing a row: build the UCR side of the comparison from the union of included UCR course codes, create one canonical row and block for each code, populate every UCR alternative that contains that exact code, and leave the other UCR cells blank;\n- two different UCR course codes must occupy separate rows even when their content is similar; never create a row-level equivalence merely for visual alignment;\n- assign the canonical block once for the course code within that comparison; the same course may not appear under different blocks in different UCR alternatives;',
  'exact `courseCode` identity is the **only** basis for sharing a row'
);
write(productionFile, production);

// 3. Schema contract.
const schema = JSON.parse(fs.readFileSync(schemaFile, 'utf8'));
const rationaleSchema = schema.allOf[1].properties.academicRationale;
if (!rationaleSchema.required.includes('interestSelection')) rationaleSchema.required.push('interestSelection');
rationaleSchema.properties.interestSelection = { '$ref': '#/$defs/interestSelection' };
const alternativeDef = schema.$defs.alternativeRationale;
if (!alternativeDef.required.includes('labelRationale')) alternativeDef.required.push('labelRationale');
alternativeDef.properties.labelRationale = { type: 'string', minLength: 1 };
schema.$defs.assessedInterest = {
  type: 'object',
  required: ['registryRow', 'sourceInterestExcelRow', 'studentInterest', 'interestRelationship', 'targetMappingStatus', 'constructionRole'],
  properties: {
    registryRow: { type: 'integer', minimum: 2 },
    sourceInterestExcelRow: { type: 'integer', minimum: 2 },
    studentInterest: { type: 'string', minLength: 1 },
    interestRelationship: { type: 'string', enum: ['Direct programme interest', 'Stable study direction', 'Curricular topic', 'Illustrative or temporary topic', 'Outcome or individual trajectory'] },
    targetMappingStatus: { type: 'string' },
    constructionRole: { type: 'string', enum: ['generator-eligible', 'support-only', 'search-only', 'excluded-inherited'] }
  },
  additionalProperties: false
};
schema.$defs.candidateDirection = {
  type: 'object',
  required: ['label', 'basisType', 'generatingInterestRows', 'supportingInterestRows', 'evidence', 'disposition'],
  properties: {
    label: { type: 'string', minLength: 1 },
    basisType: { type: 'string', enum: ['programme-interest-cluster', 'official-structure', 'combined'] },
    generatingInterestRows: { type: 'array', uniqueItems: true, items: { type: 'integer', minimum: 2 } },
    supportingInterestRows: { type: 'array', uniqueItems: true, items: { type: 'integer', minimum: 2 } },
    evidence: { type: 'array', minItems: 1, items: { '$ref': '#/$defs/evidenceRef' } },
    disposition: { type: 'string', enum: ['included', 'rejected'] },
    programmeId: { type: 'string', minLength: 1 },
    rejectionReason: { type: 'string', enum: ['covered-by-closest-match', 'insufficient-evidence', 'not-coherent', 'not-substantively-distinct', 'not-feasible', 'maximum-reached'] }
  },
  additionalProperties: false
};
schema.$defs.interestSelection = {
  type: 'object',
  required: ['assessedInterests', 'candidateDirections'],
  properties: {
    assessedInterests: { type: 'array', uniqueItems: true, items: { '$ref': '#/$defs/assessedInterest' } },
    candidateDirections: { type: 'array', uniqueItems: true, items: { '$ref': '#/$defs/candidateDirection' } }
  },
  additionalProperties: false
};
write(schemaFile, `${JSON.stringify(schema, null, 2)}\n`);

// 4. Make the structural validator part of the normal counselor validation command.
const pkg = JSON.parse(fs.readFileSync(packageFile, 'utf8'));
pkg.scripts['validate:counselor'] = 'node scripts/validate-counselor-comparison.mjs all && node scripts/validate-counselor-structural-rules.mjs all';
write(packageFile, `${JSON.stringify(pkg, null, 2)}\n`);

// 5. Repair the four existing production records.
const allInterests = parseCsv(fs.readFileSync(interestsFile, 'utf8'));
for (const id of targetIds) {
  const file = path.join(comparisonsDir, `${id}.json`);
  const record = JSON.parse(fs.readFileSync(file, 'utf8'));
  const targetRows = allInterests.filter(row => row.counselor_programme_id === id);
  addLabelRationales(record);
  record.academicRationale.interestSelection = buildInterestSelection(record, targetRows);
  migrateBlocks(record);
  write(file, `${JSON.stringify(record, null, 2)}\n`);
  console.log(`${id}: migrated ${targetRows.length} programme interests and rebuilt exact-identity comparison rows`);
}

console.log('Counselor production v3 migration complete.');
