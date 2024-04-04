import boto3

import json

def handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("EnDyDBTable")
        item_json = json.dumps(event)
        item_data = json.loads(item_json)
        my_date = item_data.get('date')
        temp_data = get_date(table)
        print(f" the {temp_data}")
        if temp_data:
            for item_val in temp_data:
                temp_date = item_val['date']
            if temp_date == my_date:
                print(f"{my_date} already exists!!!")

            else:
                print("Date not equal")
                delete_item(table, temp_date)
        else:
            print("New item")
        return item_data
    except Exception as e:
        print(e)


def get_date(table):

    response = table.scan()
    print(f"the response is {response}")
    print(f" The item is : {response['Items']}")
    return response['Items']    


def delete_item(table, item_id):
    response = table.delete_item(Key={"date": item_id, "section": "Home"})
    print(response)
    print("Deleting")
    return response
