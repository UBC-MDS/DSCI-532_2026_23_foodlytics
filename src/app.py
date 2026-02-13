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
                selected="Italian"       
            ),
            ui.input_select(
                id="city",
                label="Location",
                choices=["Vancouver", "Toronto", "Calgary", "Montreal"],
                multiple=True,
                selected="Vancouver"       
            ),
            ui.input_select("reset_filters", "Reset filters"),
            open="desktop",
        ),
    ),
)

def server(input, output, session):
    pass

app = App(app_ui, server)
