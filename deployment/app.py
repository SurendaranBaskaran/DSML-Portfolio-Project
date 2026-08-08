# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# ----------------------- PATHS -----------------------
MODEL_PATH = r"C:\Users\Administrator\Desktop\Product-Sales-Forecasting\model\sales_model.pkl"
ENC_PATH   = r"C:\Users\Administrator\Desktop\Product-Sales-Forecasting\model\label_encoders.pkl"

print("Loading model...")
model = joblib.load(MODEL_PATH)
print("Model loaded.")

print("Loading encoders...")
encoders = joblib.load(ENC_PATH)
print("Encoders loaded.")

# Get model feature order
model_features = model.booster_.feature_name()
print("Model expects", len(model_features), "features.")
print(model_features)

# ----------------------- PREPROCESSING -----------------------
def preprocess_input(json_data):
    df = pd.DataFrame([json_data])

    # ---------- DATE PROCESSING ----------
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month
        df["Day"] = df["Date"].dt.day
        df["Weekday"] = df["Date"].dt.weekday
        df["Week"] = df["Date"].dt.isocalendar().week.astype(int)

    # ---------- APPLY LABEL ENCODERS ----------
    for col, le in encoders.items():
        if col in df.columns:
            value = str(df[col].iloc[0])
            if value not in le.classes_:
                if "Unknown" not in le.classes_:
                    le.classes_ = np.append(le.classes_, "Unknown")
                value = "Unknown"
            df[col] = le.transform([value])[0]

    # ---------- ENGINEERED FEATURE DEFAULTS ----------
    engineered = [
        "store_sales_mean",
        "store_sales_median",
        "store_sales_std",
        "store_7d_avg"
    ]
    for col in engineered:
        if col not in df.columns:
            df[col] = 0  # safe default

    # Remove unused columns
    df = df.drop(columns=[c for c in ["ID", "Sales", "Date"] if c in df.columns], errors="ignore")

    # ---------- ALIGN TO MODEL FEATURES ----------
    for col in model_features:
        if col not in df.columns:
            df[col] = 0

    df = df.reindex(columns=model_features, fill_value=0)

    # convert to numeric
    df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

    return df


# ----------------------- ROUTE -----------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    try:
        X = preprocess_input(data)
        pred = model.predict(X)[0]
        return jsonify({"predicted_sales": float(pred)})
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route("/")
def home():
    return app.send_static_file("index.html")

# ----------------------- RUN APP -----------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
