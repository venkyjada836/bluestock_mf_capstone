from pathlib import Path
import pandas as pd

RAW_DATA = Path("data/raw")

for file in RAW_DATA.glob("0*.csv"):
    print("=" * 60)
    print(file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("Columns:")
    print(df.columns.tolist())
    print()