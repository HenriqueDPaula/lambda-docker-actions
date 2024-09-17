import json
from lambda_function_log import Logger
import boto3

logger = Logger()

nome_tabela = "eventos_lambda"
dynamo = boto3.resource('dynamodb').Table(nome_tabela)

def create(request):
    return dynamo.put_item(request)

def read(request):
    return dynamo.scan()

def echo(request):
    return request

operations = {
    'create': create,
    'read': read,
    'echo': echo
}

def lambda_handler(event, context):
    logger.info('received event from handler' + json.dumps(event))

    method = event['method']
    request = event['data']

    if method in operations:
        return operations[method](request)