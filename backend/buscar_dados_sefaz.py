import re
import requests
def buscar_dados_sefaz(cnpj):
    # Realiza o tratamento do CNPJ, retirando . - /
    cnpj = re.sub(r'[.\-\/\s]', '', cnpj)
    print(cnpj)
    url = f"https://consultapublica.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf={cnpj}"