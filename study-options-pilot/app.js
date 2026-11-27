import { createSearch } from "./search.js";

async function start() {
  const response = await fetch(new URL("index.json", import.meta.url));
  if (!response.ok) throw new Error("Search index unavailable");
  const search = createSearch(await response.json());
  const form = document.querySelector("#search");
  const input = document.querySelector("#interest");
  const list = document.querySelector("#options");
  const heading = document.querySelector("#browse");
  const status = document.querySelector("#status");
  const reset = document.querySelector("#reset");
  const cards = new Map([...list.children].map(card => [card.dataset.option, card]));

  function show(value) {
    const query = value.trim();
    heading.textContent = query ? "Search results" : "Browse study options";
    reset.hidden = !query;
    if (!query) {
      for (const card of cards.values()) card.querySelector(".match").hidden = true;
      list.replaceChildren(...cards.values());
      status.textContent = "";
      return;
    }
    const results = search(query);
    const full = results.filter(r => !r.missing.length).length;
    if (!results.length) status.textContent = "No study options match these interests in this pilot. Try a broader subject or browse all study options.";
    else if (!full) status.textContent = "These options cover part of your search.";
    else status.textContent = full === 1 ? "One option covers your full search." : `${full} options cover your full search.`;
    const ordered = results.map(({slug, matched, missing}) => {
      const card = cards.get(slug);
      const note = card.querySelector(".match");
      note.hidden = false;
      note.textContent = missing.length
        ? `Partial match · ${matched.join(", ")}. Outside this match: ${missing.join(", ")}.`
        : `Matches · ${matched.join(", ")}`;
      return card;
    });
    list.replaceChildren(...ordered);
  }

  function update() {
    const url = new URL(location.href);
    const query = input.value.trim();
    if (query) url.searchParams.set("q", query);
    else url.searchParams.delete("q");
    history.replaceState(null, "", url);
    show(query);
  }
  function restore() {
    input.value = (new URL(location.href).searchParams.get("q") || "").slice(0, input.maxLength);
    show(input.value);
  }
  form.addEventListener("submit", e => { e.preventDefault(); update(); });
  input.addEventListener("input", update);
  reset.addEventListener("click", () => { input.value = ""; update(); input.focus(); });
  window.addEventListener("popstate", restore);
  restore();
  form.hidden = false;
}

// The complete list of study options and their links already exist in the HTML.
start().catch(() => { document.querySelector("#status").textContent = "Search is unavailable. Browse the study options below."; });
