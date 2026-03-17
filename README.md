

# Customer Churn Prediction (End-to-End ML)

Simple end-to-end ML project to predict customer churn using a real telecom dataset.  
Covers full pipeline: data → preprocessing → model → API → UI.

---

## What this project does

- Takes customer data (tenure, charges, services, etc.)
- Runs through preprocessing pipeline (encoding + scaling)
- Uses trained model (Random Forest)
- Outputs churn prediction + probability

---

## Tech used

- Python
- Pandas, NumPy
- scikit-learn
- imbalanced-learn (SMOTE)
- FastAPI (API layer)
- Streamlit (UI)

---

## Project structure

```

Churn_Prediction_Pipeline/
│
├── data/                  # dataset
├── models/                # saved model (pkl)
├── src/
│   ├── init.py
│   ├── train.py
│   ├── predict.py
│
├── api/
│   ├── init.py
│   ├── main.py           # FastAPI app
│
├── app.py                # Streamlit UI
├── requirements.txt
└── README.md

````

---

## How to run

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Train model (optional)

```bash
py -m src.train
```

Model will be saved in:

```
models/churn_pipeline_v1.pkl
```

---

### 3. Run API

```bash
py -m uvicorn api.main:app --reload --app-dir .
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 4. Run UI (Streamlit)

```bash
py -m streamlit run app.py
```

---

## API endpoints

* `/health` → check if API running
* `/predict` → main prediction endpoint
* `/model-info` → basic model info

---

## Example input

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.0,
  "TotalCharges": 350.0
}
```

---

## Model details

* Algorithm: Random Forest
* Preprocessing:

  * StandardScaler (numerical)
  * OneHotEncoder (categorical)
* Imbalance handled using SMOTE (inside CV only)
* Evaluation: ROC-AUC

---

## Notes

* Pipeline used to avoid data leakage
* Same preprocessing applied during training and inference
* Model saved using joblib

---

## Future improvements

* Deploy API (Render / AWS)
* Add auth + logging
* Improve UI
* Add model monitoring

---


