import json
import boto3
import uuid 
from lambda_function_log import Logger

logger = Logger()

nome_tabela = "eventos_lambda_teste"
dynamo = boto3.resource('dynamodb').Table(nome_tabela)

def create(request):

    evento = {
        'id_evento': str(uuid.uuid4),
        'corpo': json.dumps(request)
    }

    return dynamo.put_item(Item=evento)

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