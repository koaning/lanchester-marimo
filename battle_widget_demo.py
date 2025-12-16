import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import anywidget
    import traitlets
    from pathlib import Path
    import marimo as mo


    def read_text(path: str) -> str:
        base = Path(__file__).resolve().parent
        return (base / path).read_text(encoding="utf-8")

    class BattleWidget(anywidget.AnyWidget):
        """Init-only batch simulator.

        Pass `grid_spec` + `runs_per_point` and read results from `results` once `done=True`.
        Each result record has: `run_id`, `seed`, `time`, `n_blue`, `n_red`.
        """

        _esm = read_text("battle_widget/battle_widget.js")
        _css = read_text("battle_widget/battle_widget.css")

        grid_spec = traitlets.Dict(default_value={"n_blue": [50], "n_red": [50]}).tag(sync=True)
        runs_per_point = traitlets.Int(5).tag(sync=True)
        seed_mode = traitlets.Unicode("random").tag(sync=True)
        base_seed = traitlets.Int(1).tag(sync=True)

        arena_width = traitlets.Int(640).tag(sync=True)
        arena_height = traitlets.Int(420).tag(sync=True)
        unit_radius = traitlets.Float(4.0).tag(sync=True)

        step_dt = traitlets.Float(0.02).tag(sync=True)  # seconds
        move_speed = traitlets.Float(55.0).tag(sync=True)  # pixels / second

        attack_range = traitlets.Float(10.0).tag(sync=True)  # pixels
        attack_cooldown = traitlets.Float(0.25).tag(sync=True)  # seconds
        hit_chance = traitlets.Float(0.85).tag(sync=True)
        damage = traitlets.Int(1).tag(sync=True)
        hp = traitlets.Int(1).tag(sync=True)

        max_time = traitlets.Float(30.0).tag(sync=True)
        record_dt = traitlets.Float(0.1).tag(sync=True)
        render = traitlets.Bool(True).tag(sync=True)
        done = traitlets.Bool(False).tag(sync=True)
        results = traitlets.List(traitlets.Dict()).tag(sync=True)
        results_len = traitlets.Int(0).tag(sync=True)
        error = traitlets.Unicode("").tag(sync=True)

    battle = mo.ui.anywidget(
        BattleWidget(
            grid_spec={"n_blue": [30, 40, 50], "n_red": [30, 40, 50]},
            runs_per_point=1,
            record_dt=0.2,
        )
    )
    battle
    return (battle,)


@app.cell
def _(battle):
    import polars as pl

    df = pl.DataFrame(battle.results).melt(id_vars=["run_id", "seed", "time"])
    df
    return (df,)


@app.cell
def _(df):
    import altair as alt

    chart = (
        alt.Chart(df)
        .mark_line()
        .encode(x="time:Q", y="value:Q", color="variable:N", detail='run_id')
        .properties(width=640, height=320, title="Army sizes over time")
    )
    chart
    return


if __name__ == "__main__":
    app.run()
