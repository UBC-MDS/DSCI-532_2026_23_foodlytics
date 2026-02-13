from shiny import App, ui, render
import pandas as pd

# Placeholders
app_ui = ui.page_fillable(
    ui.h1("FOODLYTICS", style = "color: darkblue;"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_checkbox_group(
                id="price_range",
                label="Price Range",
                choices=["$", "$$", "$$$", "$$$$"],
                selected=["$$"],
            ),
            ui.input_select(
                id="cuisine",
                label="Cuisine Type",
                choices=["Italian", "Chinese", "Mexican"],
                multiple=True,
                selected=["Italian"]      
            ),
            ui.input_select(
                id="city",
                label="Location",
                choices=["Vancouver", "Toronto", "Calgary", "Montreal"],
                multiple=True,
                selected=["Vancouver"]      
            ),
            ui.input_action_button("reset_filters", "Reset filters"),
            open="desktop"
        ),

        ui.row(
            ui.column(6,
                      ui.value_box("Total Restaurants", "12")),
            ui.column(6,
                      ui.value_box("Average Rating", "8.5"))
        ),
        ui.row(
            ui.column(
                6,
                ui.card(
                    ui.card_header("Map Visual Placeholder"),
                    ui.output_text("map"),
                    full_screen=True
                )
            ),
            ui.column(
                6,
                ui.card(
                    ui.card_header("Bar Chart Placeholder"),
                    ui.output_text("bar_chart"),
                    full_screen=True
                )
            )
        ),
        ui.row(
            ui.column(
                12,
                ui.card(
                    ui.card_header("Restaurant Table Placeholder"),
                    ui.output_data_frame("restaurant_table"),
                    full_screen=True
                )
            )
        )
    )
)

def server(input, output, session):

    @render.text
    def map():
        return "Map displaying selected locations will appear here."

    @render.text
    def bar_chart():
        return "Bar chart showing the distribution of food types based on the applied filters will appear here."

    @render.data_frame
    def restaurant_table():
        return pd.DataFrame({
            "Restaurant Name": ["Subway", "McDonalds", "Cactus Club Cafe"],
            "Stars": [3.0, 4.5, 5.0],
            "# of Reviews": [4056, 10050, 8000]
            })

app = App(app_ui, server)
