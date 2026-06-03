import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
DB_PATH = "sqlite:///data/db/bluestock_mf.db"

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

print("ETL Pipeline Started...")

# ==========================
# NAV HISTORY
# ==========================

nav_df = pd.read_csv(RAW_PATH / "02_nav_history.csv")

print("\nOriginal Shape:", nav_df.shape)

# Convert date
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Keep only positive NAV values
nav_df = nav_df[nav_df["nav"] > 0]

print("Cleaned Shape:", nav_df.shape)

# Save cleaned file
nav_df.to_csv(
    PROCESSED_PATH / "nav_history_clean.csv",
    index=False
)

print("Saved: nav_history_clean.csv")


# ==========================
# INVESTOR TRANSACTIONS
# ==========================

txn_df = pd.read_csv(RAW_PATH / "08_investor_transactions.csv")

print("\nTransactions Original Shape:", txn_df.shape)

# Convert date
txn_df["transaction_date"] = pd.to_datetime(txn_df["transaction_date"])

# Standardize transaction type
txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]

txn_df = txn_df[
    txn_df["transaction_type"].isin(valid_types)
]

# Amount must be positive
txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

# Remove duplicates
txn_df = txn_df.drop_duplicates()

print("Transactions Cleaned Shape:", txn_df.shape)

txn_df.to_csv(
    PROCESSED_PATH / "investor_transactions_clean.csv",
    index=False
)

print("Saved: investor_transactions_clean.csv")
# ==========================
# SCHEME PERFORMANCE
# ==========================

perf_df = pd.read_csv(RAW_PATH / "07_scheme_performance.csv")

print("\nPerformance Original Shape:", perf_df.shape)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Expense ratio validation
perf_df = perf_df[
    perf_df["expense_ratio_pct"].between(0.1, 2.5)
]

# Remove duplicates
perf_df = perf_df.drop_duplicates()

print("Performance Cleaned Shape:", perf_df.shape)

perf_df.to_csv(
    PROCESSED_PATH / "scheme_performance_clean.csv",
    index=False
)

print("Saved: scheme_performance_clean.csv")
# ==========================
# AUM BY FUND HOUSE
# ==========================

aum_df = pd.read_csv(RAW_PATH / "03_aum_by_fund_house.csv")
aum_df["date"] = pd.to_datetime(aum_df["date"])
aum_df = aum_df.drop_duplicates()

aum_df.to_csv(
    PROCESSED_PATH / "aum_by_fund_house_clean.csv",
    index=False
)

print("Saved: aum_by_fund_house_clean.csv")


# ==========================
# MONTHLY SIP INFLOWS
# ==========================

sip_df = pd.read_csv(RAW_PATH / "04_monthly_sip_inflows.csv")
sip_df = sip_df.drop_duplicates()

sip_df.to_csv(
    PROCESSED_PATH / "monthly_sip_inflows_clean.csv",
    index=False
)

print("Saved: monthly_sip_inflows_clean.csv")


# ==========================
# CATEGORY INFLOWS
# ==========================

cat_df = pd.read_csv(RAW_PATH / "05_category_inflows.csv")
cat_df = cat_df.drop_duplicates()

cat_df.to_csv(
    PROCESSED_PATH / "category_inflows_clean.csv",
    index=False
)

print("Saved: category_inflows_clean.csv")


# ==========================
# INDUSTRY FOLIO COUNT
# ==========================

folio_df = pd.read_csv(RAW_PATH / "06_industry_folio_count.csv")
folio_df = folio_df.drop_duplicates()

folio_df.to_csv(
    PROCESSED_PATH / "industry_folio_count_clean.csv",
    index=False
)

print("Saved: industry_folio_count_clean.csv")


# ==========================
# PORTFOLIO HOLDINGS
# ==========================

hold_df = pd.read_csv(RAW_PATH / "09_portfolio_holdings.csv")

hold_df = hold_df[
    hold_df["weight_pct"] > 0
]

hold_df = hold_df.drop_duplicates()

hold_df.to_csv(
    PROCESSED_PATH / "portfolio_holdings_clean.csv",
    index=False
)

print("Saved: portfolio_holdings_clean.csv")


# ==========================
# BENCHMARK INDICES
# ==========================

bench_df = pd.read_csv(RAW_PATH / "10_benchmark_indices.csv")

bench_df["date"] = pd.to_datetime(
    bench_df["date"]
)

bench_df = bench_df.drop_duplicates()

bench_df.to_csv(
    PROCESSED_PATH / "benchmark_indices_clean.csv",
    index=False
)

print("Saved: benchmark_indices_clean.csv")


# ==========================
# FUND MASTER
# ==========================

fund_df = pd.read_csv(RAW_PATH / "01_fund_master.csv")

fund_df["launch_date"] = pd.to_datetime(
    fund_df["launch_date"]
)

fund_df = fund_df.drop_duplicates()

fund_df.to_csv(
    PROCESSED_PATH / "fund_master_clean.csv",
    index=False
)

print("Saved: fund_master_clean.csv")
# ==========================
# LOAD TO SQLITE
# ==========================

print("\nCreating SQLite database...")

engine = create_engine(DB_PATH)

# Load cleaned datasets
fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

sip_df.to_sql(
    "fact_sip_industry",
    engine,
    if_exists="replace",
    index=False
)

cat_df.to_sql(
    "fact_category_inflows",
    engine,
    if_exists="replace",
    index=False
)

folio_df.to_sql(
    "fact_folio_statistics",
    engine,
    if_exists="replace",
    index=False
)

hold_df.to_sql(
    "fact_portfolio",
    engine,
    if_exists="replace",
    index=False
)

bench_df.to_sql(
    "fact_benchmark",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite database created successfully!")