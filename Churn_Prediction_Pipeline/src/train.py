import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE

from src.preprocessing import clean_data
from src.config import CATEGORICAL_FEATURES, NUMERICAL_FEATURES, TARGET


def train():
    df = pd.read_csv("data/telco.csv")
    df = clean_data(df)

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=42
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
    )

    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), NUMERICAL_FEATURES),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES)
    ])

    pipeline = ImbPipeline([
        ("preprocessing", preprocessor),
        ("smote", SMOTE(random_state=42)),
        ("model", RandomForestClassifier(random_state=42))
    ])

    param_grid = {
        "model__n_estimators": [100, 200],
        "model__max_depth": [5, 10, None],
        "model__min_samples_split": [2, 5]
    }

    grid = GridSearchCV(
        pipeline,
        param_grid,
        cv=3,
        scoring="roc_auc",
        verbose=2,
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    print("Best Params:", grid.best_params_)
    print("Best AUC:", grid.best_score_)

    joblib.dump(grid.best_estimator_, "models/churn_pipeline_v1.pkl")


if __name__ == "__main__":
    train()