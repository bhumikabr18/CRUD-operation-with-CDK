from aws_cdk import (
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    RemovalPolicy,
    Duration
)
from constructs import Construct
from aws_cdk import Stack

class DynamoDbCrudStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create DynamoDB Table
        student_table = dynamodb.Table(
            self, "StudentTable",
            partition_key=dynamodb.Attribute(name="studentId", type=dynamodb.AttributeType.STRING),
            removal_policy=RemovalPolicy.DESTROY  # Only for dev/test environments
        )

        # Lambda function for Create Operation
        create_lambda = lambda_.Function(
            self,
            "CreateStudentLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="create_student.handler",
            code=lambda_.Code.from_asset("cdk-dynamodb-crud"),
            environment={
                "TABLE_NAME": student_table.table_name  # Pass table name as environment variable
            },
            timeout=Duration.seconds(10),  # Increase timeout to 10 seconds
            memory_size=1024  # Increase memory for better performance
        )

        # Lambda function for Read Operation
        read_lambda = lambda_.Function(
            self,
            "ReadStudentLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="read_student.handler",
            code=lambda_.Code.from_asset("cdk-dynamodb-crud"),
            environment={
                "TABLE_NAME": student_table.table_name
            },
            timeout=Duration.seconds(10),
            memory_size=1024
        )

        # Lambda function for Update Operation
        update_lambda = lambda_.Function(
            self,
            "UpdateStudentLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="update_student.handler",
            code=lambda_.Code.from_asset("cdk-dynamodb-crud"),
            environment={
                "TABLE_NAME": student_table.table_name
            },
            timeout=Duration.seconds(10),
            memory_size=1024
        )

        # Lambda function for Delete Operation
        delete_lambda = lambda_.Function(
            self,
            "DeleteStudentLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="delete_student.handler",
            code=lambda_.Code.from_asset("cdk-dynamodb-crud"),
            environment={
                "TABLE_NAME": student_table.table_name
            },
            timeout=Duration.seconds(10),
            memory_size=1024
        )

        # Grant the Lambda functions permission to read/write to the DynamoDB table
        student_table.grant_read_write_data(create_lambda)
        student_table.grant_read_write_data(read_lambda)
        student_table.grant_read_write_data(update_lambda)
        student_table.grant_read_write_data(delete_lambda)

        # Create an API Gateway to expose the Lambda functions
        api = apigateway.RestApi(self, "student-api", description="Student API")

        # Define API Gateway resources and methods
        students_resource = api.root.add_resource("students")
        students_resource.add_method("POST", apigateway.LambdaIntegration(create_lambda))  # POST /students (Create)
        students_resource.add_method("GET", apigateway.LambdaIntegration(read_lambda))    # GET /students (Read)

        student_resource = students_resource.add_resource("{studentId}")
        student_resource.add_method("PUT", apigateway.LambdaIntegration(update_lambda))  # PUT /students/{studentId} (Update)
        student_resource.add_method("DELETE", apigateway.LambdaIntegration(delete_lambda))  # DELETE /students/{studentId} (Delete)

    
    
    
    
    
    
    
    
    
    