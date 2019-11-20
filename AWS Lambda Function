from botocore.vendored import requests
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    data = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=3448439&appid=88ba6892440e19931ca07aa87ae42b5d&units=metric').json()
    
    client = boto3.client('s3')
    response = client.put_object(Bucket='buckettcc', Body=json.dumps(data), Key='api_response.json')
    
    return {
        'statusCode': 200,
        'body': "SUCCESS"
    }
