"""
Download dataset from Kaggle and save to data/raw.
Used by the Foodlytics dashboard. Run once before starting the app.

Requires Kaggle API credentials:
  - Set KAGGLE_API_TOKEN (from https://www.kaggle.com/settings, Create New Token), or
  - Place kaggle.json in ~/.kaggle/ (legacy).
"""

import os
from pathlib import Path

# Dataset from the "Analyze Food Delivery in Canada - Door Dash" notebook.
KAGGLE_DATASET = "satoshiss/food-delivery-in-canada-door-dash"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        raise ImportError("Install the Kaggle API: pip install kaggle")

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(KAGGLE_DATASET, path=str(RAW_DIR), unzip=True)
    print(f"Downloaded dataset to {RAW_DIR}")


if __name__ == "__main__":
    main()