import json

def lambda_handler(event, context):
    message = "hey ramesh -  deployed by GitHub Action"
    print(message)

    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }
