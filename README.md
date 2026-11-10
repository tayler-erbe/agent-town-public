# Agent Town

**A 3D town in the browser where each of my AI agents is a character with a home and an office.**

Agent Town is a visual skin over a system that was already running: a job queue, local models on one GPU, and Claude.
Every walk, light and animation comes from a real job, model server or file, so I can see who is working on what
across my projects without reading logs. It is a personal project by **Tayler Erbe**, running daily on my desktop
and still being built.

**Visit the site:** [tayler-erbe.github.io/agent-town-public](https://tayler-erbe.github.io/agent-town-public/)

| Page | What it covers |
|---|---|
| [Overview](https://tayler-erbe.github.io/agent-town-public/) | What the town is and what it does, with screens |
| [System design](https://tayler-erbe.github.io/agent-town-public/design/) | The system map, the town's rhythm, one command end to end, design decisions, and what is measured, live, built and not built |
| [How it was built](https://tayler-erbe.github.io/agent-town-public/built/) | From a 2D town to pixel art, concept art and 3D, with the trial and error |
| [The agents](https://taylererbe.com/agent-architecture.html) | On my portfolio: the agents the town shows and how they work |

## The idea in four lines

- **A projection, not a second system.** The town reads the job queue, agent charters, to-dos, ledger and model servers. It owns almost nothing.
- **One way back.** A command I confirm is written into the job queue under the queue's own lock. The queue's scheduler stays the only thing that runs work.
- **Honest states.** Each agent shows one state decided by one tested rule. A server that does not answer is offline, never asleep.
- **Honest numbers.** Money counts only when verified; untracked is not $0. No revenue, time saved or adoption is claimed.

## What is and isn't here

| Here | Not here |
|---|---|
| The website (`index.html`, `design/`, `built/`) and its screenshots | The town's source code (kept private) |
| Concept art and screens of the running town | Agent data, chats, the job queue, money records or credentials |

## View it locally

```bash
python -m http.server 8000
```

Then open http://localhost:8000/.

`design/` and `built/` are generated from the canonical pages on my portfolio with `python tools/build_pages.py <portfolio checkout>`;
`index.html` is written by hand. Styles: `assets/site.css` is a copy of the portfolio's design system, `assets/town.css` holds this site's page parts.
