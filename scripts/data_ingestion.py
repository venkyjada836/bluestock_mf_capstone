import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/raw")

csv_files = list(RAW_DATA.glob("*.csv"))

if not csv_files:
    print("No CSV files found in data/raw")
else:
    for file in csv_files:
        print("=" * 60)
        print(f"Dataset: {file.name}")

        try:
            df = pd.read_csv(file)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

        except Exception as e:
            print(f"Error reading {file.name}: {e}")

        print("=" * 60)