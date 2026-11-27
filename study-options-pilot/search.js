// The same matcher runs in the browser and in the catalogue-scale benchmark.
const filler = new Set("i m am i'm im me my really also interested interests interest in into study studying studies learn learning about combine combining how can could want to would like love enjoy and with plus of the a an at ucr both".split(" "));

function words(value) {
  return value.toLowerCase().normalize("NFKD").replace(/\p{M}/gu, "")
    .replace(/[’']/g, "").match(/[\p{L}\p{N}]+/gu) ?? [];
}

export function createSearch(index) {
  const phrases = new Map();
  let longest = 1;
  for (const [topic, aliases] of Object.entries(index.topics)) {
    for (const name of [topic, ...aliases]) {
      const parts = words(name);
      const key = parts.join(" ");
      if (phrases.has(key) && phrases.get(key) !== topic) throw new Error("Ambiguous search phrase");
      phrases.set(key, topic);
      longest = Math.max(longest, parts.length);
    }
  }

  function parse(query) {
    const requested = new Set();
    for (const part of query.split(/[,;&+/|]/u)) {
      const tokens = words(part);
      let unknown = [];
      function flush() {
        if (unknown.length) requested.add(unknown.join(" "));
        unknown = [];
      }
      for (let i = 0; i < tokens.length;) {
        let size = Math.min(longest, tokens.length - i);
        while (size > 0 && !phrases.has(tokens.slice(i, i + size).join(" "))) size--;
        if (size) {
          flush();
          requested.add(phrases.get(tokens.slice(i, i + size).join(" ")));
          i += size;
        } else {
          if (filler.has(tokens[i])) flush();
          else unknown.push(tokens[i]);
          i++;
        }
      }
      flush();
    }
    return [...requested];
  }

  return function search(query) {
    const requested = parse(query);
    const results = [];
    for (const option of index.options) {
      const matched = [];
      const missing = [];
      let weight = 0;
      for (const term of requested) {
        const rank = option.topics.indexOf(term);
        if (rank < 0) missing.push(term);
        else {
          matched.push(term);
          weight += 1 / (1 + rank);
        }
      }
      if (matched.length) results.push({slug: option.slug, matched, missing, weight});
    }
    return results.sort((a, b) => b.matched.length - a.matched.length || b.weight - a.weight
      || a.slug.localeCompare(b.slug));
  };
}
