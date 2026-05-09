"""Core analysis logic: simple linear regression and anomaly detection."""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
from typing import Tuple

# Dummy function to simulate data retrieval
async def fetch_energy_records(building_id: int, start: str, end: str):
    # Generate synthetic data for demo
    rng = pd.date_range(start=start, end=end, freq="H")
    consumption = np.random.normal(loc=50, scale=10, size=len(rng))
    df = pd.DataFrame({"timestamp": rng, "energy_kwh": consumption})
    return df

async def analyze_energy_data(building_id: int, start: str, end: str):
    df = await fetch_energy_records(building_id, start, end)
    if df.empty:
        raise ValueError("No data available")

    # Basic statistics
    avg = df["energy_kwh"].mean()
    peak = df["energy_kwh"].max()

    # Linear regression on time vs consumption
    df["hour"] = df["timestamp"].astype(int) / 10**9  # seconds since epoch
    X = df[["hour"]]
    y = df["energy_kwh"]
    model = LinearRegression()
    model.fit(X, y)
    trend = model.coef_[0]

    # Anomaly detection: flag if consumption > avg + 2*std
    std = df["energy_kwh"].std()
    anomaly = df["energy_kwh"].max() > avg + 2 * std

    recommendation = (
        "Consider load shifting during peak hours to reduce peak consumption."
        if anomaly
        else "Consumption within normal range."
    )

    return {
        "building_id": building_id,
        "period_start": datetime.fromisoformat(start),
        "period_end": datetime.fromisoformat(end),
        "avg_consumption": float(avg),
        "peak_consumption": float(peak),
        "anomaly_detected": bool(anomaly),
        "recommendation": recommendation,
    }
