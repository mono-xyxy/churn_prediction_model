import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna()

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 100],
        labels=["0-12", "13-24", "25+"]
    )

    df["high_value_customer"] = (df["MonthlyCharges"] > 70).astype(int)

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df