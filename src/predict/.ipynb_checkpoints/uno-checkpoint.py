import json
import joblib


MODEL_PATH = "../models/churn_artifacts.joblib"

with open("example.json") as info:
    churn_info = json.load(info)



def get_array(inf):


