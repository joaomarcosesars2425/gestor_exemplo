
# ==============================
# main.py
# menu terminal para testar CRUD
# ==============================

from utilizador import (
    criar_utilizador,
    listar_utilizadores,
    consultar_utilizador,
    atualizar_utilizador,
    remover_utilizador
)


# menu
def menu():
    print("\n===== MENU UTILIZADOR =====")
    print("1 - Criar utilizador")
    print("2 - Listar utilizadores")
    print("3 - Consultar utilizador")
    print("4 - Atualizar utilizador")
    print("5 - Remover utilizador")
    print("0 - Sair")


# programa principal
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            tipo = input("Tipo de conta (free/premium): ")
            data_nascimento = input("Data nascimento (YYYY-MM-DD): ")

            return_code = criar_utilizador(nome, email, tipo, data_nascimento)
            if return_code[0] == 201:
                print("Utilizador criado com sucesso.")
            elif return_code[0] == 500:
                print("Internal Error: " + return_code[1])

        elif opcao == "2":
            return_code = listar_utilizadores()
            if return_code[0] == 200:
                print("Utilizador listado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            id_utilizador = input("ID do utilizador: ")
            return_code = consultar_utilizador(id_utilizador)
            if return_code[0] == 200:
                print("Utilizador listado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])
        elif opcao == "4":
            id_utilizador = input("ID do utilizador: ")

            nome = input("Novo nome (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            tipo = input("Novo tipo (enter para manter): ")
            data = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")

            return_code = atualizar_utilizador(
                id_utilizador,
                nome if nome else None,
                email if email else None,
                tipo if tipo else None,
                data if data else None
            )
            if return_code[0] == 200:
                print("Utilizador actualizado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            id_utilizador = input("ID do utilizador: ")
            return_code = remover_utilizador(id_utilizador)
            if return_code[0] == 200:
                print("Utilizador removido com sucesso.")
            else:
                print("Internal Error: " + return_code[1])
        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()