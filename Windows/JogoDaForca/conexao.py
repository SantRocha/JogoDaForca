import sqlite3
import os
from forca import criaBanco

def get_connection():
    try:
        # Define o diretório e o caminho do banco de dados
        diretorio = os.path.join("C:\\ProgramData", "JogoDaForca")
        caminho_banco = os.path.join(diretorio, 'forca.db')
        
        # Verifica se o banco de dados já existe, caso contrário, cria-o
        if not os.path.exists(caminho_banco):
            criaBanco()

        # Retorna a conexão com o banco de dados
        return sqlite3.connect(caminho_banco)
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise  # Rethrow the exception for further handling

'''pyinstaller --name=JogoDaForca --onefile --noconsole --add-data "interface;interface" --add-data "sons;sons" --hidden-import=PIL._tkinter_finder main.py
'''