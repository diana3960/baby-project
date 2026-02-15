import pandas as pd

# ----------------------------
# Load cleaned Netflix dataset
# ----------------------------
netflix_df = pd.read_csv("Clean_data/netflix_titles.csv")

# ----------------------------
# Load country to region dataset
# ----------------------------
regions_df = pd.read_csv("data/country_regions.csv")

# ----------------------------
# Clean country column (remove extra spaces)
# ----------------------------
netflix_df["country"] = netflix_df["country"].str.strip()
regions_df["country"] = regions_df["country"].str.strip()

# ----------------------------
# Merge datasets using LEFT join
# This keeps all Netflix records
# ----------------------------
merged_df = pd.merge(
    netflix_df,
    regions_df,
    on="country",
    how="left"
)

# ----------------------------
# Save merged file
# ----------------------------
merged_df.to_csv("results/merged_output.csv", index=False)

print("Merge completed successfully.")
