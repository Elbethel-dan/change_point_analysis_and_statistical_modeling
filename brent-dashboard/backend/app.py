from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Load data
prices_df = pd.read_csv("/Users/elbethelzewdie/Downloads/change_point_analysis_and_statistical_modeling/change_point_analysis_and_statistical_modeling/data/BrentOilPrices.csv")
prices_df["Date"] = pd.to_datetime(prices_df["Date"], format="mixed")

events_df = pd.read_csv("/Users/elbethelzewdie/Downloads/change_point_analysis_and_statistical_modeling/change_point_analysis_and_statistical_modeling/data/Event_file.csv")
events_df["Approximate_date"] = pd.to_datetime(events_df["Approximate_date"],errors="coerce")
events_df["Approximate_date"] = events_df["Approximate_date"].dt.strftime("%d-%m-%Y")

with open("/Users/elbethelzewdie/Downloads/change_point_analysis_and_statistical_modeling/change_point_analysis_and_statistical_modeling/data/change_point_results.json") as f:
    cp_results = json.load(f)


# -------------------------------
# Historical Price Endpoint
# -------------------------------
@app.route("/api/prices")
def get_prices():
    start = request.args.get("start")
    end = request.args.get("end")

    df = prices_df.copy()

    if start:
        df = df[df["Date"] >= pd.to_datetime(start)]
    if end:
        df = df[df["Date"] <= pd.to_datetime(end)]

    return df.to_json(orient="records")


# -------------------------------
# Change Point Endpoint
# -------------------------------
@app.route("/api/changepoint")
def get_changepoint():
    return jsonify(cp_results)


# -------------------------------
# Events Endpoint
# -------------------------------
@app.route("/api/events")
def get_events():
    return events_df.to_json(orient="records")


# -------------------------------
# Volatility Endpoint
# -------------------------------
@app.route("/api/volatility")
def get_volatility():
    df = prices_df.copy()
    df["log_return"] = (df["Price"].apply(lambda x: pd.np.log(x))).diff()
    df["rolling_vol"] = df["log_return"].rolling(30).std()

    return df[["Date", "rolling_vol"]].dropna().to_json(orient="records")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
