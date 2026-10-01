import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

# Read the NLP results
reaction_data = pd.read_csv("outputs/nlp_reaction_summary.csv")
drug_data = pd.read_csv("outputs/nlp_drug_summary.csv")

# Adverse reaction chart
top_reactions = reaction_data.head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_reactions["Adverse Reaction"][::-1],
    top_reactions["Frequency"][::-1]
)
plt.title("Top 10 Reported Adverse Reactions")
plt.xlabel("Frequency")
plt.ylabel("Adverse Reaction")
plt.tight_layout()
plt.savefig("outputs/top_10_adverse_reactions.png", dpi=300)
plt.close()

# Drug chart
top_drugs = drug_data.head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_drugs["Drug Name"][::-1],
    top_drugs["Frequency"][::-1]
)
plt.title("Top 10 Reported Drugs")
plt.xlabel("Frequency")
plt.ylabel("Drug Name")
plt.tight_layout()
plt.savefig("outputs/top_10_reported_drugs.png", dpi=300)
plt.close()

print("NLP charts created successfully!")