from conexao import get_connection

def get_ranking_usuarios():
    """Retorna um ranking de usuários com base no número de palavras resolvidas.

    Returns:
        list: Uma lista de tuplas contendo o ID do usuário, nome do usuário, e o número de palavras resolvidas, ordenada do usuário com mais palavras para o com menos.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta para contar as palavras resolvidas por cada usuário
    query = """
    SELECT u.id_usuario, u.nome_usuario, COUNT(pr.id_palavra_fk) AS total_palavras_resolvidas
    FROM usuarios u
    LEFT JOIN palavras_resolvidas pr ON u.id_usuario = pr.id_usuario_fk
    GROUP BY u.id_usuario, u.nome_usuario
    ORDER BY total_palavras_resolvidas DESC
    """
    cursor.execute(query)
    ranking_usuarios = cursor.fetchall()

    conn.close()
    return ranking_usuarios
