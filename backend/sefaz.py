from playwright.sync_api import sync_playwright
import re

from telegram import enviar_dados_telegram
def buscar_dados_sefaz(cnpj):
    # Realiza o tratamento do CNPJ, retirando . - /
    cnpj = re.sub(r'[.\-\/\s]', '', cnpj)

    # Define a URL da Chamada HTTP
    url = f"https://consultapublica.sefaz.ce.gov.br/sintegra/consultar?tipdocumento=2&numcnpjcgf={cnpj}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)
        page.wait_for_timeout(5000)

        try:
            ie = page.locator('table#dadossintegra td').nth(1).text_content()

            return {
                "inscricao_estadual": ie
            }
        except Exception as e:
            return {"erro": f"Erro ao localizar dados: {e}"}
        finally:
            browser.close()

