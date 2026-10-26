import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

VERSAO = "3.2.2"


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()
janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("480x460")
janela.resizable(False, False)


# ============================================================
# CLASSE CLIENTE
# ============================================================

class Cliente:

    def __init__(self, nome, telefone, email, endereco, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"

    def iniciais(self):
        partes = self.nome.split()

        return "".join(
            parte[0].upper()
            for parte in partes
            if parte
        )


# ============================================================
# CLASSE GERENCIADOR DE CLIENTES
# ============================================================

class GerenciadorClientes:

    def __init__(self, caminho_banco="techbairro.db"):
        self.caminho_banco = caminho_banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):
        conexao = self.conectar()

        conexao.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            endereco TEXT
        )
        """)

        conexao.commit()
        conexao.close()

    # ========================================================
    # CREATE
    # ========================================================

    def adicionar(self, cliente):

        conexao = self.conectar()

        cursor = conexao.execute(
            "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
            (
                cliente.nome,
                cliente.telefone,
                cliente.email,
                cliente.endereco
            )
        )

        conexao.commit()

        cliente.id = cursor.lastrowid

        conexao.close()

    # ========================================================
    # READ
    # ========================================================

    def listar(self):

        conexao = self.conectar()

        # CORRIGIDO (BUG 4)
        linhas = conexao.execute(
            "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY nome"
        ).fetchall()

        conexao.close()

        return [
            Cliente(
                nome,
                telefone,
                email,
                endereco,
                id
            )
            for (id, nome, telefone, email, endereco) in linhas
        ]

    # ========================================================
    # UPDATE
    # ========================================================

    def atualizar(self, id_cliente, novo_cliente):

        conexao = self.conectar()

        cursor = conexao.execute(
            "UPDATE clientes SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id = ?",
            (
                novo_cliente.nome,
                novo_cliente.telefone,
                novo_cliente.email,
                novo_cliente.endereco,
                id_cliente
            )
        )

        # CORRIGIDO (BUG 6)
        conexao.commit()

        conexao.close()

        return cursor.rowcount == 1

    # ========================================================
    # DELETE
    # ========================================================

    def remover(self, id_cliente):

        conexao = self.conectar()

        cursor = conexao.execute(
            "DELETE FROM clientes WHERE id = ?",
            (id_cliente,)
        )

        conexao.commit()
        conexao.close()

        return cursor.rowcount == 1

    # ========================================================
    # TOTAL
    # ========================================================

    def total(self):

        conexao = self.conectar()

        quantidade = conexao.execute(
            "SELECT COUNT(*) FROM clientes"
        ).fetchone()[0]

        conexao.close()

        return quantidade


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# NOVO NA AULA 16: caminho completo do banco.
#
# __file__ é o caminho deste arquivo .py.
# Assim o techbairro.db fica SEMPRE na mesma pasta do projeto,
# não importa de onde o VS Code rodar o programa.
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
# Mostra no terminal qual banco está em uso
print(f"Banco em uso: {CAMINHO_BANCO}")
# Cria o objeto responsável por gerenciar os clientes
gerenciador = GerenciadorClientes(CAMINHO_BANCO)

id_em_edicao = None


# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================

cabecalho = tk.Frame(
    janela,
    bg="#2c3e50"
)

cabecalho.pack(
    side="top",
    fill="x"
)

tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12
).pack()


# ============================================================
# FORMULÁRIO
# ============================================================

form = tk.Frame(janela)

form.pack(
    pady=20
)

campos = [
    "Nome",
    "Telefone",
    "E-mail",
    "Endereço"
]

entradas = {}

for i, campo in enumerate(campos):

    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )

    entrada = tk.Entry(
        form,
        width=30
    )

    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )

    entradas[campo] = entrada


# ============================================================
# STATUS
# ============================================================

status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left"
)

status.pack(
    pady=(0, 5)
)


contador = tk.Label(
    janela,
    text=f"Clientes cadastrados: {gerenciador.total()}"
)

contador.pack()


# ============================================================
# LIMPAR CAMPOS
# ============================================================

def limpar_campos():

    global id_em_edicao

    for entrada in entradas.values():

        entrada.delete(
            0,
            tk.END
        )

    id_em_edicao = None


# ============================================================
# VALIDAÇÃO DE E-MAIL
# ============================================================

def email_parece_valido(email):

    if "@" not in email:
        return False

    usuario, _, dominio = email.partition("@")

    # CORRIGIDO (BUG 2)
    if usuario == "":
        return False

    # CORRIGIDO (BUG 3)
    if "." not in dominio:
        return False

    return True


# ============================================================
# SALVAR
# ============================================================

def salvar():

    global id_em_edicao

    valores = {
        campo: entradas[campo].get().strip()
        for campo in campos
    }

    # CORRIGIDO (BUG 1)
    vazios = [
        campo
        for campo in campos
        if valores[campo] == ""
    ]

    if vazios:

        status.config(
            text=f"Preencha o(s) campo(s): {', '.join(vazios)}",
            fg="red"
        )

        return

    # ========================================================
    # VALIDAÇÃO DO TELEFONE
    # ========================================================

    if not valores["Telefone"].isdigit():

        status.config(
            text="Telefone inválido: use somente números.",
            fg="red"
        )

        return

    # ========================================================
    # VALIDAÇÃO DO E-MAIL
    # ========================================================

    if not email_parece_valido(
        valores["E-mail"]
    ):

        status.config(
            text="E-mail inválido: use o formato nome@dominio.com",
            fg="red"
        )

        return

    # ========================================================
    # CRIA CLIENTE
    # ========================================================

    cliente = Cliente(
        valores["Nome"],
        valores["Telefone"],
        valores["E-mail"],
        valores["Endereço"]
    )

    try:

        # ====================================================
        # CADASTRO
        # ====================================================

        if id_em_edicao is None:

            gerenciador.adicionar(cliente)

            status.config(
                text=f"Cliente '{cliente.nome}' salvo com sucesso!",
                fg="green"
            )

        # ====================================================
        # ATUALIZAÇÃO
        # ====================================================

        else:

            gerenciador.atualizar(
                id_em_edicao,
                cliente
            )

            status.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green"
            )

    except sqlite3.Error as erro:

        status.config(
            text=f"Erro ao salvar no banco: {erro}",
            fg="red"
        )

        return

    contador.config(
        text=f"Clientes cadastrados: {gerenciador.total()}"
    )

    limpar_campos()


# ============================================================
# CANCELAR
# ============================================================

def cancelar():

    limpar_campos()

    status.config(
        text="Formulário limpo",
        fg="gray"
    )


# ============================================================
# CONSULTA DE CLIENTES
# ============================================================

def abrir_consulta():

    consulta = tk.Toplevel(janela)

    consulta.title(
        "Consulta de Clientes"
    )

    consulta.geometry(
        "500x380"
    )

    consulta.resizable(
        False,
        False
    )

    # ========================================================
    # LISTBOX
    # ========================================================

    lista = tk.Listbox(
        consulta,
        width=65,
        height=12
    )

    lista.pack(
        padx=10,
        pady=10
    )

    # ========================================================
    # BARRA DE ROLAGEM
    # ========================================================

    scrollbar = tk.Scrollbar(
        consulta
    )

    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )

    lista.config(
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(
        command=lista.yview
    )

    # ========================================================
    # ATUALIZAR LISTA
    # ========================================================

    def atualizar_lista():

        lista.delete(
            0,
            tk.END
        )

        try:

            clientes_cadastrados = gerenciador.listar()

        except sqlite3.Error as erro:

            lista.insert(
                tk.END,
                f"Erro ao ler o banco: {erro}"
            )

            return

        if not clientes_cadastrados:

            lista.insert(
                tk.END,
                "Nenhum cliente cadastrado"
            )

            return

        for cliente in clientes_cadastrados:

            lista.insert(
                tk.END,
                cliente.resumo()
            )

    # ========================================================
    # EDITAR CLIENTE
    # ========================================================

    def editar_cliente():

        global id_em_edicao

        selecionado = lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente antes de editar."
            )

            return

        indice = selecionado[0]

        cliente = gerenciador.listar()[
            indice
        ]

        id_em_edicao = cliente.id

        # ====================================================
        # COLOCA OS DADOS NO FORMULÁRIO
        # ====================================================

        entradas["Nome"].delete(
            0,
            tk.END
        )

        entradas["Nome"].insert(
            0,
            cliente.nome
        )

        entradas["Telefone"].delete(
            0,
            tk.END
        )

        entradas["Telefone"].insert(
            0,
            cliente.telefone
        )

        entradas["E-mail"].delete(
            0,
            tk.END
        )

        entradas["E-mail"].insert(
            0,
            cliente.email
        )

        entradas["Endereço"].delete(
            0,
            tk.END
        )

        entradas["Endereço"].insert(
            0,
            cliente.endereco
        )

        status.config(
            text=f"Editando cliente: {cliente.nome}",
            fg="blue"
        )

        consulta.destroy()

    # ========================================================
    # EXCLUIR CLIENTE
    # ========================================================

    def excluir_cliente():

        selecionado = lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente antes de excluir."
            )

            return

        indice = selecionado[0]

        cliente = gerenciador.listar()[
            indice
        ]

        # CORRIGIDO (BUG 5)
        confirmado = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cadastro de "
            f"{cliente.nome}?\n\n"
            f"Essa ação não pode ser desfeita."
        )

        # CORRIGIDO (BUG 5)
        if not confirmado:
            return

        try:

            gerenciador.remover(
                cliente.id
            )

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro no banco",
                f"Não foi possível excluir o cliente.\n{erro}"
            )

            return

        atualizar_lista()

        contador.config(
            text=f"Clientes cadastrados: {gerenciador.total()}"
        )

        status.config(
            text=f"Cliente '{cliente.nome}' excluído com sucesso!",
            fg="green"
        )

    # ========================================================
    # BOTÕES DA CONSULTA
    # ========================================================

    botoes_consulta = tk.Frame(
        consulta
    )

    botoes_consulta.pack(
        pady=10
    )

    tk.Button(
        botoes_consulta,
        text="Editar selecionado",
        width=18,
        command=editar_cliente
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    tk.Button(
        botoes_consulta,
        text="Excluir selecionado",
        width=18,
        command=excluir_cliente
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    atualizar_lista()


# ============================================================
# BOTÕES DA JANELA PRINCIPAL
# ============================================================

botoes = tk.Frame(
    janela
)

botoes.pack(
    pady=10
)


# Botão Salvar

tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(
    row=0,
    column=0,
    padx=5
)


# Botão Cancelar

tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)


# Botão Consultar

tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# VERSÃO
# ============================================================

tk.Label(
    janela,
    text="v3.2",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)


# ============================================================
# INICIALIZAÇÃO
# ============================================================

janela.mainloop()