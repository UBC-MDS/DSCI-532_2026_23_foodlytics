# Foodlytics

This dashboard visualizes restaurant quality and type across Canada’s main cities, including cuisine categories and price ranges. It is aimed at businesses and entrepreneurs planning to open a new restaurant. The app helps users understand the local restaurant landscape so they can make better decisions about where to open and what type of restaurant to offer.

### Motivation
Opening a restaurant involves high financial risk and strategic planning.
Business owners need reliable data to understand which cuisine types are more preferred, which neighborhoods attract more customers, and where market opportunities exist.

Foodlytics helps entrepreneurs and investors explore restaurant data to make informed, data-driven decisions before choosing a location or cuisine focus.

### What This Dashboard Solves
Foodlytics allows users to:
- Explore restaurant ratings and review patterns
- Compare locations and price ranges
- Identify trends in customer feedback
- Filter restaurants based on specific preferences

## Run the dashboard locally

1. **Clone the repository** and go into the project folder:
   ```bash
   git clone https://github.com/UBC-MDS/DSCI-532_2026_23_foodlytics.git
   cd DSCI-532_2026_23_foodlytics
   ```

2. **Create and activate the conda environment:**
   ```bash
   conda env create -f environment.yml
   conda activate dsci532
   ```

3. **Download the data (optional)**:
   - Get a Kaggle API token from [Kaggle → Account → Create New Token](https://www.kaggle.com/settings), then set it:
     ```bash
     export KAGGLE_API_TOKEN=your_token_here
     ```
   - Run the download script:
     ```bash
     python src/download_data.py
     ```
   Data will be saved to `data/raw/` (including `cleaned_full_data.csv`).

4. **Convert to parquet**
   For faster loading of the file, the dashboard reads the dataset from a parquet file, so the user can find it already converted here:
   ```bash
   data/processed/restaurants.parquet
   ```

   In alternative, the user can generate the parquet file from the processed .csv by running the following:
   ```bash
   python scripts/convert_to_parquet.py
   ```
   so the dataset will be converted to parquet format and saved in data/processed/restaurants.parquet

5. **Set up the AI-Powered Dashboard tab (optional)**  
   The app includes an AI tab that uses GitHub's model marketplace. To use it:
   - Copy the example env file and add your token:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and set `GITHUB_TOKEN` to a [GitHub Personal Access Token (classic)](https://github.com/settings/tokens). Create one under **Settings → Developer settings → Personal access tokens → Tokens (classic)**. A short expiration (e.g. 30 days) and no scopes are usually enough for local use.
   - Do not commit `.env`; it is listed in `.gitignore`.

6. **Start the dashboard:**
   ```bash
   shiny run src/app.py
   ```
   Open the URL shown in the terminal (e.g. http://127.0.0.1:8000) in your browser.

## Running Tests

There are two tests: 
- **Unit test** `test_summary_stats.py`: tests the `get_summary_stats` function in isolation, covering output dictionary structure, accurate values of total number of restaurants and average rating across various data set sizes, and edge cases like empty data frame as an input.
- **Playwright test** `test_playwright.py`: tests the dashboard UI behavior including the initial state of value boxes and the data table, filter interactions, and the reset button restoring the full data set.

**How to run all tests:**
```bash
# 1. Set up the environment
conda env create -f environment.yml
conda activate dsci532

# 2. Install Playwright
playwright install chromium

# 3. Run tests
pytest
```

If you wish to run tests separately, please make sure you have set up the environment and installed playwright (step 1 and 2 above) before running the following code.
**Only unit test:** 
```bash
pytest tests/test_summary_stats.py
```

**Only playwright test:**
```bash
pytest tests/test_playwright.py
```

### Live Dashboard
You can access the stable deployed dashboard here:
https://cynthiaagata-dsci-532-2026-23-foodlytics.share.connect.posit.cloud/
If you wish to see the preview link, you can access it here:
https://cynthiaagata-dsci-532-2026-23-foodlytics-dev.share.connect.posit.cloud

### Demo
Below is a short demo of the dashboard in action:
![App Demo](img/demo.mp4)


## Contributors

* **Valeria Siciliano** ([@Valeria-mds](https://github.com/Valeria-mds))
* **Cynthia Limantono** ([@cynthiaagata](https://github.com/cynthiaagata))
* **Rabin Duran** ([@rabin0208](https://github.com/rabin0208))
* **Shanze Khemani** ([@shanzekhem](https://github.com/shanzekhem))

To contribute to the Foodlytics app, please read and follow the guidelines in [CONTRIBUTING.md](./CONTRIBUTING.md). To run the app locally, follow the steps in the "Run the dashboard locally" section above.

## Copyright

- Copyright © 2026 Valeria Siciliano, Cynthia Limantono, Rabin Duran, Shanze Khemani.
- Free software distributed under the [MIT License](./LICENSE.md).
