import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("models/original_dataset.csv")

X = data.drop("Label", axis=1)
y = data["Label"]

X.replace([np.inf, -np.inf], np.nan, inplace=True)

imputer = SimpleImputer(strategy="mean")
X_imputed = imputer.fit_transform(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

joblib.dump(imputer, "models/imputer.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(model, "models/threat_detection_model.pkl")

# Save feature names used for training
feature_names = X.columns.tolist()
joblib.dump(feature_names, "models/feature_names.pkl")

print("✅ Model and preprocessing objects saved successfully.")
