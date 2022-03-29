import json
import uuid
import boto3
from boto3.dynamodb.conditions import Key,Attr
dynamodb = boto3.resource('dynamodb')
cart = dynamodb.Table('cart')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    params=event['queryStringParameters']
    print(params['email'])
    email=params['email']
    resp=cart.scan(FilterExpression=Attr('email').eq(email))
    if "Items" in resp:
        return{'statusCode': 200,
        'body': json.dumps(resp["Items"])}

    return {
        'statusCode': 200,
        'body': json.dumps('No items')
    }
