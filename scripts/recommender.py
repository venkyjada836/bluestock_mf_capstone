import pandas as pd

funds = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

def recommend_funds(risk_appetite):

    risk_map = {
        'Low': ['Low'],
        'Moderate': ['Moderate', 'Moderately High'],
        'High': ['High', 'Very High']
    }

    selected = funds[
        funds['risk_grade'].isin(
            risk_map[risk_appetite]
        )
    ]

    recommendations = (
        selected
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            'amfi_code',
            'risk_grade',
            'sharpe_ratio',
            'return_3yr_pct'
        ]
    ]

print(recommend_funds('Moderate'))