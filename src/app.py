# app.py — Interface gráfica CRUD com Tkinter

import tkinter as tk
from tkinter import ttk, messagebox

from utilizador import (
    criar_utilizador,
    listar_utilizadores,
    consultar_utilizador,
    atualizar_utilizador,
    remover_utilizador
)


# =====================================
# FUNÇÕES
# =====================================

# criar utilizador
# -------------------------------------
def criar():
    nome = entry_nome.get()
    email = entry_email.get()
    tipo = entry_tipo.get()
    data = entry_data.get()

    code, obj = criar_utilizador(nome, email, tipo, data)

    if code == 201:
        messagebox.showinfo("Sucesso", "Utilizador criado com sucesso.")
        limpar_campos()
        carregar_tabela()
    else:
        messagebox.showerror("Erro", str(obj))


# listar utilizadores
# -------------------------------------
def carregar_tabela():

    # limpar tabela
    for item in tabela.get_children():
        tabela.delete(item)

    code, obj = listar_utilizadores()

    if code == 200:
        for id_utilizador, dados in obj.items():
            tabela.insert(
                "",
                tk.END,
                values=(
                    id_utilizador,
                    dados["nome"],
                    dados["email"],
                    dados["tipo_conta"],
                    dados["data_nascimento"]
                )
            )


# selecionar utilizador da tabela
# -------------------------------------
def selecionar_utilizador(event):
    selecionado = tabela.focus()

    if not selecionado:
        return

    valores = tabela.item(selecionado, "values")

    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_id.insert(0, valores[0])
    entry_id.config(state="readonly")

    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, valores[1])

    entry_email.delete(0, tk.END)
    entry_email.insert(0, valores[2])

    entry_tipo.delete(0, tk.END)
    entry_tipo.insert(0, valores[3])

    entry_data.delete(0, tk.END)
    entry_data.insert(0, valores[4])


# consultar utilizador
# -------------------------------------
def consultar():
    id_utilizador = entry_id.get()

    if not id_utilizador:
        messagebox.showwarning("Aviso", "Selecione um utilizador.")
        return

    code, obj = consultar_utilizador(id_utilizador)

    if code == 200:
        messagebox.showinfo(
            "Consulta",
            f"Nome: {obj['nome']}\n"
            f"Email: {obj['email']}\n"
            f"Tipo: {obj['tipo_conta']}\n"
            f"Data Nascimento: {obj['data_nascimento']}"
        )
    else:
        messagebox.showerror("Erro", str(obj))


# atualizar utilizador
# -------------------------------------
def atualizar():
    id_utilizador = entry_id.get()

    if not id_utilizador:
        messagebox.showwarning("Aviso", "Selecione um utilizador.")
        return

    nome = entry_nome.get()
    email = entry_email.get()
    tipo = entry_tipo.get()
    data = entry_data.get()

    code, obj = atualizar_utilizador(
        id_utilizador,
        nome,
        email,
        tipo,
        data
    )

    if code == 200:
        messagebox.showinfo("Sucesso", "Utilizador atualizado com sucesso.")
        carregar_tabela()
        limpar_campos()
    else:
        messagebox.showerror("Erro", str(obj))


# remover utilizador
# -------------------------------------
def remover():
    id_utilizador = entry_id.get()

    if not id_utilizador:
        messagebox.showwarning("Aviso", "Selecione um utilizador.")
        return

    resposta = messagebox.askyesno(
        "Confirmação",
        "Tem a certeza que pretende remover este utilizador?"
    )

    if resposta:
        code, obj = remover_utilizador(id_utilizador)

        if code == 200:
            messagebox.showinfo("Sucesso", "Utilizador removido.")
            carregar_tabela()
            limpar_campos()
        else:
            messagebox.showerror("Erro", str(obj))


# limpar campos
# -------------------------------------
def limpar_campos():
    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_id.config(state="readonly")

    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_tipo.delete(0, tk.END)
    entry_data.delete(0, tk.END)


# =====================================
# JANELA PRINCIPAL
# =====================================

janela = tk.Tk()
janela.title("Sistema CRUD Utilizadores")
janela.geometry("950x600")


# =====================================
# FRAME FORMULÁRIO
# =====================================

frame_form = tk.Frame(janela)
frame_form.pack(pady=10)


# ID
# -------------------------------------
tk.Label(frame_form, text="ID").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_form, width=30, state="readonly")
entry_id.grid(row=0, column=1, padx=5, pady=5)


# Nome
# -------------------------------------
tk.Label(frame_form, text="Nome").grid(row=1, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=1, column=1, padx=5, pady=5)


# Email
# -------------------------------------
tk.Label(frame_form, text="Email").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)


# Tipo Conta
# -------------------------------------
tk.Label(frame_form, text="Tipo Conta").grid(row=3, column=0, padx=5, pady=5)
entry_tipo = tk.Entry(frame_form, width=30)
entry_tipo.grid(row=3, column=1, padx=5, pady=5)


# Data Nascimento
# -------------------------------------
tk.Label(frame_form, text="Data Nascimento").grid(row=4, column=0, padx=5, pady=5)
entry_data = tk.Entry(frame_form, width=30)
entry_data.grid(row=4, column=1, padx=5, pady=5)


# =====================================
# FRAME BOTÕES
# =====================================

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)


btn_criar = tk.Button(frame_botoes, text="Criar", width=15, command=criar)
btn_criar.grid(row=0, column=0, padx=5)

btn_consultar = tk.Button(frame_botoes, text="Consultar", width=15, command=consultar)
btn_consultar.grid(row=0, column=1, padx=5)

btn_atualizar = tk.Button(frame_botoes, text="Atualizar", width=15, command=atualizar)
btn_atualizar.grid(row=0, column=2, padx=5)

btn_remover = tk.Button(frame_botoes, text="Remover", width=15, command=remover)
btn_remover.grid(row=0, column=3, padx=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar", width=15, command=limpar_campos)
btn_limpar.grid(row=0, column=4, padx=5)


# =====================================
# TABELA
# =====================================

frame_tabela = tk.Frame(janela)
frame_tabela.pack(pady=20)


colunas = (
    "ID",
    "Nome",
    "Email",
    "Tipo Conta",
    "Data Nascimento"
)


# Treeview
# -------------------------------------
tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show="headings",
    height=15
)


# cabeçalhos
# -------------------------------------
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=180)


# mostrar tabela
# -------------------------------------
tabela.pack(side=tk.LEFT)


# scrollbar
# -------------------------------------
scrollbar = ttk.Scrollbar(
    frame_tabela,
    orient="vertical",
    command=tabela.yview
)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# associar scrollbar
# -------------------------------------
tabela.configure(yscrollcommand=scrollbar.set)


# evento clique
# -------------------------------------
tabela.bind("<<TreeviewSelect>>", selecionar_utilizador)


# =====================================
# INICIAR
# =====================================

carregar_tabela()

janela.mainloop()
