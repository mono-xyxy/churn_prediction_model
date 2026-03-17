from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict

app = FastAPI()


class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def get_prediction(customer: Customer):
    return predict(customer.dict())


@app.get("/model-info")
def model_info():
    return {"model": "RandomForest + SMOTE Pipeline v1"}