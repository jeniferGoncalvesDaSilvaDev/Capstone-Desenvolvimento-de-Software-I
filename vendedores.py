
import json
import os

ARQUIVO = "vendedores.json"


def carregar_vendedores():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


vendedores = carregar_vendedores()


def salvar_vendedores():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(vendedores, arquivo, indent=4, ensure_ascii=False)


def cadastrar_vendedor():
    print("\n===== CADASTRO DE VENDEDORES =====")

    id_vendedor = max(
        [v["id"] for v in vendedores], default=0
    ) + 1

    nome = input("Digite o nome do vendedor: ")
    cpf = input("Digite o CPF do vendedor: ")
    telefone = input("Digite o telefone do vendedor: ")
    email = input("E-mail: ")

    percentual_comissao = float(
        input("Percentual de comissão (%): ").replace(",", ".")
    )

    vendedor = {
        "id": id_vendedor,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "percentual_comissao": percentual_comissao,
        "status": "Ativo"
    }

    vendedores.append(vendedor)
    salvar_vendedores()

    print("\nVendedor cadastrado e salvo com sucesso!")
    print("ID:", vendedor["id"])
    print("Nome:", vendedor["nome"])
    print("CPF:", vendedor["cpf"])
    print("Telefone:", vendedor["telefone"])
    print("E-mail:", vendedor["email"])
    print("Comissão:", str(vendedor["percentual_comissao"]) + "%")
    print("Status:", vendedor["status"])


def listar_vendedores():
    print("\n===== LISTA DE VENDEDORES =====")

    if not vendedores:
        print("Nenhum vendedor cadastrado.")
        return

    for vendedor in vendedores:
        print("--------------------------")
        print("ID:", vendedor["id"])
        print("Nome:", vendedor["nome"])
        print("CPF:", vendedor["cpf"])
        print("Telefone:", vendedor["telefone"])
        print("E-mail:", vendedor["email"])
        print("Comissão:", str(vendedor["percentual_comissao"]) + "%")
        print("Status:", vendedor["status"])
