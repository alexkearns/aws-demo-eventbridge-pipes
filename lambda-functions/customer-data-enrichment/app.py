import os
import boto3

# Environment variables
SHOP_TABLE = os.environ["SHOP_DYNAMODB_TABLE"]

# Set up boto3 Table resource
ddb = boto3.resource("dynamodb")
table = ddb.Table(SHOP_TABLE)


def lambda_handler(event, context):
    customer_id = event["Customer"]["Id"]
    result = table.get_item(
        Key={
            "PK": f"CUST#{customer_id}",
            "SK": "META"
        }
    )
    item = result["Item"]

    event["Customer"]["Name"] = item["Name"]
    event["Customer"]["EmailAddress"] = item["EmailAddress"]

    return event
