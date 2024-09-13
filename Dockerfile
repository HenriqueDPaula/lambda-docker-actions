# Usar uma imagem base Python específica para Lambda
FROM public.ecr.aws/lambda/python:3.9

# Copiar a aplicação para o container
COPY app/ ${LAMBDA_TASK_ROOT}

# Definir o handler da função Lambda
CMD ["lambda_function.lambda_handler"]