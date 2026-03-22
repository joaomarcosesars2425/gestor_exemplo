
# ==============================
# utilizador.py
# CRUD simples para entidade Utilizador
# SEM utilização de classes
# armazenamento em dicionario
# validações feitas aqui (não no main)
# ==============================

from utils import gerar_id_utilizador, validar_data

utilizadores = {}


# CREATE

def criar_utilizador(nome, email, tipo_conta, data_nascimento):
    if not validar_data(data_nascimento):
        print("Data inválida. Utilize formato YYYY-MM-DD.")
        return

    id_utilizador = gerar_id_utilizador()

    utilizadores[id_utilizador] = {
        "nome": nome,
        "email": email,
        "tipo_conta": tipo_conta,
        "data_nascimento": data_nascimento
    }

    print(f"Utilizador criado com sucesso. ID: {id_utilizador}")


# READ (listar todos)

def listar_utilizadores():
    if not utilizadores:
        print("Não existem utilizadores registados.")
        return

    for id_utilizador, dados in utilizadores.items():
        print(f"ID: {id_utilizador} | Nome: {dados['nome']} | Email: {dados['email']} | Tipo: {dados['tipo_conta']} | Data Nascimento: {dados['data_nascimento']}")


# READ (consultar individual)

def consultar_utilizador(id_utilizador):
    if id_utilizador not in utilizadores:
        print("Utilizador não encontrado.")
        return

    print(utilizadores[id_utilizador])


# UPDATE

def atualizar_utilizador(id_utilizador, nome=None, email=None, tipo_conta=None, data_nascimento=None):
    if id_utilizador not in utilizadores:
        print("Utilizador não encontrado.")
        return

    if data_nascimento:
        if not validar_data(data_nascimento):
            print("Data inválida. Utilize formato YYYY-MM-DD.")
            return
        utilizadores[id_utilizador]["data_nascimento"] = data_nascimento

    if nome:
        utilizadores[id_utilizador]["nome"] = nome

    if email:
        utilizadores[id_utilizador]["email"] = email

    if tipo_conta:
        utilizadores[id_utilizador]["tipo_conta"] = tipo_conta

    print("Utilizador atualizado com sucesso.")


# DELETE

def remover_utilizador(id_utilizador):
    if id_utilizador not in utilizadores:
        print("Utilizador não encontrado.")
        return

    del utilizadores[id_utilizador]
    print("Utilizador removido com sucesso.")

