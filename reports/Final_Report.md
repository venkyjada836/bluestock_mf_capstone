# Bluestock Mutual Fund Analytics Capstone Project

## Executive Summary

This project develops an end-to-end Mutual Fund Analytics platform using Python, SQL, and Power BI. The objective is to analyze mutual fund industry trends, evaluate fund performance, understand investor behavior, and provide advanced risk analytics and recommendations.

---

## Project Objectives

1. Build an ETL pipeline for mutual fund datasets.
2. Perform exploratory data analysis.
3. Analyze fund performance metrics.
4. Study investor transaction patterns.
5. Calculate risk metrics such as VaR and CVaR.
6. Develop a simple fund recommendation system.
7. Build interactive Power BI dashboards.
8. Generate business insights and recommendations.

---

## Data Sources

The project uses multiple cleaned datasets:

* fund_master_clean.csv
* nav_history_clean.csv
* scheme_performance_clean.csv
* investor_transactions_clean.csv
* monthly_sip_inflows_clean.csv
* category_inflows_clean.csv
* benchmark_indices_clean.csv
* portfolio_holdings_clean.csv

---

## ETL Design

### Extract

Data was collected from multiple CSV files.

### Transform

* Missing value handling
* Data type conversions
* Duplicate removal
* Date formatting
* Standardized column names

### Load

Processed datasets were loaded into SQLite and used for analysis and dashboard development.

---

## Exploratory Data Analysis Findings

* SIP inflows showed consistent growth from 2022–2025.
* Equity funds dominated industry assets.
* Investor participation increased significantly.
* T30 cities contributed higher investment volumes.
* Several categories showed strong net inflows.

---

## Performance Analytics

Metrics analyzed:

* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Standard Deviation
* Maximum Drawdown
* Expense Ratio

Key observations:

* Small-cap funds delivered higher returns but with higher risk.
* Large-cap funds demonstrated greater stability.
* Funds with higher Sharpe ratios showed better risk-adjusted performance.

---

## Advanced Analytics

### Historical VaR and CVaR

Calculated 95% Value at Risk and Conditional Value at Risk for all 40 schemes.

### Rolling Sharpe Ratio

Computed rolling 90-day Sharpe ratios for key funds.

### Investor Cohort Analysis

Analyzed investment patterns based on investor joining year.

### SIP Continuity Analysis

Identified investors with irregular SIP behavior and flagged at-risk investors.

### Fund Recommendation Engine

Recommended top funds based on risk appetite and Sharpe ratios.

### Portfolio Concentration

Calculated Herfindahl-Hirschman Index for equity funds.

---

## Dashboard Development

### Page 1: Industry Overview

* Total AUM
* Total SIP Inflows
* Total Folios
* Total Schemes
* Industry AUM Trend
* AUM by Fund House

### Page 2: Fund Performance

* Risk vs Return Scatter Plot
* Fund Scorecard
* NAV Analysis
* Interactive Filters

### Page 3: Investor Analytics

* Transaction Amount by State
* Transaction Type Distribution
* Age Group Analysis
* Monthly Transaction Trends

### Page 4: SIP and Market Trends

* SIP Inflow Trends
* Nifty 50 Trends
* Category-wise Net Inflows
* Top Categories by Inflows

---

## Key Insights

1. SIP inflows have increased steadily over the years.
2. Small-cap funds generated high returns but carried higher risk.
3. A significant number of investors were identified as SIP at-risk.
4. Equity-oriented categories received the highest inflows.
5. Risk-adjusted performance varied considerably across schemes.

---

## Limitations

* Limited historical data period.
* Simplified recommendation methodology.
* Market assumptions may change over time.

---

## Recommendations

* Increase SIP awareness programs.
* Improve investor retention strategies.
* Monitor high-risk schemes carefully.
* Expand portfolio diversification.
* Enhance recommendation systems using machine learning.

---

## Conclusion

The project successfully built an integrated Mutual Fund Analytics platform combining ETL pipelines, analytics, risk modeling, and interactive dashboards to provide actionable insights into the Indian mutual fund industry.

---

## Author

Venky Jada

Bluestock Mutual Fund Analytics Capstone Project
