# Foodlytics

This dashboard visualizes restaurant quality and type across Canada’s main cities, including cuisine categories and price ranges. It is aimed at businesses and entrepreneurs planning to open a new restaurant. The app helps users understand the local restaurant landscape so they can make better decisions about where to open and what type of restaurant to offer.

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

4. **Start the dashboard:**
   ```bash
   shiny run src/app.py
   ```
   Open the URL shown in the terminal (e.g. http://127.0.0.1:8000) in your browser.

## Contributors

* **Valeria Siciliano** ([@Valeria-mds](https://github.com/Valeria-mds))
* **Cynthia Limantono** ([@cynthiaagata](https://github.com/cynthiaagata))
* **Rabin Duran** ([@rabin0208](https://github.com/rabin0208))
* **Shanze Khemani** ([@shanzekhem](https://github.com/shanzekhem))


## Copyright

- Copyright © 2026 Valeria Siciliano, Cynthia Limantono, Rabin Duran, Shanze Khemani.
- Free software distributed under the [MIT License](./LICENSE.md).