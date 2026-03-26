# ==============================
# utils.py
# funções auxiliares
# ==============================

from datetime import datetime

# contador simples para gerar IDs automáticos
contador_ids = 1


def gerar_id_utilizador():
    global contador_ids
    novo_id = f"U{contador_ids:03d}"
    contador_ids += 1
    return novo_id


# validação de data no formato YYYY-MM-DD

def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False

