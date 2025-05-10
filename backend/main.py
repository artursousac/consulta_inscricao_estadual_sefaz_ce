from telegram import enviar_dados_telegram
from sefaz import buscar_dados_sefaz
from dotenv import load_dotenv
import os

load_dotenv()
token_telegram = os.getenv("TOKEN_TELEGRAM")
chat_id_telegram_1 = os.getenv("CHAT_ID")
