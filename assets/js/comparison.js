// Shared presentation semantics for browser and Node renderers.
export function comparatorMetadata(record) {
  return record?.comparator || record?.referenceProgramme || {};
}

export function visibleProgrammeLabel(record, programme) {
  const meta = comparatorMetadata(record);
  if (programme.role === 'comparator') return `${meta.name} at ${meta.institution}`;
  // Current records own their case-specific labels. Legacy labels are fallback-only.
  if (programme.label && !/^(UCR\s*[—–-]|Disciplinary\s)/i.test(programme.label)) {
    return record.origin === 'counselor'
      ? programme.label.replace('your interests', 'related interests')
      : programme.label;
  }
  if (programme.role === 'ucr-depth') return `Closest match to ${meta.name}`;
  if (programme.role === 'ucr-balanced') return `${meta.name} + related subjects`;
  return record.origin === 'counselor'
    ? 'A broader programme around related interests'
    : 'A broader programme around your interests';
}

export function comparisonNotes(record) {
  return (record.notes || []).filter(note =>
    (!note.placement || note.placement === 'comparison') && note.text
  ).map(note => note.text);
}

export const comparisonGuidance = 'Blank cells indicate that no sufficiently comparable named component is shown in that position. The UCR programmes are illustrative compositions, not official tracks or guaranteed future schedules.';
