import json
from lambda_function_log import Logger

logger = Logger()

def lambda_handler(event, context):
    logger.info('received event from handler' + json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }