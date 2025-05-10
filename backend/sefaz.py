import requests
from bs4 import BeautifulSoup
import re

def limpar_cnpj(cnpj):
    return re.sub(r'[.\-\/\s]', '', cnpj)

def buscar_inscricao_estadual(cnpj):
    cnpj = limpar_cnpj(cnpj)
    url = f"https://consultapublica.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf={cnpj}"

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        tabela = soup.find("table", id="dadossintegra")
        if not tabela:
            return {"erro": "Tabela 'dadossintegra' não encontrada"}

        # Agora pega especificamente o tbody
        tbody = tabela.find("tbody")
        linha = tbody.find("tr") if tbody else None
        if not linha:
            return {"erro": "Linha de dados não encontrada"}

        colunas = linha.find_all("td")
        if len(colunas) >= 3:
            return {
                "inscricao_estadual": colunas[1].text.strip()
            }
        else:
            return {"erro": "Colunas de dados não encontradas"}

    except Exception as e:
        return {"erro": f"Erro ao processar: {str(e)}"}
