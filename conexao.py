import sqlite3
import os
from forca import criaBanco

def get_connection():
    try:
        diretorio = os.path.join(os.path.expanduser("~"), "JogoDaForca")
        caminho_banco = os.path.join(diretorio, 'forca.db')

        criaBanco()

        return sqlite3.connect(caminho_banco)
    except Exception as e:
        criaBanco()
        return sqlite3.connect(caminho_banco)
