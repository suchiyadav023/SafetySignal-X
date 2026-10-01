from pathlib import Path
import pandas as pd

# Project folder location
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# FDA data folder
FDA_FOLDER = (
    PROJECT_FOLDER
    / "data"
    / "raw"
    / "faers_ascii_2025q1"
    / "ASCII"
)

# Processed data folder
PROCESSED_FOLDER = PROJECT_FOLDER / "data" / "processed"

# Create processed folder if it does not exist
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

print("SafetySignal-X FDA data processing started...")

# Read the FDA files
drug_file = FDA_FOLDER / "DRUG25Q1.txt"
reaction_file = FDA_FOLDER / "REAC25Q1.txt"
demo_file = FDA_FOLDER / "DEMO25Q1.txt"

print("Reading drug data...")
drug_data = pd.read_csv(drug_file, sep="$", encoding="latin1", low_memory=False)

print("Reading reaction data...")
reaction_data = pd.read_csv(
    reaction_file, sep="$", encoding="latin1", low_memory=False
)

print("Reading demographic data...")
demo_data = pd.read_csv(demo_file, sep="$", encoding="latin1", low_memory=False)

# Display basic information
print("\nData loaded successfully!")
print("Drug records:", len(drug_data))
print("Reaction records:", len(reaction_data))
print("Demographic records:", len(demo_data))

# Save processed copies
drug_data.to_csv(PROCESSED_FOLDER / "drug_data.csv", index=False)
reaction_data.to_csv(PROCESSED_FOLDER / "reaction_data.csv", index=False)
demo_data.to_csv(PROCESSED_FOLDER / "demographic_data.csv", index=False)

print("\nProcessed files saved successfully!")
print("Location:", PROCESSED_FOLDER)