import boto3
import datetime

def handler(event, context):
    try:

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("EnDyDBTable")
        my_date = str(datetime.datetime.now().date())
        print(my_date)
        temp_data = get_date(table)
        if temp_data:
            for item_val in temp_data:
                response = item_val
        else:
            print("Table is empty")
        
        print(f" The item in API Gateway : {response}")
        return response
    except Exception as e:
        print(e)


def get_date(table):
    response = table.scan()
    return response["Items"]
