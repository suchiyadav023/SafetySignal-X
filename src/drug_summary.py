from pathlib import Path
import pandas as pd

# Project folder
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Data and output folders
DATA_FOLDER = PROJECT_FOLDER / "data" / "processed"
OUTPUT_FOLDER = PROJECT_FOLDER / "outputs"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Load drug data
drug_file = DATA_FOLDER / "drug_data.csv"

print("Loading drug data...")
drug_data = pd.read_csv(drug_file, low_memory=False)

print("Finding the most frequently reported drugs...")

# Display available columns
print("\nAvailable columns:")
print(drug_data.columns.tolist())

# Select the drug name column
drug_column = "drugname"

if drug_column not in drug_data.columns:
    drug_column = drug_data.columns[0]
    print("\nUsing column:", drug_column)

# Count drug names
drug_counts = drug_data[drug_column].dropna().value_counts()

# Select top 20 drugs
top_drugs = drug_counts.head(20)

print("\nTop 20 Reported Drugs")
print("---------------------")
print(top_drugs)

# Save results
output_file = OUTPUT_FOLDER / "top_20_drugs.csv"
top_drugs.to_csv(output_file, header=["Count"])

print("\nDrug summary saved successfully!")
print("Saved at:", output_file)