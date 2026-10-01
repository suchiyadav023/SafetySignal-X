import pandas as pd
import os

# Signal result
result = {
    "Drug": ["DUPIXENT"],
    "Adverse Reaction": ["Injection site pain"],
    "ROR": [6.6935],
    "95% CI Lower": [6.3914],
    "95% CI Upper": [7.0099]
}

# Create a DataFrame
signal_data = pd.DataFrame(result)

# Create the output folder if it does not exist
os.makedirs("outputs", exist_ok=True)

# Save the result
output_file = "outputs/signal_results.csv"
signal_data.to_csv(output_file, index=False)

print("Signal result saved successfully!")
print("File location:", output_file)
print("\nSaved result:")
print(signal_data)