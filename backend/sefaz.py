import http
import re
import requests
from telegram import enviar_dados_telegram
def buscar_dados_sefaz(cnpj):
    # Realiza o tratamento do CNPJ, retirando . - /
    cnpj = re.sub(r'[.\-\/\s]', '', cnpj)

    # Define a URL da Chamada HTTP
    url = f"https://consultapublica.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf={cnpj}"

    try:
        response = requests.get(url, timeout=10)  # Adiciona timeout por segurança
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return {"erro": "RJSON inválido"}
        else:
            return {"erro": f"Erro HTTP: {response.status_code}"}
    except requests.RequestException as e:
        return {"erro": f"Falha na requisição: {str(e)}"}

