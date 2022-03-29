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
    resp1=table_EkartItems.query(KeyConditionExpression=Key('item_id').eq(item_id))
    if resp1['Items'][0]['supplier_email']==email:
        response = table_EkartItems.delete_item(
            Key={
                'item_id': item_id,
            },
            ConditionExpression="attribute_exists (item_id)",
        )
        return{'statusCode': 200,
        'body': json.dumps('Successfully deleted the product')}
    else:
        return{'statusCode': 200,
        'body': json.dumps('Error while deleting')}