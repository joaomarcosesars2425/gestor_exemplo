
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

            code, obj = criar_utilizador(nome, email, tipo, data_nascimento)
            if code == 201:
                print("Utilizador criado com sucesso." + str(obj))
            else:
                print("Internal Error: " + str(obj))

        elif opcao == "2":
            code, obj = listar_utilizadores()
            if code == 200:
                print("Lista de utilizadores:")
                for id_utilizador, dados in obj.items():
                    print(f"ID: {id_utilizador} | Nome: {dados['nome']} | Email: {dados['email']} | Tipo: {dados['tipo_conta']} | Data Nascimento: {dados['data_nascimento']}")

            else:
                print(str(code) + ": " + str(obj))

        elif opcao == "3":
            id_utilizador = input("ID do utilizador: ")
            code, obj = consultar_utilizador(id_utilizador)
            if code == 200:
                print("Utilizador" + id_utilizador + ":")
                print(obj)

            else:
                print("Internal Error: " + str(obj))
        elif opcao == "4":
            id_utilizador = input("ID do utilizador: ")

            nome = input("Novo nome (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            tipo = input("Novo tipo (enter para manter): ")
            data = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")

            code, obj = atualizar_utilizador(
                id_utilizador,
                nome if nome else None,
                email if email else None,
                tipo if tipo else None,
                data if data else None
            )
            if code == 200:
                print("Utilizador actualizado com sucesso: \n" + str(obj))
            else:
                print("Internal Error: " + str(obj))

        elif opcao == "5":
            id_utilizador = input("ID do utilizador: ")
            code, obj = remover_utilizador(id_utilizador)
            if code == 200:
                print("Utilizador removido com sucesso: " + obj)
            else:
                print("Internal Error: " + obj)
        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
