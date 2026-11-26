
import os


PRIORIDADES_VALIDAS = [
    "Baixa",
    "Média",
    "Alta",
    "Crítica"
]


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_cabecalho(titulo):
    """Exibe um cabeçalho organizado."""
    print("\n" + "=" * 45)
    print(titulo.center(45))
    print("=" * 45)


def ler_texto(mensagem):
    """Solicita um texto que não pode ficar vazio."""
    while True:
        try:
            texto = input(mensagem).strip()

            if texto:
                return texto

            print("Erro: o campo não pode ficar vazio.")

        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada.")
            return None


def ler_inteiro(mensagem):
    """Solicita um número inteiro válido."""
    while True:
        try:
            return int(input(mensagem).strip())

        except ValueError:
            print("Erro: digite um número inteiro.")

        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada.")
            return None


def ler_valor(mensagem):
    """Solicita um valor monetário não negativo."""
    while True:
        try:
            valor = input(mensagem).strip()
            valor = float(valor.replace(",", "."))

            if valor < 0:
                print("Erro: o valor não pode ser negativo.")
                continue

            return valor

        except ValueError:
            print("Digite um valor válido. Exemplo: 1500,50.")

        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada.")
            return None


def validar_prioridade(prioridade):
    """Verifica se a prioridade é válida."""
    return prioridade.strip().casefold() in [
        item.casefold() for item in PRIORIDADES_VALIDAS
    ]


def formatar_cep(cep):
    """Formata um CEP com oito dígitos."""
    cep_limpo = "".join(
        caractere for caractere in cep
        if caractere.isdigit()
    )

    if len(cep_limpo) != 8:
        return None

    return f"{cep_limpo[:5]}-{cep_limpo[5:]}"