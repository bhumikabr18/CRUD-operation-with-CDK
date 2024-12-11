import os
import boto3

def handler(event, context):
    # Get the DynamoDB table name from environment variables
    table_name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    # Extract data from the event
    student_id = event['studentId']
    name = event['name']
    age = event['age']
    grade = event['grade']
    
    # Insert a new student record into the DynamoDB table
    table.put_item(
        Item={
            'studentId': student_id,
            'name': name,
            'age': age,
            'grade': grade,
        }
    )
    
    return {
        'statusCode': 200,
        'body': f"Student {name} created successfully!"
    }
