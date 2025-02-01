import pandas as pd
import json
import os

# File paths
RAW_DATA_PATH = os.path.join("data", "raw_data.json")
CLEANED_DATA_PATH = os.path.join("data", "cleaned_data.csv")

# Check if file is empty
if not os.path.exists(RAW_DATA_PATH) or os.stat(RAW_DATA_PATH).st_size == 0:
    print("❌ Error: raw_data.json is empty or missing. Run the scraper first.")
    exit(1)

# Read raw JSON data
try:
    with open(RAW_DATA_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)
except json.JSONDecodeError:
    print("❌ Error: raw_data.json is not valid JSON.")
    exit(1)

# Convert to DataFrame
df = pd.DataFrame(raw_data)

# Drop duplicate messages
df.drop_duplicates(subset=["message_id"], keep="first", inplace=True)

# Remove empty text messages
df.dropna(subset=["text"], inplace=True)

# Standardize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime('%Y-%m-%d %H:%M:%S')

# Save cleaned data
df.to_csv(CLEANED_DATA_PATH, index=False)

print(f"✅ Cleaned data saved to {CLEANED_DATA_PATH}")
