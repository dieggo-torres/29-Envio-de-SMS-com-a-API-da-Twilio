# Importação da biblioteca da Twilio
from twilio.rest import Client

# Importa a biblioteca os
import os

# Importa a biblioteca json
import json

# Importa um método da biblioteca python-dotenv
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém dados sensíveis
with open('segredos.json') as segredos:
    dados_sensiveis = json.load(segredos)

remetente = dados_sensiveis['meu_numero_twilio']
destinatario = dados_sensiveis['contato']

# SID da conta da Twilio
account_sid = os.getenv('ACCOUNT_SID')

# Token de autenticação da Twilio
auth_token = os.getenv('AUTH_TOKEN')

# Cria uma instância de cliente
cliente = Client(account_sid, auth_token)

# Mensagem
texto = 'Olá! Esta é uma mensagem enviada com a API da Twilio.'

# Cria uma mensagem para enviar via SMS
mensagem = cliente.messages.create(
    to=destinatario,
    from_=remetente,
    body=texto
)