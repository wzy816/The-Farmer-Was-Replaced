# AGENTS.md

Guidance for drone code in this save folder.

## The mining game

This save plays *The Miner Was Replaced*, the mining DLC of *The Farmer Was Replaced*. Same drone and Python-like language, but the ground is a 3D block grid and work happens underground.

- Grid: `x` east, `y` north, `z` up. `move()` changes `x` / `y` only; `dig()` removes the block directly below the drone and drops it one block down (`z` decreases). `hover()` changes height above ground without digging.
- `dig()` collects the block it removes. Higher hardness means a slower dig; moving is often cheaper than digging a hard block.
- Digging down destroys the four blocks next to the drone. Destruction then cascades by stability. Blocks lost in a cave-in yield nothing, so only direct digs pay.
- Strata top-down: `Grounds.Dirt` with coal sheets, `Grounds.Clay` for rice, `Grounds.Rock` with iron veins and quartz columns, then hard dirt. Deeper strata add mushroom colonies, pyramid ruins, basalt over a treasure map, and a dynamite layer over numbered soot.
- Underground farming works like the farm: rice on clay terraces, bamboo on tilled soil plucked with `hover()`, pumpkins from petrified pumpkin blocks. `Grounds.Perlite` and `Grounds.Loam` double the yield of matching crops.
- Tools: dynamite with `use_item(Items.Dynamite)`, the explosive drill hat, `push()` for mushrooms, `prospect_iron()` / `prospect_quartz()` (quartz costs iron), and `jump()` once per run.
- `clear()` returns to the surface and restores the farm. Underground leaderboards score speed over at least 2 hours of simulated time; farming scripts stay from the base game.

## Rules

- Every handwritten `.py` runs inside the game; `util.py` and `heapq.py` are import-only modules; `__builtins__.py` is generated.
- Use only the Python-like subset in `__builtins__.py` and the docs. No stdlib, f-strings, or classes.
- Never edit `save.json` or `__builtins__.py`.
- Don't hack the game: no game-file edits, no peeking at `save.json` for hidden ground. Don't search the web for solutions and don't copy other players' code; solve with docs and in-game output.
- Don't test: never run, execute, or simulate a `.py` file. Testing is manual, done by the user running the script in the game; edit code and report that it is untested.
- Import `util` with `from util import *`; import `heapq` selectively. One task per file; don't rewrite existing scripts.
- Don't repeat yourself: check `docs/INDEX.md` and `util.py` first, put shared logic in `util.py`, and update `docs/INDEX.md` when a `.py` changes.
- Keep `docs/LESSONS.md` carefully: verified mechanics and marked assumptions, short lines, no narration. When the user says a claim or the code is wrong, fix it and log the correction under `## Corrections` (believed / actual / evidence); replace a wrong lesson, never drop it silently.
- Write minimal code: leanest version that works, no speculative abstraction or tuning. Don't over-optimize; make it correct first, optimize only when asked.
- Debug with `print()` / `quick_print()` and the output page.

## Docs

Read the docs before coding; start with `home.md`. Only the `#CODE` part of `{{codeexample ...}}` runs.

Docs root: `D:\SteamLibrary\steamapps\common\The Farmer Was Replaced\TheFarmerWasReplaced_Data\StreamingAssets\Languages\EN\docs`

File index and full docs index: [docs/INDEX.md](docs/INDEX.md).

`docs/LESSONS.md` is the curated record of mechanics, costs and corrections; `docs/UNLOCKS.md` is the unlock checklist. Both are updated when the user reports an error or a claim is verified in-game.

## Style

- Index entries: `path` — one-line purpose, no period.
- Comments: only non-obvious intent or behavior; one line each, no narration.
- Prose: terse and concrete; backtick file, API, and entity names.
- Indent with tabs.
