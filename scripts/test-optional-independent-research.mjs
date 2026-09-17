import assert from 'node:assert/strict';
import { applyOptionalIndependentResearch, stripOptionalIndependentResearch } from './optional-independent-research.mjs';

function baseRecord() {
  return {
    programmes: [
      { id: 'comparator', family: 'comparator' },
      { id: 'ucr-1', family: 'ucr' },
      { id: 'ucr-2', family: 'ucr' }
    ],
    blocks: [
      {
        title: 'Research and professional development',
        rows: [
          { cells: { comparator: { text: 'Bachelor Thesis', credits: 10, componentId: 'thesis' } } },
          { cells: {
            'ucr-1': { text: 'Personal & Professional Development', credits: 7.5, courseCode: 'ACCPPDE101' },
            'ucr-2': { text: 'Personal & Professional Development', credits: 7.5, courseCode: 'ACCPPDE101' }
          } }
        ]
      }
    ]
  };
}

{
  const record = applyOptionalIndependentResearch(baseRecord(), 'thesis');
  const row = record.blocks[0].rows[0];
  assert.equal(row.cells['ucr-1'].text, 'Optional independent research');
  assert.equal(row.cells['ucr-1'].credits, 15);
  assert.equal(record.optionalIndependentResearch.placement, 'parallel-to-comparator-research');
  const stripped = stripOptionalIndependentResearch(record);
  assert.equal(stripped.blocks[0].rows[0].cells['ucr-1'], undefined);
  assert.equal(stripped.blocks[0].rows.length, 2);
}

{
  const record = applyOptionalIndependentResearch(baseRecord(), null);
  assert.equal(record.blocks[0].rows.length, 3);
  assert.equal(record.blocks[0].rows[2].cells['ucr-2'].text, 'Optional independent research');
  assert.equal(record.optionalIndependentResearch.placement, 'ppd-block-fallback');
}

{
  const record = baseRecord();
  record.blocks[0].rows[0].cells['ucr-1'] = { text: 'Research Methods', credits: 7.5, courseCode: 'METHOD101' };
  applyOptionalIndependentResearch(record, 'thesis');
  assert.equal(record.blocks[0].rows.length, 3);
  assert.equal(record.blocks[0].rows[1].cells['ucr-1'].text, 'Optional independent research');
  assert.equal(record.optionalIndependentResearch.placement, 'adjacent-to-comparator-research');
}

console.log('Optional independent research placement tests: PASS');
