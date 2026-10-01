import pandas as pd
import os
from nltk.tokenize import wordpunct_tokenize

print("Starting NLP extraction...")

os.makedirs("outputs", exist_ok=True)

# Function to clean text using basic NLP
def clean_text(text):
    text = str(text).upper().strip()
    tokens = wordpunct_tokenize(text)
    cleaned_text = " ".join(tokens)
    return cleaned_text


# -------------------------------
# 1. Process drug names
# -------------------------------
drug_file = "data/processed/drug_data.csv"

print("Processing drug names...")

drug_counts = {}

for chunk in pd.read_csv(
    drug_file,
    usecols=["drugname"],
    chunksize=100000,
    low_memory=False
):
    chunk["clean_drug"] = chunk["drugname"].apply(clean_text)

    counts = chunk["clean_drug"].value_counts()

    for drug, count in counts.items():
        drug_counts[drug] = drug_counts.get(drug, 0) + count

drug_summary = (
    pd.Series(drug_counts)
    .sort_values(ascending=False)
    .head(50)
    .reset_index()
)

drug_summary.columns = ["Drug Name", "Frequency"]

drug_summary.to_csv(
    "outputs/nlp_drug_summary.csv",
    index=False
)


# -------------------------------
# 2. Process adverse reactions
# -------------------------------
reaction_file = "data/processed/reaction_data.csv"

print("Processing adverse reactions...")

reaction_counts = {}

for chunk in pd.read_csv(
    reaction_file,
    usecols=["pt"],
    chunksize=100000,
    low_memory=False
):
    chunk["clean_reaction"] = chunk["pt"].apply(clean_text)

    counts = chunk["clean_reaction"].value_counts()

    for reaction, count in counts.items():
        reaction_counts[reaction] = reaction_counts.get(reaction, 0) + count

reaction_summary = (
    pd.Series(reaction_counts)
    .sort_values(ascending=False)
    .head(50)
    .reset_index()
)

reaction_summary.columns = ["Adverse Reaction", "Frequency"]

reaction_summary.to_csv(
    "outputs/nlp_reaction_summary.csv",
    index=False
)

print("\nNLP extraction completed successfully!")

print("Drug summary saved at:")
print("outputs/nlp_drug_summary.csv")

print("\nReaction summary saved at:")
print("outputs/nlp_reaction_summary.csv")

print("\nTop 10 adverse reactions:")
print(reaction_summary.head(10))