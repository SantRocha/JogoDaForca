import tkinter as tk
from tkinter import ttk
from get_ranking_usuarios import get_ranking_usuarios  # Importa a função para obter o ranking
import interface.jogar
import musica

class TelaRanking:
    def __init__(self, master, usuario_atual):
        self.master = master
        self.usuario_atual = usuario_atual  # Tupla contendo o ID e nome do usuário atual

        self.master.title("Jogo Da Forca")
        self.master.geometry("900x600")
        self.master.configure(bg="#3181BE")

        # Título da tela
        label_titulo = tk.Label(self.master, text="Ranking de Usuários", font=("Arial", 18, "bold"), bg="#3181BE", fg="white")
        label_titulo.pack(pady=10)

        # Frame para a tabela
        frame_tabela = tk.Frame(self.master, bg="#3181BE")
        frame_tabela.pack(pady=10)

        self.tree = ttk.Treeview(frame_tabela, columns=("Colocação", "Nome", "Palavras Resolvidas"), show="headings", height=12)
        self.tree.heading("Colocação", text="Colocação")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Palavras Resolvidas", text="Palavras Resolvidas")

        self.tree.column("Colocação", width=150, anchor="center")
        self.tree.column("Nome", width=300, anchor="center")
        self.tree.column("Palavras Resolvidas", width=300, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#3181BE", foreground="white")
        style.configure("Treeview", rowheight=30, font=("Arial", 12))

        self.preencher_tabela()

        self.tree.pack()

        self.create_styled_button("Voltar ao Início", self.voltar_inicio).pack(pady=15)

    def preencher_tabela(self):
        ranking = get_ranking_usuarios()

        for index, usuario in enumerate(ranking, start=1):
            user_id, nome, qtd_palavras = usuario
            colocacao = index


            if user_id == self.usuario_atual[0]:
                self.tree.insert("", "end", values=(colocacao, nome, qtd_palavras), tags=("usuario_atual",))
            else:
                self.tree.insert("", "end", values=(colocacao, nome, qtd_palavras))

        self.tree.tag_configure("usuario_atual", background="#FFD700")

    def create_styled_button(self, text, command):
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
        self.master.destroy()  # Fecha a tela de ranking
        root = tk.Tk()  # Cria uma nova instância de janela principal
        interface.jogar.Janela_Jogo(root, self.usuario_atual)  # Retorna à tela de início

# Função para iniciar a Tela de Ranking
def iniciar_tela_ranking(usuario):
    root = tk.Tk()
    TelaRanking(root, usuario)
    root.mainloop()
