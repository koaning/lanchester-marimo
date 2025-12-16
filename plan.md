# Battle anywidget demo plan (implemented)

## Goals

- Provide a spatial battle anywidget demo that runs smoothly in the browser (JS), while exposing parameters + results to Python via traitlets.
- Keep notebook integration simple: the marimo notebook defines the Python widget class inline and points `_esm` / `_css` to on-disk asset files.

## Implemented steps

1. Implement the spatial simulation in JS:
   - Units spawn on left/right halves of the arena with a seeded RNG.
   - Each tick, every unit moves toward its nearest opponent.
   - Naive collision handling: a couple of relaxation passes push overlapping circles apart.
   - Combat: if nearest opponent is within `attack_range` and cooldown allows, attack with `hit_chance` and apply `damage` to `hp`.
   - Stop condition: one team reaches 0 alive units; set `winner`.

2. Implement rendering + controls in JS:
   - Canvas renderer draws blue/red circles and an overlay with `t`, blue count, red count.
   - UI controls: `Generate`, `Start/Pause`, `Reset`, `Export history`.
   - A requestAnimationFrame loop advances simulation (a few substeps per frame) when `running=true`.

3. Define widget state (traitlets) in Python:
   - Parameters: `n_blue`, `n_red`, `seed`, arena size, `unit_radius`, `step_dt`, `move_speed`, and combat params.
   - Control/state: `running`, `status`, `command`.
   - Output: `history_json` for exporting results back to Python.

4. Implement export plumbing:
   - `Export history` button sets `command="export:<nonce>"` to trigger JS export.
   - JS writes a single JSON payload into `history_json` (params + summary + coarse `history` time series).
   - JS also auto-exports when the battle finishes.

5. Implement the marimo demo notebook:
   - File: `battle_widget_demo.py`.
   - Contains the `BattleWidget` class inline and loads `_esm`/`_css` by reading:
     - `battle_widget/battle_widget.js`
     - `battle_widget/battle_widget.css`
   - Instantiates and displays a `BattleWidget()` instance.

## Files

- JS simulation/UI: `battle_widget/battle_widget.js`
- Widget styles (incl. dark mode): `battle_widget/battle_widget.css`
- Demo notebook: `battle_widget_demo.py`
