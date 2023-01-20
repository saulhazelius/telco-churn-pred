"""
Script for churn prediction using a json payload.
"""
import json
import joblib
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def load_payload():
    with open("example.json") as info:
        churn_info = json.load(info)
    return churn_info


if __name__ == "__main__":
    MODEL_PATH = "../model/churn_artifacts.joblib"
    dv, model = joblib.load(MODEL_PATH)
    churn_info = load_payload()
    churn_input = dv.transform(churn_info)
    prediction = round(model.predict_proba(churn_input)[0][1], 2)
    logging.info(f"Probability of churn: {prediction}")
