# App Specification

## 2.1 Updated Job Stories

| # | Job Story | Status | Notes |
|---|-----------|--------|-------|
| 1 | When I am evaluating potential restaurant locations across the main Canadian cities, I want to compare and visualize restaurant density so I can avoid opening a restuarant in saturated areas. | ⏳ Pending M2 |  |
| 2 | When I am developing a pricing strategy for the city of Vancouver, I want to analyze restaurants' price ranges and performance so I can create a competitive pricing strategy | ⏳ Pending M2 |  |
| 3 | When I am deciding what type of restaurant to open, I want to analyze the distribution of different cuisine types so I can identify underserved markets | ⏳ Pending M2 |  |

## 2.2 Component Inventory

The following table describes every input, reactive calc, and output the Foodlytics app will have.

| ID | Type | Shiny widget / renderer | Depends on | Job story |
|----|------|-------------------------|------------|------------|
| input_city | Input | `ui.input_select()` | — | #1, #2 #3|
| input_cuisine | Input | `ui.input_select()` | — | #1 #3|
| input_price_range | Input | `ui.input_select()` | — | #2|
| filtered_df | Reactive calc | `@reactive.calc` | input_city, input_cuisine, input_price_range | #1, #2, #3 |
| summary_stats | Reactive calc | `@reactive.calc` | filtered_df | #1, #2 |
| card_total_restaurants | Output | `render.text()` | summary_stats | #1|
| card_avg_rating | Output | `render.text()` | summary_stats | #2|
| plot_bar_cuisine | Output | `@render.plot` | filtered_df | #3 |
| plot_map | Output | `@render.plot` | filtered_df | #1 |
| tbl_restaurants | Output | `@render.data_frame` | filtered_df | #2 |

## 2.3 Reactivity Diagram

## 2.4 Calculation Details
