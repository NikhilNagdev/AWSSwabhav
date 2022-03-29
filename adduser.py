import json
import os
import boto3
import base64
from boto3.dynamodb.conditions import Key,Attr
from datetime import datetime

ddb = boto3.resource('dynamodb')

users=ddb.Table('users')
print(users)

def lambda_handler(event, context):
    # TODO implement
    print(event)
    registerUser(event)
    return {
        'statusCode': 200,
        'body': json.dumps('user created')
    }

def registerUser(event):
    print(event['email'],event['fname'],event['lname'],event['pwd'])
    email=event['email']
    fname=event['fname']
    lname=event['lname']
    pwd=encodePass(event['pwd'])
    resp= users.get_item(Key={"email":email})
    print(resp)
    if "Item" in resp:
        email=resp['Item']['email']
        print("User !! ",email)
        return{'statusCode': 200,
        'body': json.dumps('User ALready exists!!!')}
    
    r=users.put_item(Item={"email":email,"fname":fname,"lname":lname,"pwd":pwd})
    return {
    'statusCode': 200,
    'body': json.dumps('user created')
    }
    
def encodePass(pwd):
    string_bytes = pwd.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

    