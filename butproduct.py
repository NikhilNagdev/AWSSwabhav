import json
import boto3
from boto3.dynamodb.conditions import Key,Attr
from datetime import datetime

ddb = boto3.resource('dynamodb')

items=ddb.Table('products')
cart=ddb.Table('cart')


def lambda_handler(event, context):
    # TODO implement
    print(event['email'],event['item_id'],event['quantity'])
    email=event['email']
    item_id=event['item_id']
    quantity=event['quantity']
    print(items)
    resp=items.get_item(Key={"id":item_id})
    # resp=items.scan(FilterExpression=Attr('id').ne(1))
    if "Item" not in resp:
        return{'statusCode': 200,
        'body': json.dumps('Product doesnt exist')}
    price=int(resp['Item']['price'])
    product_quantity=int(resp['Item']['quantity'])
    product_name=resp['Item']['name']
    print(resp)
    if (product_quantity-quantity)<0:
        return{'statusCode': 200,
        'body': json.dumps('There is no quantity')}
    # resp=cart.scan(FilterExpression=Attr('item_id').eq(item_id))
    # resp= cart.get_item(Key={"item_id":item_id})
    resp= cart.get_item(Key={"email":email,"item_id":item_id})
    print(resp)
   
    if "Item" in resp:
        print("Found")
        quantityInDB=int(resp['Item']['quantity'])
        total_amountIn_DB=int(resp['Item']['amount'])
        response = cart.update_item(
            Key={
                'item_id': item_id,
                'email':email
            },
            UpdateExpression="set quantity = :quantity, amount= :amount",
            ExpressionAttributeValues={
                ':quantity': str(quantityInDB+int(quantity)),
                ':amount': str(total_amountIn_DB+int(quantity)*price)
            },
            ReturnValues="UPDATED_NEW"
        )
        items.update_item(
        Key={
            'id': item_id,
        },UpdateExpression="set quantity = :quantity",ExpressionAttributeValues={':quantity': product_quantity-1,},
        ReturnValues="UPDATED_NEW"
    )
    else:
        print("Not Found")
        am = str(price*int(quantity))
        cart.put_item(Item={"item_id":item_id,"email":email,"order_status":"ordered",
        "name":product_name,"quantity":quantity,"amount":am})
        items.update_item(
        Key={
            'id': item_id,
        },UpdateExpression="set quantity = :quantity",ExpressionAttributeValues={':quantity': str(product_quantity-1),},
        ReturnValues="UPDATED_NEW"
    )
    
    return{'statusCode': 200,
    'body': json.dumps('Successfull')}