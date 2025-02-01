import pandas as pd
from sqlalchemy import create_engine
import os

# File paths
CLEANED_DATA_PATH = os.path.join("data", "cleaned_data.csv")
DB_PATH = os.path.join("data", "medical_business.db")

# Create SQLite database connection
engine = create_engine(f"sqlite:///{DB_PATH}")

# Load cleaned data
df = pd.read_csv(CLEANED_DATA_PATH)

# Store cleaned data in the SQLite database
df.to_sql("medical_data", con=engine, if_exists="replace", index=False)

print(f"✅ Cleaned data stored in {DB_PATH}")
