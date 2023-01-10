import json
import os
import boto3

# Environment variables
SHOP_TABLE = os.environ["SHOP_DYNAMODB_TABLE"]

# Set up boto3 Table resource
ddb = boto3.resource("dynamodb")
table = ddb.Table(SHOP_TABLE)


def lambda_handler(event, context):
    response = []
    for item in event:
        item = json.loads(item["body"])
        customer_id = item["Customer"]["Id"]
        result = table.get_item(
            Key={
                "PK": f"CUST#{customer_id}",
                "SK": "META"
            }
        )
        result = result["Item"]

        item["Customer"]["Name"] = result["Name"]
        item["Customer"]["EmailAddress"] = result["EmailAddress"]

        response.append(item)

    return response
