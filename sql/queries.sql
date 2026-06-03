-- Top 5 funds by AUM
SELECT fund_house, MAX(aum_crore) AS aum
FROM fact_aum
GROUP BY fund_house
ORDER BY aum DESC
LIMIT 5;

-- Average NAV by month
SELECT strftime('%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- Transactions by state
SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- Top 10 funds by 5Y return
SELECT scheme_name, return_5yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 10;
