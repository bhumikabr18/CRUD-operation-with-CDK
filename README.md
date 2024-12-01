# CRUD-operation-with-CDK

# Student CRUD Operations using AWS Lambda, DynamoDB, API Gateway, and CDK
This project demonstrates how to implement a simple CRUD (Create, Read, Update, Delete) operation for managing student data using AWS services, including AWS Lambda, DynamoDB, and API Gateway. The application allows users to interact with a DynamoDB table through HTTP requests exposed via API Gateway, with all operations being handled by Lambda functions written in Python using the boto3 AWS SDK. The project leverages AWS Cloud Development Kit (CDK) to provision and manage the infrastructure, making it easy to deploy and scale.
<br>

# Features
* Create, Read, Update, and Delete student data stored in DynamoDB.
* API endpoints exposed via API Gateway for interacting with Lambda functions.
* Serverless architecture, with infrastructure fully managed by AWS CDK.

# Architecture
1. AWS Lambda:

* Serverless compute service that runs the Python functions to handle CRUD operations (Create, Read, Update, Delete) for student data.
* Each Lambda function is triggered by corresponding HTTP requests sent to the API Gateway.

2. Amazon DynamoDB:

* A fully managed NoSQL database used to store and manage student data.
* The student data is stored in a table with the primary key student_id.

3. AWS API Gateway:

* Exposes RESTful API endpoints that handle incoming HTTP requests.
* Routes requests to the appropriate Lambda function for processing based on the HTTP method (POST, GET, PUT, DELETE).

4. AWS CDK (Cloud Development Kit):

* Used to define and deploy the infrastructure as code (IaC).
* Automatically provisions the Lambda functions, API Gateway, and DynamoDB table, making the deployment and management process easier and more scalable.

# Technologies Used

* AWS Lambda: For executing Python functions in response to API requests.
* Amazon DynamoDB: For storing and managing student data.
* AWS API Gateway: For exposing RESTful APIs to interact with Lambda functions.
* AWS CDK: For defining and deploying AWS infrastructure.

# How It Works
1. Create Operation (POST):

* The client sends a POST request with student details (e.g., student_id, name, age).
* API Gateway triggers the Lambda function responsible for creating a student record.
* The Lambda function writes the data to DynamoDB.

2. Read Operation (GET):

* The client sends a GET request with a student_id.
* API Gateway triggers the Lambda function responsible for fetching the student data from DynamoDB.
* The Lambda function retrieves the record from DynamoDB and returns it to the client.

3. Update Operation (PUT):

* The client sends a PUT request with the updated student details and student_id.
* API Gateway triggers the Lambda function that updates the student record in DynamoDB.
* The Lambda function modifies the existing record based on the student_id.

4. Delete Operation (DELETE):

* The client sends a DELETE request with the student_id to remove the student record.
* API Gateway triggers the Lambda function responsible for deleting the student record from DynamoDB.
* The Lambda function deletes the record from the database.

5. Deployment:

* AWS CDK is used to define the infrastructure, including the Lambda functions, API Gateway, and DynamoDB table.
* Once the infrastructure is defined in the CDK stack, running the cdk deploy command provisions all resources in the AWS environment.
* API Gateway provides the URL for accessing the CRUD operations through HTTP requests.

This architecture enables efficient, scalable CRUD operations for managing student data with minimal infrastructure management.




















