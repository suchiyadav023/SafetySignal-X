import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the saved signal result
file_path = "outputs/signal_results.csv"
data = pd.read_csv(file_path)

# Extract values
drug = data.loc[0, "Drug"]
reaction = data.loc[0, "Adverse Reaction"]
ror = data.loc[0, "ROR"]
lower = data.loc[0, "95% CI Lower"]
upper = data.loc[0, "95% CI Upper"]

# Create the graph
plt.figure(figsize=(8, 5))

plt.errorbar(
    ["DUPIXENT"],
    [ror],
    yerr=[[ror - lower], [upper - ror]],
    fmt="o",
    capsize=8
)

plt.axhline(y=1, linestyle="--", label="Reference line: ROR = 1")

plt.title("Reporting Odds Ratio Signal")
plt.ylabel("Reporting Odds Ratio")
plt.xlabel("Drug")

plt.legend()
plt.tight_layout()

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Save the graph
output_path = "outputs/signal_result_chart.png"
plt.savefig(output_path, dpi=300)

print("Signal graph created successfully!")
print("Graph saved at:", output_path)

plt.show()