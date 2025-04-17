import pandas as pd
import joblib
import traceback
import numpy as np

model = joblib.load("../models/threat_detection_model.pkl")
scaler = joblib.load("../models/scaler.pkl")
imputer = joblib.load("../models/imputer.pkl")

def preprocess_input(file):
    try:
        df = pd.read_csv(file, encoding='utf-8')

        if 'Label' in df.columns:
            df.drop(columns=['Label'], inplace=True)

        feature_names = joblib.load("../models/feature_names.pkl")

        missing = set(feature_names) - set(df.columns)
        if missing:
            print(f"❌ Missing columns in uploaded file: {missing}")
            return None

        df = df[feature_names]
        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        df_imputed = imputer.transform(df)
        df_scaled = scaler.transform(df_imputed)

        return df_scaled

    except Exception as e:
        print(f"❌ ERROR during preprocessing: {e}")
        return None

def make_prediction(processed_data):
    try:
        predictions = model.predict(processed_data)

        # Ensure it's a 1D list (e.g., [0, 1, 0])
        if isinstance(predictions, (np.ndarray, list)):
            predictions = np.array(predictions).flatten().tolist()
        else:
            predictions = [predictions]

        return predictions

    except Exception as e:
        print("[ERROR in prediction]", traceback.format_exc())
        return None
