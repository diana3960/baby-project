import pandas as pd

netflix_df = pd.read_csv("Clean_data/netflix_titles.csv")
regions_df = pd.read_csv("data/country_regions.csv")

netflix_df["country"] = netflix_df["country"].str.strip()
regions_df["country"] = regions_df["country"].str.strip()

merged_df = pd.merge(
    netflix_df,
    regions_df,
    on="country",
    how="left"
)

merged_df.to_csv("results/merged_output.csv", index=False)

print("Merge completed successfully.")
