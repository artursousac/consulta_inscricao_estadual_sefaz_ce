from telegram import enviar_dados_telegram
from sefaz import buscar_inscricao_estadual
from dotenv import load_dotenv
import os

load_dotenv()
token_telegram = os.getenv("TOKEN_TELEGRAM")
chat_id_telegram = os.getenv("CHAT_ID")

enviar_dados_telegram(buscar_inscricao_estadual("cnpj"), token_telegram, chat_id_telegram)
