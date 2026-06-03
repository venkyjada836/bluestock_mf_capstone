# Data Dictionary

## 01_fund_master.csv

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier |
| fund_house         | Text      | Asset Management Company name |
| scheme_name        | Text      | Mutual fund scheme name       |
| category           | Text      | Fund category                 |
| sub_category       | Text      | Fund sub-category             |
| plan               | Text      | Direct/Regular plan           |
| launch_date        | Date      | Scheme launch date            |
| benchmark          | Text      | Benchmark index               |
| expense_ratio_pct  | Float     | Expense ratio percentage      |
| exit_load_pct      | Float     | Exit load percentage          |
| min_sip_amount     | Float     | Minimum SIP investment        |
| min_lumpsum_amount | Float     | Minimum lumpsum investment    |
| fund_manager       | Text      | Fund manager name             |
| risk_category      | Text      | Risk classification           |
| sebi_category_code | Text      | SEBI category code            |

---

## 02_nav_history.csv

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | Integer   | AMFI scheme code |
| date      | Date      | NAV date         |
| nav       | Float     | Net Asset Value  |

---

## 03_aum_by_fund_house.csv

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | AMC name          |
| aum_lakh_crore | Float     | AUM in lakh crore |
| aum_crore      | Float     | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

---

## 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description                      |
| ------------------------- | --------- | -------------------------------- |
| month                     | Text      | Reporting month                  |
| sip_inflow_crore          | Float     | SIP inflow amount                |
| active_sip_accounts_crore | Float     | Active SIP accounts              |
| new_sip_accounts_lakh     | Float     | New SIP registrations            |
| sip_aum_lakh_crore        | Float     | SIP AUM                          |
| yoy_growth_pct            | Float     | Year-over-year growth percentage |

---

## 05_category_inflows.csv

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Text      | Reporting month   |
| category         | Text      | Fund category     |
| net_inflow_crore | Float     | Net inflow amount |

---

## 06_industry_folio_count.csv

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Text      | Reporting month |
| total_folios_crore  | Float     | Total folios    |
| equity_folios_crore | Float     | Equity folios   |
| debt_folios_crore   | Float     | Debt folios     |
| hybrid_folios_crore | Float     | Hybrid folios   |
| others_folios_crore | Float     | Other folios    |

---

## 07_scheme_performance.csv

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| amfi_code          | Integer   | Scheme code             |
| return_1yr_pct     | Float     | 1-year return           |
| return_3yr_pct     | Float     | 3-year return           |
| return_5yr_pct     | Float     | 5-year return           |
| alpha              | Float     | Alpha metric            |
| beta               | Float     | Beta metric             |
| sharpe_ratio       | Float     | Sharpe ratio            |
| sortino_ratio      | Float     | Sortino ratio           |
| std_dev_ann_pct    | Float     | Annualized volatility   |
| max_drawdown_pct   | Float     | Maximum drawdown        |
| aum_crore          | Float     | Assets under management |
| expense_ratio_pct  | Float     | Expense ratio           |
| morningstar_rating | Integer   | Morningstar rating      |
| risk_grade         | Text      | Risk grade              |

---

## 08_investor_transactions.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Unique investor identifier |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Scheme code                |
| transaction_type   | Text      | SIP/Lumpsum/Redemption     |
| amount_inr         | Float     | Transaction amount         |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | Tier classification        |
| age_group          | Text      | Investor age group         |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income              |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |

---

## 09_portfolio_holdings.csv

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Scheme code              |
| stock_symbol      | Text      | Stock ticker             |
| stock_name        | Text      | Company name             |
| sector            | Text      | Industry sector          |
| weight_pct        | Float     | Portfolio weight         |
| market_value_cr   | Float     | Market value             |
| current_price_inr | Float     | Current stock price      |
| portfolio_date    | Date      | Portfolio reporting date |

---

## 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading date         |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |
