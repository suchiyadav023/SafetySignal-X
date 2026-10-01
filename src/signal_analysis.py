import pandas as pd
import math

# -----------------------------
# File paths
# -----------------------------
DRUG_FILE = "data/processed/drug_data.csv"
REACTION_FILE = "data/processed/reaction_data.csv"

# -----------------------------
# Select drug and reaction
# -----------------------------
TARGET_DRUG = "DUPIXENT"
TARGET_REACTION = "Injection site pain"

print("Loading drug and reaction data...")

# Load data
drug_data = pd.read_csv(DRUG_FILE, low_memory=False)
reaction_data = pd.read_csv(REACTION_FILE, low_memory=False)

# -----------------------------
# Find reports containing drug
# -----------------------------
drug_reports = set(
    drug_data.loc[
        drug_data["drugname"]
        .astype(str)
        .str.casefold()
        == TARGET_DRUG.casefold(),
        "primaryid"
    ]
)

# -----------------------------
# Find reports containing reaction
# -----------------------------
reaction_reports = set(
    reaction_data.loc[
        reaction_data["pt"]
        .astype(str)
        .str.casefold()
        == TARGET_REACTION.casefold(),
        "primaryid"
    ]
)

# -----------------------------
# Calculate 2x2 table
# -----------------------------
all_reports = set(drug_data["primaryid"].dropna().unique())

a = len(drug_reports & reaction_reports)
b = len(drug_reports - reaction_reports)
c = len(reaction_reports - drug_reports)
d = len(all_reports - (drug_reports | reaction_reports))

# -----------------------------
# Calculate ROR
# -----------------------------
if b == 0 or c == 0:
    print("ROR cannot be calculated because b or c is zero.")
else:
    ror = (a * d) / (b * c)

    print("\n2x2 Table")
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

    print("\nReporting Odds Ratio (ROR):", round(ror, 4))

    print("\nSignal analysis completed successfully!")