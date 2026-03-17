import joblib
import pandas as pd

MODEL_PATH = "models/churn_pipeline_v1.pkl"

model = joblib.load(MODEL_PATH)


def predict(data: dict):
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    risk = "HIGH" if probability > 0.7 else "MEDIUM" if probability > 0.4 else "LOW"

    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability),
        "risk_level": risk
    }