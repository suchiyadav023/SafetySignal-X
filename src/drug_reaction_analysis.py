import pandas as pd
import os

TARGET_DRUG = "DUPIXENT"

drug_file = "data/processed/drug_data.csv"
reaction_file = "data/processed/reaction_data.csv"

os.makedirs("outputs", exist_ok=True)

print("Finding reports for DUPIXENT...")

# Find report IDs for DUPIXENT
drug_report_ids = set()

for chunk in pd.read_csv(
    drug_file,
    usecols=["primaryid", "drugname"],
    chunksize=100000,
    low_memory=False
):
    matching_rows = chunk[
        chunk["drugname"].astype(str).str.upper().str.strip()
        == TARGET_DRUG
    ]

    drug_report_ids.update(
        matching_rows["primaryid"].dropna().astype(str)
    )

print("DUPIXENT reports found:", len(drug_report_ids))

# Find reactions connected to DUPIXENT reports
reaction_counts = {}

print("Finding adverse reactions...")

for chunk in pd.read_csv(
    reaction_file,
    usecols=["primaryid", "pt"],
    chunksize=100000,
    low_memory=False
):
    chunk["primaryid"] = chunk["primaryid"].astype(str)

    matching_reactions = chunk[
        chunk["primaryid"].isin(drug_report_ids)
    ]

    counts = matching_reactions["pt"].value_counts()

    for reaction, count in counts.items():
        reaction_counts[reaction] = (
            reaction_counts.get(reaction, 0) + count
        )

# Create summary
result = (
    pd.Series(reaction_counts)
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

result.columns = ["Adverse Reaction", "Frequency"]

result.to_csv(
    "outputs/dupixent_reactions.csv",
    index=False
)

print("\nTop 20 reactions reported with DUPIXENT:")
print(result)

print("\nAnalysis completed successfully!")
print("Saved at: outputs/dupixent_reactions.csv")