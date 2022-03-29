import json
import boto3
import base64
from boto3.dynamodb.conditions import Key,Attr
ddb = boto3.resource('dynamodb')

users=ddb.Table('users')
print(users)

def lambda_handler(event, context):
    # TODO implement
    email=event['email']
    pwd=encodePass(event['pwd'])
    resp= users.get_item(Key={"email":email})
    print(resp)
    if "Item" in resp:
        pwdDB=resp['Item']['pwd']
        if pwdDB==pwd:
            print("Exist")
            return{'statusCode': 200,
            'body': json.dumps("Logged ")}
        else:
            return{'statusCode': 200,
            'body': json.dumps('Not Authenticated')}
    return {
    'statusCode': 200,
    'body': json.dumps('Not Authenticated')
    }
    
def encodePass(pwd):
    string_bytes = pwd.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string