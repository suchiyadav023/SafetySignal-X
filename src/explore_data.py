from pathlib import Path
import pandas as pd

# Project folder location
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Processed data folder
DATA_FOLDER = PROJECT_FOLDER / "data" / "processed"

# Read the drug data
drug_file = DATA_FOLDER / "drug_data.csv"

print("Loading drug data...")
drug_data = pd.read_csv(drug_file, low_memory=False)

print("\nSafetySignal-X Drug Data Exploration")
print("------------------------------------")

print("Total drug records:", len(drug_data))

print("\nColumn names:")
print(drug_data.columns.tolist())

print("\nFirst 5 rows:")
print(drug_data.head())

print("\nData shape:")
print(drug_data.shape)

print("\nDrug data exploration completed successfully!")