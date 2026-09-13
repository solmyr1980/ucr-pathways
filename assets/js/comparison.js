// Shared presentation semantics for browser and Node renderers.
export function comparatorMetadata(record) {
  return record?.comparator || record?.referenceProgramme || {};
}

export function isComparatorProgramme(programme) {
  return programme?.role === 'comparator' || programme?.family === 'comparator';
}

export function isUcrAlternative(programme) {
  if (!programme || typeof programme !== 'object') return false;
  if (programme.family === 'ucr') return true;
  return ['ucr-alternative', 'ucr-depth', 'ucr-balanced', 'ucr-thematic'].includes(programme.role);
}

export function visibleProgrammeLabel(record, programme) {
  const meta = comparatorMetadata(record);
  if (isComparatorProgramme(programme)) return `${meta.name} at ${meta.institution}`;

  // Current records own their case-specific labels. Legacy labels are fallback-only.
  if (programme.label && !/^(UCR\s*[—–-]|Disciplinary\s)/i.test(programme.label)) {
    return record.origin === 'counselor'
      ? programme.label.replace('your interests', 'related interests')
      : programme.label;
  }

  const kind = programme.alternativeKind || programme.alternative_kind;
  if (kind === 'closest-match' || programme.role === 'ucr-depth') {
    return `Closest match to ${meta.name}`;
  }
  if (kind === 'related-direction' || programme.role === 'ucr-balanced') {
    return `${meta.name} + related subjects`;
  }
  if (kind === 'question-led' || programme.role === 'ucr-thematic') {
    return record.origin === 'counselor'
      ? 'A broader programme around related interests'
      : 'A broader programme around your interests';
  }
  return 'Another UCR programme option';
}

export function comparisonNotes(record) {
  return (record.notes || []).filter(note =>
    (!note.placement || note.placement === 'comparison') && note.text
  ).map(note => note.text);
}

export const comparisonGuidance = 'Blank cells indicate that no sufficiently comparable named component is shown in that position. The UCR programmes are illustrative compositions, not official tracks or guaranteed future schedules.';
