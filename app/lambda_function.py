import json
import boto3
import uuid 
from lambda_function_log import Logger

logger = Logger()

nome_tabela = "eventos_lambda_teste"
dynamo = boto3.resource('dynamodb').Table(nome_tabela)

def create(request):

    id = str(uuid.uuid4)

    evento = {
        'id_evento': id,
        'corpo': json.dumps(request)
    }

    logger.info(f'inserindo registro na tabela `{nome_tabela}` com id: {id}')
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