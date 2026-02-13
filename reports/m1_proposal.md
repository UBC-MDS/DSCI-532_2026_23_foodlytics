## Section 1: Motivation and Purpose

## Section 2: Description of the Data

## Section 3: Research Questions & Usage Scenarios

### Persona
This application is designed for a prospective restaurant owner with prior experience running a small business. They are exploring opportunities to open a new restaurant in a major Canadian city and want to make informed, data-driven decisions before investing.
As a cautious and strategic entrepreneur, they prefer to rely on structured market data rather than intuition alone. Their primary objective is to identify a neighborhood where their restaurant can thrive — one with sufficient demand, manageable competition, and strong potential for profitability. They are particularly interested in understanding market saturation by cuisine type and price range. By identifying under served food categories within specific neighborhoods, they aim to fill a market gap and position their business competitively.
Key challenges include navigating local competition, avoiding over saturated cuisine segments, and minimizing financial risk in a highly competitive industry.

### Usage Scenario
Daniel is an entrepreneur who is thinking about opening a Mediterranean restaurant in downtown Vancouver. Before signing the lease, he wants to make sure that the area is not too competitive and that the price range of nearby restaurants matches his idea.
To make a better decision, he uses the app “Foodlytics” to explore the data. He filters by location, type of cuisine, ratings, and price range to understand how many similar restaurants already exist in that neighborhood.
After reviewing the results, he realizes that downtown has many mid-range Mediterranean restaurants. However, a nearby neighborhood has fewer competitors in the same category. Based on this information, Daniel adjusts his business plan and considers opening his restaurant in the less saturated area to reduce risk and increase his chances of success.

### User Stories
- **User Story 1:** 
As an **entrepreneur in the food industry**, I am evaluating how to compare and visualize restaurant density across the neighborhoods of the main cities of Canada, in order to avoid saturated areas.
- **User Story 2:**
A **business investor** is seeking information regarding the price ranges in the city of Vancouver to determine a good pricing strategy.
- **User story 3:**
A **prospective restaurant owner** is evaluating the distribution of the different types of cuisine, so they can provide a better service in a lacking market.

## Section 4: Exploratory Data Analysis
To address User Story 1 (Restaurant Density), we analyzed the number of restaurants across major Canadian cities.

**Analysis**

The bar chart in notebooks/eda_analysis.ipynb shows clear differences in restaurant concentration between cities. Vancouver and Toronto display the highest number of restaurants, while cities such as Winnipeg and Ottawa have comparatively lower concentrations.

**Reflection**

This finding supports the need for a city-level comparison filter in the dashboard. By allowing entrepreneurs to visualize and compare restaurant density across cities, they can identify highly saturated markets versus less competitive ones. This helps decision-makers evaluate whether entering a dense market requires strong differentiation or whether a lower-density city may offer a better opportunity for new restaurant entry.



## Section 5: App Sketch & Description

