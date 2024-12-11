import os
import boto3

def handler(event, context):
    # Get the DynamoDB table name from environment variables
    table_name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    student_id = event['pathParameters']['studentId']

    # Get the student record from DynamoDB
    response = table.get_item(
        Key={'studentId': student_id}
    )

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': f"Student with ID {student_id} not found"
        }

    student = response['Item']
    
    return {
        'statusCode': 200,
        'body': student
    }
