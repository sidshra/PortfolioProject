import boto3
import json

def handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("EnDyDBTable")
        item_json = json.dumps(event)
        item_data = json.loads(item_json)
        print(item_data)
        response = table.put_item(Item=item_data)
        print(response)
        return response
    except Exception as e:
        print(e)

        
