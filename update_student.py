import os
import boto3

def handler(event, context):
    # Get the DynamoDB table name from environment variables
    table_name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    student_id = event['pathParameters']['studentId']
    updated_data = event['body']
    
    # Assuming updated_data contains the updated fields (e.g., name, age, grade)
    response = table.update_item(
        Key={'studentId': student_id},
        UpdateExpression="SET #name = :name, #age = :age, #grade = :grade",
        ExpressionAttributeNames={
            '#name': 'name',
            '#age': 'age',
            '#grade': 'grade'
        },
        ExpressionAttributeValues={
            ':name': updated_data['name'],
            ':age': updated_data['age'],
            ':grade': updated_data['grade']
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': f"Student {student_id} updated successfully!"
    }
