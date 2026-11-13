import sqlite3
import tkinter as tk
from tkinter import messagebox


# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
def inicializar_banco():
    """Cria o banco de dados e a tabela de clientes caso ainda não existam."""
    conexao = sqlite3.connect("cadastro_clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()


# --- FUNCIONALIDADES ---
def salvar_cliente():
    """Valida os campos e salva os dados do cliente no banco SQLite."""
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # 4) Validação de campos vazios
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Campos Obrigatórios",
            "Por favor, preencha todos os campos (Nome, E-mail e Telefone).",
        )
        return

    try:
        conexao = sqlite3.connect("cadastro_clientes.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone),
        )
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()
    except Exception as erro:
        messagebox.showerror(
            "Erro no Banco de Dados", f"Não foi possível salvar os dados: {erro}"
        )


def limpar_formulario():
    """Limpa todos os campos de entrada do formulário."""
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_nome.focus()  # Retorna o cursor para o primeiro campo


# --- 1) INTERFACE GRÁFICA (TKINTER) ---
inicializar_banco()

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("380x250")
janela.resizable(False, False)

# Frame principal para organização
frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack(fill=tk.BOTH, expand=True)

# Campo Nome
tk.Label(frame_principal, text="Nome:", font=("Arial", 10, "bold")).grid(
    row=0, column=0, sticky="w", pady=5
)
entrada_nome = tk.Entry(frame_principal, width=32, font=("Arial", 10))
entrada_nome.grid(row=0, column=1, pady=5)

# Campo E-mail
tk.Label(frame_principal, text="E-mail:", font=("Arial", 10, "bold")).grid(
    row=1, column=0, sticky="w", pady=5
)
entrada_email = tk.Entry(frame_principal, width=32, font=("Arial", 10))
entrada_email.grid(row=1, column=1, pady=5)

# Campo Telefone
tk.Label(frame_principal, text="Telefone:", font=("Arial", 10, "bold")).grid(
    row=2, column=0, sticky="w", pady=5
)
entrada_telefone = tk.Entry(frame_principal, width=32, font=("Arial", 10))
entrada_telefone.grid(row=2, column=1, pady=5)

# Frame para os botões
frame_botoes = tk.Frame(frame_principal)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=20)

# Botão Salvar
btn_salvar = tk.Button(
    frame_botoes,
    text="Salvar Cliente",
    command=salvar_cliente,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    width=14,
)
btn_salvar.pack(side=tk.LEFT, padx=10)

# Botão Limpar
btn_limpar = tk.Button(
    frame_botoes,
    text="Limpar Formulário",
    command=limpar_formulario,
    bg="#f44336",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15,
)
btn_limpar.pack(side=tk.LEFT, padx=10)

# Inicia o loop da aplicação
janela.mainloop()
