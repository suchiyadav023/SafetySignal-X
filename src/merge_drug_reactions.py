from pathlib import Path
import pandas as pd

# Project folders
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "data" / "processed"
OUTPUT_FOLDER = PROJECT_FOLDER / "outputs"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

print("Loading drug data...")
drug_data = pd.read_csv(
    DATA_FOLDER / "drug_data.csv",
    low_memory=False
)

print("Loading reaction data...")
reaction_data = pd.read_csv(
    DATA_FOLDER / "reaction_data.csv",
    low_memory=False
)

print("\nDrug columns:")
print(drug_data.columns.tolist())

print("\nReaction columns:")
print(reaction_data.columns.tolist())

# Find the common report identifier
common_columns = list(
    set(drug_data.columns).intersection(reaction_data.columns)
)

print("\nCommon columns:", common_columns)

# Use the common report ID
if "primaryid" in common_columns:
    merge_column = "primaryid"
elif "caseid" in common_columns:
    merge_column = "caseid"
else:
    raise ValueError("No suitable common ID found.")

print("Merging using:", merge_column)

# Keep only required columns
drug_selected = drug_data[
    [merge_column, "drugname"]
].dropna(subset=["drugname"])

reaction_selected = reaction_data[
    [merge_column, reaction_data.columns[-1]]
]

# Merge the datasets
merged_data = pd.merge(
    drug_selected,
    reaction_selected,
    on=merge_column,
    how="inner"
)

# Save the merged data
output_file = OUTPUT_FOLDER / "drug_reaction_merged.csv"
merged_data.to_csv(output_file, index=False)

print("\nMerge completed successfully!")
print("Merged records:", len(merged_data))
print("Saved at:", output_file)