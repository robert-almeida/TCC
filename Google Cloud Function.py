from google.cloud import storage
import requests
import json
import flask

def upload_blob(bucket_name, blob_text, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(blob_text)

def open_weather(request):
    data = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=3448439&appid=88ba6892440e19931ca07aa87ae42b5d&units=metric').json()
    BUCKET_NAME = 'tccbucket'
    BLOB_NAME = 'forecast'
    BLOB_STR = json.dumps(data)

    upload_blob(BUCKET_NAME, BLOB_STR, BLOB_NAME)
    return f'forecast json file success uploaded!'
