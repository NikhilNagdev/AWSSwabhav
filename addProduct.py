import json
import uuid
import boto3
from boto3.dynamodb.conditions import Key,Attr
dynamodb = boto3.resource('dynamodb')
items = dynamodb.Table('products')

def lambda_handler(event, context):
    # TODO implement
    item_id = event["item_id"]
    item_name = event["name"]
    price = event["price"]
    quantity = event["quantity"]
    supplier_email = event["email"]
    
    
    resp= items.get_item(Key={"id":item_id})
    print(resp)
   
    if "Item" in resp:
         return {
        'statusCode': 200,
        'body': json.dumps('Product ID already exist')
    }

    else:
        a=items.put_item(Item={"id":item_id,"supplier_email":supplier_email,"price":price,"name":item_name,"quantity":quantity})
    
    return {
        'statusCode': 200,
        'body': json.dumps('Product Added')
    }
