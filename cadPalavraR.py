from conexao import get_connection

def registrar_palavra_resolvida(id_usuario, id_palavra):
    """Insere uma palavra resolvida no banco de dados para um usuário específico.

    Args:
        id_usuario (int): O ID do usuário.
        id_palavra (int): O ID da palavra resolvida.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta para inserir a palavra resolvida
    query = """
    INSERT INTO palavras_resolvidas (id_usuario_fk, id_palavra_fk)
    VALUES (?, ?)
    """
    try:
        cursor.execute(query, (id_usuario, id_palavra))
        conn.commit()  # Confirma a inserção no banco de dados
    except Exception as e:
        conn.rollback()  # Reverte a transação em caso de erro
    finally:
        conn.close()  # Fecha a conexão com o banco de dados
