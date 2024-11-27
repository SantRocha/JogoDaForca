from conexao import get_connection

def get_palavras_nao_resolvidas(id_usuario, id_tema):
    """Retorna todas as palavras de um tema que o usuário ainda não resolveu.

    Args:
        id_usuario (int): O ID do usuário.
        id_tema (int): O ID do tema.

    Returns:
        list: Uma lista de tuplas contendo as palavras não resolvidas.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta para buscar palavras do tema que o usuário ainda não resolveu
    query = """
    SELECT p.id_palavra, p.nome_palavra
    FROM palavras p
    LEFT JOIN palavras_resolvidas pr ON p.id_palavra = pr.id_palavra_fk AND pr.id_usuario_fk = ?
    WHERE p.id_tema_fk = ? AND pr.id_usuario_fk IS NULL
    """
    cursor.execute(query, (id_usuario, id_tema))
    palavras_nao_resolvidas = cursor.fetchall()

    conn.close()
    return palavras_nao_resolvidas
