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
    resp= items.get_item(Key={"item_id":item_id})
    if "Item" in resp and resp['Items'][0]['supplier_email']==email::
        response = items.update_item(
            Key={
                'item_id': item_id,
            },
            UpdateExpression="set quantity_available = :quantity_available, price= :price, prod_name= :prod_name",
            ExpressionAttributeValues={
                ':quantity_available': quantity_available,
                ':price': price,
                ':prod_name': prod_name
            },
            ReturnValues="UPDATED_NEW"
        )
        return{'statusCode': 200,
        'body': json.dumps('Updated')}
    else:
        return{'statusCode': 200,
        'body': json.dumps('Error')}