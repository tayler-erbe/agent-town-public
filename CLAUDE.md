# Rules for this repository

This is the PUBLIC companion to the private repository that holds Agent Town's source. It holds a website only.

- Publish design and screens only. Never add source code, agent data, chats, job queue contents, money records, credentials, tokens, IP addresses, machine paths, or anything about Tayler's family.
- Claims must say whether they are measured, live, built or not built. Never claim revenue, time saved or adoption.
- `design/` and `built/` are generated from the portfolio pages (`agent-town-system-design.html`, `agent-city.html`) by `tools/build_pages.py`: change the portfolio page first, then rebuild. `index.html` is hand-written.
- Colours and fonts come only from the tokens in `assets/site.css` (a copy of the portfolio's); page parts go in `assets/town.css`.
- Images: crop to the content (no blurred padding, no burned-in labels), at most 900 px wide; keep privacy blurs that are already in a screenshot.
- Tayler approves text before it goes public.
