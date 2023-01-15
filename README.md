# telco-churn-pred
Customer churn prediction. Includes EDA, model selection, and deployment. It is the continuation of the churn prediction project in the [ML for ronins repo](https://github.com/saulhazelius/ML_ronin/tree/main/projects/churn_prediction)

This project consists of a ML model for churn prediction of customers in a telecommunications company. The dataset used for training is the [telco dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). 
The model is a simple logistic regression trained in the `model_selection.ipynb` notebook. After running this notebook you can see the logged metrics from the hyperparameter search with:

`mlflow ui`

The model artifacts are stored in the `/model` dir


