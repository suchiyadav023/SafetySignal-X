from pathlib import Path

# Get the project folder location
project_folder = Path(__file__).resolve().parent.parent

# Define the data folders
raw_folder = project_folder / "data" / "raw"
processed_folder = project_folder / "data" / "processed"

print("SafetySignal-X data folder check")
print("--------------------------------")

print("Raw data folder:", raw_folder)
print("Raw folder exists:", raw_folder.exists())

print("Processed data folder:", processed_folder)
print("Processed folder exists:", processed_folder.exists())

print("\nData folder setup completed successfully!")