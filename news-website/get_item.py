import boto3
import datetime

def handler(event, context):
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("EnDyDBTable")
    my_date = str(datetime.datetime.now().date())
    response = table.get_item(Key={"date": my_date, "section": "Home"})
    print(f" The item in API Gateway : {response.get('Item')}")
    return response.get("Item")
