

Watched an overview video: [Getting Started with Amazon SageMaker - Build, Train, and Deploy Machine Learning Models][1]. Sagemake includes:
 * hosted Jupyter notebooks
 * Ground Truth, annotation tool
 * model training and hyperparameter tuning
 * deploy models in a lambda-like managed environment
 * deploy containers

Did an introductory tutorial that stepped through [Build, Train, and Deploy a Machine Learning Model][2] in a Jupyter notebook.

Set up a lambda and an API gateway in front of the model, following [Call an Amazon SageMaker model endpoint using Amazon API Gateway and AWS Lambda][3].

The lambda accesses the model like this:

> runtime= boto3.client('runtime.sagemaker')
> def lambda_handler(event, context):
>   ...
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
>   ...

Once th API gateway was in place, it was available from guest wifi on public internet, but somehow [got a 403 Forbidden error from inside VPC][4]???


[1]: https://www.youtube.com/watch?v=Bus4ldBVgLM
[2]: https://aws.amazon.com/getting-started/tutorials/build-train-deploy-machine-learning-model-sagemaker
[3]: https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/
[4]: https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-vpc-connections/
