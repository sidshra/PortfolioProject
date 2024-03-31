import boto3
import datetime
import json

def handler(event, context):
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("EnDyDBTable")
    item_json = json.dumps(event)
    # item_data = event.get("Payload")
    # item_data = event.get('responseData','')
    item_data = json.loads(item_json)
    print(json.dumps(event))
    my_date = str(datetime.datetime.now().date())
    print(my_date)
    if item_data['date'] == my_date:
        
   
    response = table.get_item(Key={"date": my_date, "section": "Home"})
    print(response)
    print(f" The item in API Gateway : {response.get('Item')}")
    return response
