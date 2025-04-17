import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib

data = pd.read_csv("models/original_dataset.csv")

X = data.drop("Label", axis=1)
y = data["Label"]

X.replace([np.inf, -np.inf], np.nan, inplace=True)

imputer = SimpleImputer(strategy="mean")
X_imputed = imputer.fit_transform(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

joblib.dump(imputer, "models/imputer.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Preprocessing objects saved (imputer and scaler)")
