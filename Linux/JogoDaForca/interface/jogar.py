import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from interface.temas import iniciar_temas
from interface.ranking import iniciar_tela_ranking
from interface.palavrasResolvidas import iniciar_tela_palavras_resolvidas
import musica
import interface.inicial
import sys
import os

class Janela_Jogo:
    def __init__(self, master, usuario):
        self.janela_jogo = master
        self.usuario = usuario
        self.janela_jogo.title("Jogo Da Forca")
        self.janela_jogo.geometry("900x600")
        self.janela_jogo.configure(bg="#3181BE")

        # Imagem de topo
        self.logo = Image.open(self.resource_path("interface/nua.jpg"))
        self.logo = self.logo.resize((300, 300), Image.ANTIALIAS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.janela_jogo, image=self.logo_tk, bg="#3181BE")
        self.label_logo.pack(pady=10)

        # Label para exibir o nome do usuário
        self.label_usuario = ttk.Label(self.janela_jogo, text=f"Bem Vindo {self.usuario[1].upper()}", font=("Arial", 18, "bold"), foreground="white", background="#3181BE")
        self.label_usuario.pack(pady=10)

        # Frame para os botões de ação principais
        button_frame = tk.Frame(self.janela_jogo, bg="#3181BE")
        button_frame.pack(pady=20)

        # Botões principais (Ranking, Jogar e Minhas Palavras)
        self.create_styled_button(button_frame, "Ranking", self.abrir_ranking).pack(side="left", padx=10)
        self.create_styled_button(button_frame, "Jogar", self.abrir_temas, bg="#087631", active_bg="#065A28", fg="white").pack(side="left", padx=10)
        self.create_styled_button(button_frame, "Minhas Palavras", self.abrir_palavras).pack(side="left", padx=10)

        # Botão Sair (Inferior esquerdo)
        self.btn_sair = self.create_styled_button(self.janela_jogo, "Sair", self.fechar, bg="#ff0014", active_bg="#ba0a18")
        self.btn_sair.config(width=10, height=1)  # Diminuindo o tamanho
        self.btn_sair.place(relx=0.05, rely=0.9, anchor="sw")  # Posiciona no canto inferior esquerdo

        # Botão Controle de Áudio (Inferior direito)
        self.btn_audio = self.create_styled_button(self.janela_jogo, "Controle de Áudio", self.abrir_controle_audio, bg="#FFCC00", active_bg="#FFD700")
        self.btn_audio.config(width=15, height=1)
        self.btn_audio.place(relx=0.95, rely=0.9, anchor="se")  # Posiciona no canto inferior direito

    def create_styled_button(self, parent, text, command, bg="#FFCC00", active_bg="#FFD700", fg="black"):
        button = tk.Button(parent, text=text, font=("Arial", 14), command=command,
                           width=15, height=2, bg=bg, fg=fg, activebackground=active_bg,
                           activeforeground="black", relief="flat", bd=1)
        button.bind("<Enter>", lambda e: button.config(bg=active_bg))  # Cor ao passar o mouse
        button.bind("<Leave>", lambda e: button.config(bg=bg))  # Cor ao sair do hover
        button.pack_propagate(False)
        return button

    def resource_path(self, relative_path):
        """Obtenha o caminho absoluto do recurso, usando PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def abrir_temas(self):
        musica.play_botao()
        self.janela_jogo.destroy()
        iniciar_temas(self.usuario)

    def abrir_ranking(self):
        musica.play_botao()
        self.janela_jogo.destroy()
        iniciar_tela_ranking(self.usuario)

    def abrir_palavras(self):
        musica.play_botao()
        self.janela_jogo.destroy()
        iniciar_tela_palavras_resolvidas(self.usuario)

    def abrir_controle_audio(self):
        musica.play_botao()
        musica.interface()  # Abre a interface de controle de áudio

    def fechar(self):
        musica.play_botao()
        self.janela_jogo.destroy()
        root = tk.Tk()
        interface.inicial.Janela_Inicial(root)

# Função para iniciar a tela de jogo
def iniciar_tela_jogo(usuario):
    root = tk.Tk()
    Janela_Jogo(root, usuario)
    root.mainloop()
