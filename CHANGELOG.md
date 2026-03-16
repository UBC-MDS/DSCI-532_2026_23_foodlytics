## [0.2.0] 

### Added

- App specification: `reports/m2_spec.md`
- Deployment setup to Posit Connect Cloud on main and dev branch
- Basic user interface layout (sidebar + main panel)
- `requirements.txt` for all packages that the app needs
- `reports/m2_spec.md` file 

### Changed

- README.md file with embedded demo animation and deployed link
- Updated app layout compared to M1 sketch to improve usability
- Refined input controls based on M2 spec feedback
- Fixed rendering issues with maps to confine it to Canadian cities
- Corrected data filtering logic (e.g. selecting the city incorrectly called “Branpton”, instead of “Bramption”)
- Updated location selection bar to handle empty selections with a default output state, or cuisine type, or food type


### Fixed

N/A

### Known Issues

N/A


### Reflection

**Job Stories Status**

Fully Implemented:
**Job Story 1**: Comparing and visualizing restaurant density across major Canadian cities to avoid saturated areas.


**Job Story 3**: Analyzing the distribution of cuisine types to identify underserved markets.


Partially Implemented (Revised in M2):

**Job Story 2**: Pricing strategy analysis for Vancouver. The story was refined in M2 to include performance analysis and an average ratings summary card. Core functionality is implemented, but further refinement and advanced analytics are planned for M3.

Pending for M3: further enhancements and potential expansion of performance metrics.


**Comparison to M1 Sketch and M2 Spec**
In Milestone 1, the application consisted primarily of static layout placeholders for the map, bar chart, summary cards, and table.

**Implementation status**
In Milestone 2, these placeholders were replaced with fully functional reactive components. We implemented:
- A new cuisine type selection bar
- Dynamic KPI cards (Total Restaurants, Average Rating)
- Interactive map visualization
- Reactive bar chart
- Filtered restaurant table
- Reset filters functionality


**Deviations**
The overall layout remained consistent with the M1 sketch, but the functionality was significantly improved from static placeholders to a working interactive dashboard
A cuisine type selection bar was added to increase analytical flexibility.
KPI summary cards were enhanced to provide clearer high-level insights.
Some visual components were simplified to ensure stable reactivity and usability.


These deviations were intentional design improvements with the goal of improving the user experience.

**Known Issues**
If no location or cuisine is selected, outputs may display empty results rather than a guiding message.


**Best Practices**
The dashboard follows core visualization best practices:
Minimal color usage to reduce cognitive load.
Avoid unnecessary decorative elements.


**Self Assessment**
Strengths: The filtering system (price range, cuisine type, and location) works cohesively, and all outputs update consistently based on user input. This demonstrates solid logic design and alignment with the original job stories.


Limitations: One limitation is that when no filters are selected, the app displays all restaurants by default. While this ensures that users always see data, it may reduce clarity because the outputs do not explicitly communicate that no filters are applied. A clearer default state or guiding message could improve user understanding.


Future Improvements: From an analytical perspective, the pricing component could be expanded to include more comparative insights.


## [0.3.0] - 2026-03-07

### Added
- A querychat AI chat interface, AI-powered dashboard tab, A dataframe output component to see the filtered dataframe (`#30`)
- 2 other output component visualizations that use the querychat filtered dataframe: Barplot, Total Restaurant + Average Rating features, Adds a data download button that will download the querychat filtered dataframe (`#31`)

### Changed
- README file providing instructions for AI tab feature (`#30`)
- Dependencies in requirements.txt and environment.yml (`#30`)

### Fixed
- Adjusted map size to remove scrolling (`#32`)
- Removed background of the bar plot for better visualization  (`#32`)

### Known Issues
N/A

### Reflection

With the AI-powered dashboard tab, we can type in the chatbot for commanding AI to do simple tasks like filtering the dataset that we have. Furthermore, we can see the responding dataframe with three other visual features: Barplot of "Restaurant Count by Cuisine", Total Restaurants, and Average rating of the filtered restaurants. In addition, we could download the filtered dataframe into a csv file and the resulting barplot into a png file.
One current limitation we have is that the AI chatbot can only do simple task like filtering with obvious command. Improvements can be made by using an Anthropic API key to enhance the AI feature for future projects. There is no intentional deviations from DSCI 531 visualization best practices so far.

## [0.4.0] - 2026-03-15

### Added

- Data pipeline: parquet + DuckDB via ibis and filtering in `@reactive.calc` before data enters a DataFrame (`#46`).
- Script `scripts/convert_to_parquet.py`, `data/processed/restaurants.parquet`, and README instructions for generating parquet (`#46`).
- Advanced feature (Option A): QueryChat customization with custom system prompt, Strategic Focus dropdown (Market Saturation / Pricing Strategy / Cuisine Analysis), `on_tool_request` for tool-call interception including experiment notebook `notebooks/ai_strategy_experiments.ipynb` (`#47`).
- Refactored `filter_data` in `src/filter_data.py`, unit tests `tests/test_filter_data.py`, Playwright tests `tests/test_playwright.py`, and README section for running tests (`#49`).

### Changed

- Spec document updated with M4 additions: parquet/DuckDB pipeline and advanced feature (Option A) motivation and implementation (`reports/m2_spec.md`) via `#50`.
- CONTRIBUTING.md updated with M3 retrospective and M4 collaboration norms (incl. feedback from `#34`) via `#50`.

### Fixed

- Addressed feedback: map sizing and reduced scrollability in AI-Powered Dashboard tab (`#45`) via `#46`.
- Addressed feedback: filtered out restaurants with no ratings/reviews (`#42`) via `#47`
- Addressed feedback: Data coverage dates are not specified (`#41`) addressed via `#49`.
- Addressed feedback: The download button is hard to see (`#43`) via `#50`.

- **Feedback prioritization issue link:** [#39](https://github.com/UBC-MDS/DSCI-532_2026_23_foodlytics/issues/39). We categorized feedback as critical (accuracy/data integrity) or non-critical. One critical-ish item (restaurants with missing ratings/reviews and filter NAs such as "redbull") was addressed. Non-critical items (data coverage dates, AI tab layout, download button visibility) were prioritized for impact on user experience.

### Known Issues

N/A

### Release Highlight: QueryChat Customization (Option A)

The AI-Powered Dashboard tab now lets users choose a **Strategic Focus** (Market Saturation, Pricing Strategy, or Cuisine Analysis). The LLM’s system prompt is updated accordingly so answers emphasize density, price-vs.-rating, or underrepresented cuisines. Tool calls are intercepted via `on_tool_request` for validation/logging. Experiments are documented in `notebooks/ai_strategy_experiments.ipynb`.

- **Option chosen:** A (QueryChat Customization)
- **PR:** #47
- **Why this option over the others:** Our job stories center on saturation, pricing, and cuisine gaps; users need flexible exploration that fixed filters can’t fully provide. We chose Option A over Option D because customizing the LLM’s focus adds more analytical depth than component click interaction. See `#48`.
- **Feature prioritization issue link:** [#48](https://github.com/UBC-MDS/DSCI-532_2026_23_foodlytics/issues/48)

### Collaboration

- **CONTRIBUTING.md:** Updated with M3 retrospective and M4 norms (spread of work, scoped PRs, design before code, reviews) (`#50`)
- **M3 retrospective:** Scoped PRs and docs worked well, code was concentrated with one member (`#34`). We addressed this in M4.
- **M4:** Work distributed across PRs (#46 parquet, #47 advanced feature, #49 tests, and #50 changelog and reflection).

### Reflection

The dashboard now loads data via parquet and DuckDB with filtering at the database level, supports strategic AI queries with a configurable focus, and has documented tests (Playwright for UI behavior, pytest for `get_summary_stats`). Limitations include the need for a GitHub token for the AI tab and dataset size assumptions in tests. No intentional deviations from DSCI 531 visualization practices.

**Tests.** The unit tests (`test_summary_stats`) cover the `get_summary_stats` function: they check the output dictionary structure, accurate values of total number of restaurants and average rating across various dataset sizes, and edge cases like empty data frame as an input. The Playwright tests ensure the dashboard shows the full dataset in its original state on load, that applying one or multiple filters produces the expected counts and table, and that the reset button restores the original dataset and value boxes. *What could break:* If `get_summary_stats` or the summary logic changes, the unit tests would fail and the value boxes for total restaurants and average rating could become inaccurate. If the initial state, filter behavior, or reset logic changes, the Playwright tests would fail and users could see inaccurate filtered data or lose the ability to return to the original state, and dashboard behavior would no longer match what we expect.

**Trade-offs:** We prioritized feedback that affected accuracy (e.g. missing ratings/reviews and filter NAs) or user experience (coverage dates, layout, button visibility). Full categorization and rationale are in [#39](https://github.com/UBC-MDS/DSCI-532_2026_23_foodlytics/issues/39). Critical items were resolved first, with at least one item per team member.

**Most useful:** Lecture 7 and Lecture 8 were the most useful for M4. Lecture 7 (parquet and DuckDB) guided our data pipeline refactor: switching to parquet, connecting with ibis + DuckDB, and keeping filtering in `@reactive.calc` before data becomes a DataFrame. Lecture 8 shaped how we added the refactored `filter_data` unit tests and the Playwright tests for initial state, filters, and reset behavior.