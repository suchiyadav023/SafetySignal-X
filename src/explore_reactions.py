from pathlib import Path
import pandas as pd

# Project folder location
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Processed data folder
DATA_FOLDER = PROJECT_FOLDER / "data" / "processed"

# Reaction data file
reaction_file = DATA_FOLDER / "reaction_data.csv"

print("Loading adverse reaction data...")

reaction_data = pd.read_csv(
    reaction_file,
    low_memory=False
)

print("\nSafetySignal-X Reaction Data Exploration")
print("---------------------------------------")

print("Total reaction records:", len(reaction_data))

print("\nColumn names:")
print(reaction_data.columns.tolist())

print("\nFirst 5 rows:")
print(reaction_data.head())

print("\nData shape:")
print(reaction_data.shape)

print("\nReaction data exploration completed successfully!")