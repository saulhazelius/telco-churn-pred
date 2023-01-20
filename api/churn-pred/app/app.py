import joblib
import json


MODEL_PATH = '/opt/ml/model'
model = joblib.load(MODEL_PATH)


def lambda_handler(event, context):
    dv, model = joblib.load(MODEL_PATH)
    churn_info = json.loads(event['body'])
    churn_input = dv.transform(churn_info)
    prediction = round(model.predict_proba(churn_input)[0][1], 2)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predicted_probability": prediction,
            }
        )
    }
