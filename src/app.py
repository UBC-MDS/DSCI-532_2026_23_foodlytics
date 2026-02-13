from shiny import App, ui

# Placeholders
app_ui = ui.page_fillable(
    ui.panel_title("FOODLYTICS"),
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
                selected=["Italian" ]      
            ),
            ui.input_select(
                id="city",
                label="Location",
                choices=["Vancouver", "Toronto", "Calgary", "Montreal"],
                multiple=True,
                selected="Vancouver"       
            ),
            ui.input_action_button("reset_filters", "Reset filters"),
            open="desktop",
        ),
        ui.main_panel(
            ui.row(
                ui.value_box("Total Restaurants", "12"),
                ui.value_box("Average Rating", "8.5"),
            ),
            ui.row(
                ui.column(
                    6,
                    ui.card(
                        ui.card_header("Map Visual Placeholder"),
                        ui.output_widget("map")
                        )
            ),
                ui.column(
                        6,
                        ui.card(
                            ui.card_header("Bar Chart Placeholder"),
                            ui.output_widget("bar_chart")
                            )
                        )
                ),
            ui.row(
                ui.column(
                    12,
                    ui.card(
                        ui.card_header("Restaurant Table Placeholder"),
                        ui.output_widget("restaurant_table")
            )
        )
    )
)
    ),
)

def server(input, output, session):
    pass

app = App(app_ui, server)
