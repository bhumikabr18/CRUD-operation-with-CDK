import os
import boto3

def handler(event, context):
    # Get the DynamoDB table name from environment variables
    table_name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    student_id = event['pathParameters']['studentId']
    
    # Delete the student record from DynamoDB
    table.delete_item(
        Key={'studentId': student_id}
    )
    
    return {
        'statusCode': 200,
        'body': f"Student {student_id} deleted successfully!"
    }
