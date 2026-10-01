from pathlib import Path
import pandas as pd

# Project folder location
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Data folders
DATA_FOLDER = PROJECT_FOLDER / "data" / "processed"
OUTPUT_FOLDER = PROJECT_FOLDER / "outputs"

# Create the output folder if needed
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Load reaction data
reaction_file = DATA_FOLDER / "reaction_data.csv"

print("Loading reaction data...")
reaction_data = pd.read_csv(reaction_file, low_memory=False)

print("Finding the most common adverse reactions...")

print("\nAvailable columns:")
print(reaction_data.columns.tolist())

reaction_column = reaction_data.columns[-1]

print("\nUsing reaction column:", reaction_column)

reaction_counts = reaction_data[reaction_column].value_counts()

# Select the top 20 reactions
top_reactions = reaction_counts.head(20)

print("\nTop 20 Reported Adverse Reactions")
print("---------------------------------")
print(top_reactions)

# Save the results
output_file = OUTPUT_FOLDER / "top_20_reactions.csv"
top_reactions.to_csv(output_file, header=["Count"])

print("\nSummary saved successfully!")
print("Saved at:", output_file)