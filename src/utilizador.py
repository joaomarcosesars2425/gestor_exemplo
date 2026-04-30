import json
import os

from utils import gerar_id_utilizador, validar_data

FICHEIRO_UTILIZADORES = "utilizadores.json"

utilizadores = {}


# ==========================
# Persistência
# ==========================
def guardar_utilizadores():
    with open(FICHEIRO_UTILIZADORES, "w", encoding="utf-8") as ficheiro:
        json.dump(utilizadores, ficheiro, indent=4, ensure_ascii=False)


def carregar_utilizadores():
    global utilizadores

    if os.path.exists(FICHEIRO_UTILIZADORES):
        with open(FICHEIRO_UTILIZADORES, "r", encoding="utf-8") as ficheiro:
            utilizadores = json.load(ficheiro)
    else:
        utilizadores = {}


# ==========================
# CREATE
# ==========================
def criar_utilizador(nome, email, tipo_conta, data_nascimento):
    carregar_utilizadores()

    if not validar_data(data_nascimento):
        return 500, "Data inválida. Utilize formato YYYY-MM-DD"

    id_utilizador = gerar_id_utilizador()

    utilizador = {
        "nome": nome,
        "email": email,
        "tipo_conta": tipo_conta,
        "data_nascimento": data_nascimento
    }

    utilizadores[id_utilizador] = utilizador
    guardar_utilizadores()

    return 201, utilizador


# ==========================
# READ ALL
# ==========================
def listar_utilizadores():
    carregar_utilizadores()

    if not utilizadores:
        return 404, "Não existem utilizadores registados."

    return 200, utilizadores


# ==========================
# READ ONE
# ==========================
def consultar_utilizador(id_utilizador):
    carregar_utilizadores()

    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."

    return 200, utilizadores[id_utilizador]


# ==========================
# UPDATE
# ==========================
def atualizar_utilizador(
    id_utilizador,
    nome=None,
    email=None,
    tipo_conta=None,
    data_nascimento=None
):
    carregar_utilizadores()

    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."

    if data_nascimento:
        if not validar_data(data_nascimento):
            return 500, "Data inválida"

        utilizadores[id_utilizador]["data_nascimento"] = data_nascimento

    if nome:
        utilizadores[id_utilizador]["nome"] = nome

    if email:
        utilizadores[id_utilizador]["email"] = email

    if tipo_conta:
        utilizadores[id_utilizador]["tipo_conta"] = tipo_conta

    guardar_utilizadores()

    return 200, utilizadores[id_utilizador]


# ==========================
# DELETE
# ==========================
def remover_utilizador(id_utilizador):
    carregar_utilizadores()

    if id_utilizador not in utilizadores:
        return 404, "Utilizador não encontrado."

    del utilizadores[id_utilizador]
    guardar_utilizadores()

    return 200, id_utilizador
