import tkinter as tk
from tkinter import ttk
from palavras_resolvidas import get_palavras_resolvidas  # Importa a função para obter as palavras resolvidas
import interface.jogar
import musica

class TelaPalavrasResolvidas:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario  # Tupla contendo o ID e nome do usuário

        self.master.title("Jogo Da Forca - Palavras Resolvidas")
        self.master.geometry("900x600")
        self.master.configure(bg="#3181BE")

        # Título da tela
        label_titulo = tk.Label(self.master, text="Palavras Resolvidas", font=("Arial", 18, "bold"), bg="#3181BE", fg="white")
        label_titulo.pack(pady=10)

        # Frame para a tabela
        frame_tabela = tk.Frame(self.master, bg="#3181BE")
        frame_tabela.pack(pady=10)

        # Configuração da tabela
        self.tree = ttk.Treeview(frame_tabela, columns=("Palavra", "Tema"), show="headings", height=10)
        self.tree.heading("Palavra", text="Palavra")
        self.tree.heading("Tema", text="Tema")

        # Ajusta largura e alinhamento das colunas
        self.tree.column("Palavra", width=400, anchor="center")
        self.tree.column("Tema", width=400, anchor="center")

        # Estilização adicional para a tabela
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#3181BE", foreground="white")
        style.configure("Treeview", rowheight=30, font=("Arial", 12))

        # Obtém as palavras resolvidas e preenche a tabela
        self.preencher_tabela()

        self.tree.pack()

        # Botão para voltar ao início
        self.create_styled_button("Voltar ao Início", self.voltar_inicio).pack(pady=15)

    def preencher_tabela(self):
        # Obtém todas as palavras resolvidas pelo usuário
        palavras_resolvidas = get_palavras_resolvidas(self.usuario[0])

        for palavra in palavras_resolvidas:
            palavra_id, nome_palavra, nome_tema = palavra
            self.tree.insert("", "end", values=(nome_palavra, nome_tema))

    def create_styled_button(self, text, command):
        # Criação de botão estilizado com efeito hover
        button = tk.Button(self.master, text=text, font=("Arial", 14), command=command,
                           width=20, height=2, bg="#FFCC00", fg="black", activebackground="#FFD700", activeforeground="black",
                           relief="flat", bd=1)
        button.bind("<Enter>", lambda e: button.config(bg="#FFD700"))
        button.bind("<Leave>", lambda e: button.config(bg="#FFCC00"))
        button.pack_propagate(False)
        return button

    def voltar_inicio(self):
        musica.play_botao()
        # Fecha a tela atual e volta para a tela inicial
        self.master.destroy()  # Fecha a tela de palavras resolvidas
        root = tk.Tk()  # Cria uma nova instância de janela principal
        interface.jogar.Janela_Jogo(root, self.usuario)  # Retorna à tela de início

# Função para iniciar a Tela de Palavras Resolvidas
def iniciar_tela_palavras_resolvidas(usuario):
    root = tk.Tk()
    TelaPalavrasResolvidas(root, usuario)
    root.mainloop()
