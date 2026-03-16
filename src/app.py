from pathlib import Path

import altair as alt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import chatlas as clt
import querychat
from dotenv import load_dotenv
from shiny import App, ui, render, reactive
from shinywidgets import output_widget, render_altair, render_widget
from vega_datasets import data as vega_data
from faicons import icon_svg
from filter_data import filter_data


_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

# Load data
def get_data():
    df = pd.read_csv(_DATA_DIR / "cleaned_full_data.csv")
    df["city"] = df["city"].str.replace("Branpton", "Brampton", regex=False)
    return df

# QueryChat setup for Dashboard 
load_dotenv()
df = get_data()
chat = querychat.QueryChat(
    df, 
    "foodlytics",
    client=clt.ChatGithub(model="gpt-4.1-mini")
)

def get_cities_coords():
    coords = pd.read_csv(_DATA_DIR / "cities_coordinates.csv")
    coords["City"] = coords["City"].str.replace("Branpton", "Brampton", regex=False)
    return coords

CITIES_COORDS = get_cities_coords()

# Canada-only base
countries_topo = alt.topo_feature(vega_data.world_110m.url, "countries")

# Filter choices from data
CITIES = sorted(df["city"].dropna().unique().tolist())
CUISINES = sorted(df["category_1"].dropna().unique().tolist())
PRICE_RANGES = sorted(df["price_range"].dropna().unique().tolist())
CATEGORY_2 = sorted(df["category_2"].dropna().unique().tolist())

# Footer content
REPO_URL = "https://github.com/UBC-MDS/DSCI-532_2026_23_foodlytics"
KAGGLE_URL = "https://www.kaggle.com/datasets/satoshiss/food-delivery-in-canada-door-dash"
APP_DESCRIPTION = (
    "Foodlytics visualizes restaurant quality and type across Canada's main cities. "
    "Intended for businesses and entrepreneurs planning to open a new restaurant."
)
AUTHORS = "Valeria Siciliano, Cynthia Limantono, Rabin Duran, Shanze Khemani"
LAST_UPDATED = "March 2026"
DATA_DESCRIPTION = "Last updated: 2022"

# Overall (full-dataset) stats for value-box comparisons
OVERALL_N = len(df)
OVERALL_AVG = float(df["star"].mean())

# Baseline for "total restaurants" comparison: average per city
AVG_RESTAURANTS_PER_CITY = OVERALL_N / len(CITIES) if CITIES else 0


def compare(current, baseline, higher_is_better=True, vs_label="overall avg"):
    """
    Classify current vs baseline — five states:
      significantly above / slightly above / stable / slightly below / significantly below
    Thresholds: change < 1%: stable, 1–5%: slight, > 5%: significant
    Returns dict(icon, theme, badge, label) for value_box.
    """
    if baseline == 0 or pd.isna(current):
        return dict(icon="circle-minus", theme="secondary", badge="no data", label="no data")

    pct = (current - baseline) / abs(baseline) * 100
    is_good = (pct > 0) if higher_is_better else (pct < 0)
    abs_pct = abs(pct)

    sign = "+" if pct >= 0 else ""
    badge = f"{sign}{current - baseline:.1f} ({sign}{pct:.1f}%) vs {vs_label}"

    if abs_pct < 1:
        return dict(icon="arrow-right", theme="secondary", badge="≈ stable vs " + vs_label, label="stable")

    icon = "arrow-trend-up" if pct > 0 else "arrow-trend-down"
    theme = (
        "success" if (is_good and abs_pct >= 5) else
        "teal" if is_good else
        "danger" if abs_pct >= 5 else
        "warning"
    )
    quantifier = "significantly" if abs_pct >= 5 else "slightly"
    label = f"{quantifier} {'above' if pct > 0 else 'below'} avg"
    return dict(icon=icon, theme=theme, badge=badge, label=label)


def kpi_showcase(cmp):
    """FA icon for the value-box showcase panel — inherits theme colour."""
    return icon_svg(cmp["icon"], height="2.5em", fill_opacity="0.85")


def kpi_caption(cmp):
    """Delta badge + five-state label rendered below the value."""
    return ui.tags.div(
        ui.HTML(f'<strong style="opacity:0.9">{cmp["badge"]}</strong>'),
        ui.div(cmp.get("label", ""), style="opacity:0.7;font-size:0.8rem;margin-top:2px"),
    )


# ── UI ──────────────────────────────────────────────────────────────
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Foodlytics Dashboard",
        ui.page_fillable(
            ui.h1("FOODLYTICS", style="color: darkblue;"),
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_checkbox_group(
                        id="price_range",
                        label="Price Range",
                        choices=PRICE_RANGES,
                        selected=PRICE_RANGES,
                    ),
                    ui.input_select(
                        id="cuisine",
                        label="Cuisine / restaurant type",
                        choices=CUISINES,
                        multiple=True,
                        selected=CUISINES,
                    ),
                    ui.input_select(
                        id="city",
                        label="Location",
                        choices=CITIES,
                        multiple=True,
                        selected=CITIES,
                    ),
                    ui.input_select(
                        id="category_2",
                        label="Dish / food type",
                        choices=CATEGORY_2,
                        multiple=True,
                        selected=CATEGORY_2,
                    ),
                    ui.input_action_button("reset_filters", "Reset filters"),
                    open="desktop",
                ),

                # Row 1: KPI value boxes (from summary_stats)
                ui.output_ui("kpi_boxes"),

                # Row 2: Map + Bar chart (from filtered_df)
                ui.row(
                    ui.column(
                        6,
                        ui.card(
                            ui.card_header("Map Visual"),
                            output_widget("map"),
                            full_screen=True,
                        ),
                    ),
                    ui.column(
                        6,
                        ui.card(
                            ui.card_header("Restaurant count by cuisine"),
                            output_widget("plot_bar_cuisine"),
                            full_screen=True,
                        ),
                    ),
                ),

                # Row 3: Table (from filtered_df)
                ui.row(
                    ui.column(
                        12,
                        ui.card(
                            ui.card_header("Restaurants"),
                            ui.output_data_frame("tbl_restaurants"),
                            full_screen=True,
                        ),
                    ),
                ),

                # Footer
                ui.tags.footer(
                    ui.tags.div(
                        ui.tags.p(APP_DESCRIPTION, style="margin-bottom:0.5rem;"),
                        ui.tags.p(
                            "Authors: " + AUTHORS,
                            style="margin-bottom:0.25rem;font-size:0.9rem;",
                        ),
                        ui.tags.p(
                            "Data Source: ", 
                            ui.tags.a(
                                "Kaggle ",
                                href=KAGGLE_URL,
                                target="_blank",
                                rel="noopener",
                                ), 
                             " · " + DATA_DESCRIPTION + " ",
                            style="margin-bottom:0;font-size:0.9rem;",
                        ),
                        ui.tags.p(
                            ui.tags.a(
                                "Repository",
                                href=REPO_URL,
                                target="_blank",
                                rel="noopener",
                            ),
                            " · Last updated: " + LAST_UPDATED,
                            style="margin-bottom:0;font-size:0.9rem;",
                        ),
                        style="padding:1rem 0;border-top:1px solid #dee2e6;color:#6c757d;font-size:0.85rem;",
                    ),
                    style="margin-top:1.5rem;",
                ),
            ),
        ),
    ),
    ui.nav_panel(
        "AI-Powered Dashboard",
        ui.page_sidebar(
            chat.sidebar(),
            ui.card(
                ui.card_header(ui.output_text("title")),
                ui.output_data_frame("data_table"),
                ui.download_button("download_ai_data", "Download filtered data", class_="mt-2"),
                fill=True,
            ),
            ui.output_ui("ai_kpi_boxes"),
            ui.row(
                ui.column(
                    12,
                    ui.card(
                        ui.card_header("Restaurant count by cuisine (AI-filtered)"),
                        output_widget("ai_plot_bar_cuisine"),
                        full_screen=True,
                    ),
                ),
            ),
            fillable=True,
            title="Foodlytics QueryChat"
        )
    )
)


# ── Server ────────────────────────────────────────────────────────────
def server(input, output, session):
    @reactive.calc
    def filtered_df():
        data = df.copy()
        cities = input.city()
        cuisines = input.cuisine()
        price_ranges = input.price_range()
        categories_2 = input.category_2()
        return filter_data(data, cities, cuisines, price_ranges, categories_2)

    @reactive.calc
    def summary_stats():
        data = filtered_df()
        n = len(data)
        avg = data["star"].mean() if n else 0.0
        return {"n_restaurants": n, "avg_rating": avg}

    @render.ui
    def kpi_boxes():
        stats = summary_stats()
        n, avg = stats["n_restaurants"], stats["avg_rating"]
        # No matches: neutral "no data" state instead of red
        if n == 0:
            no_data = dict(
                icon="circle-minus",
                theme="secondary",
                badge="No restaurants match the selected filters.",
                label="no data",
            )
            cmp_n = cmp_avg = no_data
        else:
            cmp_n = compare(n, AVG_RESTAURANTS_PER_CITY, higher_is_better=True, vs_label="avg per city")
            cmp_avg = compare(avg, OVERALL_AVG, higher_is_better=True)
        return ui.row(
            ui.column(
                6,
                ui.value_box(
                    "Total Restaurants",
                    str(n),
                    kpi_caption(cmp_n),
                    showcase=kpi_showcase(cmp_n),
                    theme=cmp_n["theme"],
                    id="total_res",
                ),
            ),
            ui.column(
                6,
                ui.value_box(
                    "Average Rating",
                    "—" if n == 0 else f"{avg:.1f}",
                    kpi_caption(cmp_avg),
                    showcase=kpi_showcase(cmp_avg),
                    theme=cmp_avg["theme"],
                    id="avg_rating",
                ),
            ),
        )

    @render_altair
    def map():
        data = filtered_df()
        proj = "equalEarth"  # fixed per M2 spec (no projection input)

        # Canada only
        base = (
            alt.Chart(countries_topo)
            .mark_geoshape(fill="#e0e0e0", stroke="white", strokeWidth=0.5)
            .transform_filter(alt.datum.id == 124)
        )

        if data.empty:
            return (
                base.project(type=proj)
                .properties(width=420, height=380, title="Restaurant count by city — Canada")
            )

        # Aggregate by city: restaurant count and total reviews
        by_city = (
            data.groupby("city")
            .agg(count=("restaurant", "size"), total_reviews=("num_reviews", "sum"))
            .reset_index()
        )
        by_city["total_reviews"] = by_city["total_reviews"].fillna(0).astype(int)
        coords = CITIES_COORDS.rename(columns={"City": "city"})
        map_df = by_city.merge(coords, on="city", how="inner")
        if map_df.empty:
            return (
                base.project(type=proj)
                .properties(width="container", height=380, title="Restaurant count by city — Canada")
            )

        # Data-driven layer: size = restaurants, color = total reviews
        points = (
            alt.Chart(map_df)
            .mark_circle(size=120)
            .encode(
                longitude="Longitude:Q",
                latitude="Latitude:Q",
                size=alt.Size("count:Q").scale(range=[80, 300]).legend(None),
                color=alt.Color("total_reviews:Q")
                .scale(scheme="blues", type="linear")
                .legend(title="# of reviews"),
                tooltip=[
                    alt.Tooltip("city:N", title="City"),
                    alt.Tooltip("count:Q", title="Restaurants"),
                    alt.Tooltip("total_reviews:Q", title="# of reviews", format=","),
                ],
            )
        )

        return (
            alt.layer(base, points)
            .project(type=proj)
            .properties(width=420, height=360, title="Restaurant count by city — Canada")
        )

    @render_widget
    def plot_bar_cuisine():
        data = filtered_df()
        if data.empty:
            fig = go.Figure()
            fig.add_annotation(
                text="No restaurants match the selected filters.",
                xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False,
                font=dict(size=14),
            )
            fig.update_layout(height=400, xaxis=dict(visible=False), yaxis=dict(visible=False))
            return fig
        else:
            agg = data["category_1"].value_counts().reset_index()
            agg.columns = ["cuisine", "count"]
            agg = agg.sort_values("count", ascending=True).tail(20)
            fig = px.bar(
                agg,
                x="count",
                y="cuisine",
                orientation="h",
                labels={"count": "Number of restaurants", "cuisine": "Cuisine"},
                color="count",
                color_continuous_scale="blues",
            )
            fig.update_layout(showlegend=False, height=400, margin=dict(l=20, r=20, t=20, b=20),
                              plot_bgcolor="white",
                              paper_bgcolor="white")
        return fig

    @render.data_frame
    def tbl_restaurants():
        data = filtered_df()
        out = data[["restaurant", "star", "num_reviews", "city", "price_range", "category_1", "category_2"]].copy()
        out = out.rename(columns={"restaurant": "Restaurant", "star": "Stars", "num_reviews": "# of Reviews"})
        return out

    @reactive.effect
    @reactive.event(input.reset_filters)
    def _():
        input.reset_filters()
        ui.update_checkbox_group("price_range", selected=PRICE_RANGES)
        ui.update_select("cuisine", selected=CUISINES)
        ui.update_select("city", selected=CITIES)
        ui.update_select("category_2", selected=CATEGORY_2)

    # AI server
    qc_vals = chat.server()

    @render.text
    def title():
        return qc_vals.title() or "AI Filtered Dataframe"

    @render.data_frame
    def data_table():
        return qc_vals.df()

    # AI tab: value boxes and bar chart from querychat filtered dataframe
    @render.ui
    def ai_kpi_boxes():
        data = qc_vals.df()
        n = len(data) if not data.empty else 0
        avg = float(data["star"].mean()) if not data.empty and "star" in data.columns else 0.0
        if n == 0:
            no_data = dict(
                icon="circle-minus",
                theme="secondary",
                badge="No restaurants in AI filter result.",
                label="no data",
            )
            cmp_n = cmp_avg = no_data
        else:
            cmp_n = compare(n, AVG_RESTAURANTS_PER_CITY, higher_is_better=True, vs_label="avg per city")
            cmp_avg = compare(avg, OVERALL_AVG, higher_is_better=True)
        return ui.row(
            ui.column(
                6,
                ui.value_box(
                    "Total Restaurants",
                    str(n),
                    kpi_caption(cmp_n),
                    showcase=kpi_showcase(cmp_n),
                    theme=cmp_n["theme"],
                ),
            ),
            ui.column(
                6,
                ui.value_box(
                    "Average Rating",
                    "—" if n == 0 else f"{avg:.1f}",
                    kpi_caption(cmp_avg),
                    showcase=kpi_showcase(cmp_avg),
                    theme=cmp_avg["theme"],
                ),
            ),
        )

    @render_widget
    def ai_plot_bar_cuisine():
        data = qc_vals.df()
        if data.empty or "category_1" not in data.columns:
            fig = go.Figure()
            fig.add_annotation(
                text="No data or no cuisine column. Try a query in the chat.",
                xref="paper", yref="paper", x=0.5, y=0.5, showarrow=False,
                font=dict(size=14),
            )
            fig.update_layout(height=400, xaxis=dict(visible=False), yaxis=dict(visible=False))
            return fig
        agg = data["category_1"].value_counts().reset_index()
        agg.columns = ["cuisine", "count"]
        agg = agg.sort_values("count", ascending=True).tail(20)
        fig = px.bar(
            agg,
            x="count",
            y="cuisine",
            orientation="h",
            labels={"count": "Number of restaurants", "cuisine": "Cuisine"},
            color="count",
            color_continuous_scale="blues",
        )
        fig.update_layout(showlegend=False, height=400, margin=dict(l=20, r=20, t=20, b=20),
                              plot_bgcolor="white",
                              paper_bgcolor="white")
        return fig

    @render.download(filename="querychat_filtered_data.csv")
    def download_ai_data():
        data = qc_vals.df()
        yield data.to_csv(index=False)

app = App(app_ui, server)

# For local testing
if __name__ == "__main__":
    from shiny import run_app
    run_app(app, host="127.0.0.1", port=8000)
