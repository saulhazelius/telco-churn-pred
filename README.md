# telco-churn-pred
Customer churn prediction. Includes EDA, model selection, and deployment. It is the continuation of the churn prediction project in the [ML for ronins repo](https://github.com/saulhazelius/ML_ronin/tree/main/projects/churn_prediction)

This project consists of a ML model for churn prediction of customers in a telecommunications company. The dataset used for training is the [telco dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). 
The model is a simple logistic regression trained in the `model_selection.ipynb` notebook. After running this notebook you can see the logged metrics from the hyperparameter search with:

`mlflow ui`

The model artifacts are stored in the `/model` dir

## Deployment
You can deploy the service with a AWS Lambda Function and API Gateway. In order to follow the deploy commands you should have aws credentials and the aws-cli, sam-cli packages using the provided `template.yaml` file.  

Firstly, in the `api/churn-pred` dir build the container with:

`sam build --use-container --parameter-overrides DockerTag=dev`

`dev` indicates a development environment. Then, create the repository (you can change the name):
`aws ecr create-repository --repository-name churn-pred/dev`

Then login using the repo uri obtained with `aws ecr describe-repositories --repository-name churn-pred/dev`

`aws ecr get-login-password --region <your_region> | docker login -u AWS --password-stdin <repo_uri>`

Push the container:

`docker tag churnpredfunction:dev <repo_uri>:latest`

`docker push <repo_uri>:latest`

And perform the deployment with:

`sam deploy --stack-name churnpredfunction-dev --region <your_region> --image-repository <repo_uri> --capabilities CAPABILITY_IAM --parameter-overrides Environment=dev`

If success, test the microservice with curl or postman using the created endpoint:


`curl -X POST -H "Content-Type: application/json" -d @../../src/predict/example.json <endpoint>`


After the stack creation, you can delete it with:

`aws cloudformation delete-stack --stack-name churnpredfunction-dev`

