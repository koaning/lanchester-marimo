import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl
    return (pl,)


@app.cell
def _():
    import marimo as mo
    from battle_widget import BattleWidget

    battle = mo.ui.anywidget(
        BattleWidget(
            grid_spec={"n_blue": list(range(30, 100, 1)), "n_red": [30]},
            runs_per_point=1,
            seed_mode="random",
            base_seed=1,
            arena_width=640,
            arena_height=420,
            unit_radius=4.0,
            spawn_mode="sides",  # "sides" | "mixed"
            step_dt=0.02,
            move_speed=55.0,
            attack_range=10.0,
            attack_cooldown=0.1,
            hit_chance=0.85,
            damage=1,
            hp=20,
            max_time=30.0,
            record_dt=0.2,
            render=True,
        )
    )
    battle
    return battle, mo


@app.cell
def _(battle, pl):
    pl.DataFrame(battle.results).with_columns(diff=pl.col("n_blue") - pl.col("n_red")).plot.line(x="time", y="n_blue", detail="run_id")
    return


@app.cell
def _(battle, pl):
    (
        pl.DataFrame(battle.results)
            .group_by("run_id")
            .agg(
                pl.col("n_blue").max().alias("blue_max"),
                pl.col("n_blue").min().alias("blue_min"),
                pl.col("n_red").max().alias("red_max"),
                pl.col("n_red").min().alias("red_min"),
            )
            .with_columns(
                blue_diff = pl.col("blue_max") - pl.col("blue_min"),
                red_diff = pl.col("red_max") - pl.col("red_min"),
            )
            .with_columns(
                start_diff = pl.col("blue_max") - pl.col("red_max"),
            )
            .plot.scatter("start_diff", "blue_min")
    )
    return


@app.cell
def _(battle, pl):
    (
        pl.DataFrame(battle.results)
            .group_by("run_id")
            .agg(
                pl.col("n_blue").max().alias("blue_max"),
                pl.col("n_blue").min().alias("blue_min"),
                pl.col("n_red").max().alias("red_max"),
                pl.col("n_red").min().alias("red_min"),
            )
            .with_columns(
                blue_diff = pl.col("blue_max") - pl.col("blue_min"),
                red_diff = pl.col("red_max") - pl.col("red_min"),
            )
            .with_columns(
                start_diff = pl.col("blue_max") - pl.col("red_max"),
            )
            .plot.scatter("blue_max", "blue_min")
    )
    return


@app.cell
def _(battle, pl):
    (
        pl.DataFrame(battle.results)
            .group_by("run_id")
            .agg(
                pl.col("n_blue").max().alias("blue_max"),
                pl.col("n_blue").min().alias("blue_min"),
                pl.col("n_red").max().alias("red_max"),
                pl.col("n_red").min().alias("red_min"),
            )
            .with_columns(
                expected_blue_min = (pl.col("blue_max")**2 - pl.col("red_max")**2).sqrt(),
            )
            .plot.scatter("expected_blue_min", "blue_min")
    )
    return


@app.cell
def _(battle, pl):
    df = pl.DataFrame(battle.results).melt(id_vars=["run_id", "seed", "time"])
    return (df,)


@app.cell
def _(df, mo):
    dropdown = mo.ui.dropdown(df["run_id"].unique())
    dropdown
    return (dropdown,)


@app.cell
def _(df, dropdown, mo, pl):
    import altair as alt

    mo.stop(dropdown.value == "")

    run_id = dropdown.value

    _df = df.filter(pl.col("run_id") == run_id)

    chart = (
        alt.Chart(_df)
        .mark_line()
        .encode(x="time:Q", y="value:Q", color="variable:N", detail='run_id')
        .properties(width=640, height=320, title="Army sizes over time")
    )
    chart
    return


if __name__ == "__main__":
    app.run()
