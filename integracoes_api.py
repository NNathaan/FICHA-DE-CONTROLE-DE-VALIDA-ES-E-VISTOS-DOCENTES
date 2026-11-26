import urllib.request
import urllib.error
import json


def consultar_cep(cep):
    """Consulta um CEP na ViaCEP."""
    cep = "".join(c for c in str(cep) if c.isdigit())

    if len(cep) != 8:
        raise ValueError("CEP inválido")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError):
        print("Aviso: Sem conexão com a ViaCEP.")
        return None

    if dados.get("erro"):
        raise ValueError("CEP não encontrado")

    return dados


def consultar_cotacao_dolar():
    """Consulta a cotação do dólar."""
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError):
        print("Aviso: Sem conexão com a AwesomeAPI.")
        return None

    return float(dados["USDBRL"]["bid"])


if __name__ == "__main__":
    endereco = consultar_cep("01001-000")

    if endereco:
        print(endereco)

    cotacao = consultar_cotacao_dolar()

    if cotacao is not None:
        print("Dólar:", cotacao)