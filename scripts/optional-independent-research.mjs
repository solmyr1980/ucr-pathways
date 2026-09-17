export const OPTIONAL_RESEARCH_ID = 'optional-independent-research';
export const OPTIONAL_RESEARCH_TEXT = 'Optional independent research';
export const OPTIONAL_RESEARCH_CREDITS = 15;
export const PPD_CODE = 'ACCPPDE101';

function nonEmptyCell(cell) {
  return cell && typeof cell === 'object' && !Array.isArray(cell) && Object.keys(cell).length > 0;
}

function optionalCell() {
  return {
    text: OPTIONAL_RESEARCH_TEXT,
    credits: OPTIONAL_RESEARCH_CREDITS,
    comparisonOnly: true,
    comparisonElementId: OPTIONAL_RESEARCH_ID
  };
}

function ucrProgrammes(record) {
  return (record.programmes || []).filter(programme => programme?.family === 'ucr');
}

function rowHasOptionalResearch(row, programmeIds) {
  return programmeIds.some(id => row?.cells?.[id]?.comparisonElementId === OPTIONAL_RESEARCH_ID);
}

export function applyOptionalIndependentResearch(record, researchComponentId) {
  if (!record || typeof record !== 'object' || Array.isArray(record)) throw new Error('record must be an object');
  if (!Object.hasOwn(record, 'blocks') || !Array.isArray(record.blocks)) throw new Error('record.blocks must be an array');

  const ucr = ucrProgrammes(record);
  if (!ucr.length) throw new Error('record must contain at least one UCR programme');
  const programmeIds = ucr.map(programme => programme.id);

  let existing = 0;
  for (const block of record.blocks) {
    for (const row of block.rows || []) if (rowHasOptionalResearch(row, programmeIds)) existing += 1;
  }
  if (existing) throw new Error('optional independent research is already present');

  if (researchComponentId !== null && (typeof researchComponentId !== 'string' || !researchComponentId.trim())) {
    throw new Error('researchComponentId must be a non-empty comparator component ID or null');
  }

  let targetBlock = null;
  let targetRowIndex = -1;
  let placement = null;

  if (researchComponentId !== null) {
    for (const block of record.blocks) {
      const index = (block.rows || []).findIndex(row => row?.cells?.comparator?.componentId === researchComponentId);
      if (index >= 0) {
        if (targetBlock) throw new Error(`researchComponentId ${researchComponentId} appears in more than one comparison row`);
        targetBlock = block;
        targetRowIndex = index;
      }
    }
    if (!targetBlock) throw new Error(`researchComponentId ${researchComponentId} is not present in the comparison`);

    const targetRow = targetBlock.rows[targetRowIndex];
    const occupied = programmeIds.some(id => nonEmptyCell(targetRow?.cells?.[id]));
    if (!occupied) {
      for (const id of programmeIds) targetRow.cells[id] = optionalCell();
      placement = 'parallel-to-comparator-research';
    } else {
      const row = {
        comparisonOnly: OPTIONAL_RESEARCH_ID,
        cells: Object.fromEntries(programmeIds.map(id => [id, optionalCell()]))
      };
      targetBlock.rows.splice(targetRowIndex + 1, 0, row);
      placement = 'adjacent-to-comparator-research';
    }
  } else {
    for (const block of record.blocks) {
      const index = (block.rows || []).findIndex(row => programmeIds.some(id => row?.cells?.[id]?.courseCode === PPD_CODE));
      if (index >= 0) {
        if (targetBlock) throw new Error('PPD appears in more than one comparison block');
        targetBlock = block;
        targetRowIndex = index;
      }
    }
    if (!targetBlock) throw new Error('cannot place optional independent research because no PPD row was found');
    const row = {
      comparisonOnly: OPTIONAL_RESEARCH_ID,
      cells: Object.fromEntries(programmeIds.map(id => [id, optionalCell()]))
    };
    targetBlock.rows.splice(targetRowIndex + 1, 0, row);
    placement = 'ppd-block-fallback';
  }

  record.optionalIndependentResearch = {
    id: OPTIONAL_RESEARCH_ID,
    text: OPTIONAL_RESEARCH_TEXT,
    credits: OPTIONAL_RESEARCH_CREDITS,
    researchComponentId,
    placement,
    excludedFromProgrammeCredits: true,
    excludedFromSchedule: true
  };
  return record;
}

export function stripOptionalIndependentResearch(record) {
  const copy = structuredClone(record);
  for (const block of copy.blocks || []) {
    block.rows = (block.rows || []).filter(row => row?.comparisonOnly !== OPTIONAL_RESEARCH_ID);
    for (const row of block.rows) {
      for (const [id, cell] of Object.entries(row.cells || {})) {
        if (cell?.comparisonElementId === OPTIONAL_RESEARCH_ID) delete row.cells[id];
      }
    }
  }
  delete copy.optionalIndependentResearch;
  return copy;
}
