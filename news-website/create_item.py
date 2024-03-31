import boto3

import json

def handler(event, context):
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("EnDyDBTable")
    item_json = json.dumps(event)
    #item_data = event.get("Payload")
    # item_data = event.get('responseData','')
    item_data = json.loads(item_json)
    print(json.dumps(event))
    # item = item_data["detail"]["item"]
    print(item_data)

   
    response = table.put_item(Item=item_data)
    print(response)
    return response
