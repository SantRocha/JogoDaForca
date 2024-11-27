# cadastroUsuario.py

from conexao import get_connection

def cadastrar_usuario(nome, senha):
    """Cadastra um novo usuário no banco de dados."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nome_usuario = ?", (nome,))
    if cursor.fetchone():
        conn.close()
        return "Erro: O nome de usuário já está cadastrado."

    cursor.execute("INSERT INTO usuarios (nome_usuario, senha_usuario) VALUES (?, ?)", (nome, senha))
    conn.commit()
    conn.close()

    return "Usuário cadastrado com sucesso."
