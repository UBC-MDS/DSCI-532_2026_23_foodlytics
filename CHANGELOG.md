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


### Fixed

N/A

### Known Issues

- Updated location selection bar to handle empty selections with a default output state, or cuisine type, or food type


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

