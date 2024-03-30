import boto3

import json

def handler(event, context):
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("EnDyDBTable")
    item_data = event["Payload"]
    # item_data = json.loads(item_json)
    # print(json.dumps(event))
    # item = item_data["detail"]["item"]
    print(item_data)

    # item = {'date' : "2024-03-28", 'section' : "Home", 'content' : ["My content","No"]}
    response = table.put_item(Item=item_data)
    print(response)
    return response
