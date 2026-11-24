
import vendedores


def exibir_menu():
    print("\n" + "=" * 40)
    print("              PARK FLOW")
    print("         SISTEMA DE VEÍCULOS")
    print("=" * 40)

    print("\n1 - Cadastrar vendedor")
    print("2 - Listar vendedores")
    print("3 - Cadastrar cliente")
    print("4 - Cadastrar veículo")
    print("5 - Compra e venda")
    print("6 - Aluguel de veículos")
    print("0 - Sair")


def iniciar_sistema():
    while True:
        exibir_menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            vendedores.cadastrar_vendedor()

        elif opcao == "2":
            print("\nCarregando vendedores...")
            vendedores.listar_vendedores()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "3":
            print("\nCadastro de clientes em desenvolvimento.")

        elif opcao == "4":
            print("\nCadastro de veículos em desenvolvimento.")

        elif opcao == "5":
            print("\nMódulo de compra e venda em desenvolvimento.")

        elif opcao == "6":
            print("\nMódulo de aluguel em desenvolvimento.")

        elif opcao == "0":
            print("\nEncerrando o Park Flow...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
