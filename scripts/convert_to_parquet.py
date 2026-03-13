import pandas as pd

# Load processed CSV
df = pd.read_csv("data/processed/restaurants.csv")

# Convert to parquet
df.to_parquet("data/processed/restaurants.parquet", index=False)

print("Parquet file created successfully.")