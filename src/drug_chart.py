from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project folders
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
OUTPUT_FOLDER = PROJECT_FOLDER / "outputs"

# Read the drug summary
summary_file = OUTPUT_FOLDER / "top_20_drugs.csv"
drug_data = pd.read_csv(summary_file)

# Create the chart
plt.figure(figsize=(12, 8))

plt.barh(
    drug_data.iloc[:, 0],
    drug_data.iloc[:, 1]
)

plt.xlabel("Number of Reports")
plt.ylabel("Drug Name")
plt.title("Top 20 Reported Drugs - FDA Q1 2025")

plt.gca().invert_yaxis()
plt.tight_layout()

# Save the chart
chart_file = OUTPUT_FOLDER / "top_20_drugs_chart.png"
plt.savefig(chart_file, dpi=300)

print("Drug chart created successfully!")
print("Chart saved at:", chart_file)

plt.show()