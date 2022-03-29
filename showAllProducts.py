import json
import boto3
from boto3.dynamodb.conditions import Key,Attr
dynamodb = boto3.resource('dynamodb')
items = dynamodb.Table('products')


def lambda_handler(event, context):
    # TODO implement
    
    print("Event", event)
    # params=event['queryStringParameters']
    # print(params['email'])
    # email=params['email']
    resp=items.scan(FilterExpression=Attr('supplier_email').ne(email))
    print("Products",resp['Items'])

    if "Items" in resp:
        return{'statusCode': 200,
        'body': json.dumps(resp["Items"])}
    else :
        return {
            'statusCode': 200,
            'body': json.dumps('Not present')
        }
