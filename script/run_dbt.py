import os

# Change to DBT project directory
DBT_PROJECT_DIR = "dbt_project"

print("🚀 Running DBT transformations...")
os.system(f"cd {DBT_PROJECT_DIR} && dbt run")
print("✅ DBT transformations completed.")
