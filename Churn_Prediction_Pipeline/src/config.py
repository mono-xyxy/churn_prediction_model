TARGET = "Churn"

CATEGORICAL_FEATURES = [
    "gender", "Partner", "Dependents", "PhoneService",
    "MultipleLines", "InternetService", "OnlineSecurity",
    "OnlineBackup", "DeviceProtection", "TechSupport",
    "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod"
]

NUMERICAL_FEATURES = [
    "tenure", "MonthlyCharges", "TotalCharges"
]