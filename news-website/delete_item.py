import json


def handler(event,context):
    response = table.delete_item(
        Key={
            'date' : '2024-03-27',
            'section' : "Home"
        }
    )
    print("Successfully deleted")
    
