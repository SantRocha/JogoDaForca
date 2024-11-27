import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import interface.jogar
import interface.iniciarjogo
from cadPalavraR import registrar_palavra_resolvida
from interface.ranking import iniciar_tela_ranking
import sys
import os
import musica

class TelaOpcoes:
    def __init__(self, master, usuario, tema, palavra):
        self.master = master
        self.usuario = usuario
        self.tema = tema
        self.palavra = palavra

        self.master.title("Jogo Da Forca")
        self.master.geometry("900x600")
        self.master.configure(bg="#3181BE")
        
        # Imagem de topo
        self.logo = Image.open(self.resource_path("interface/nua.jpg"))  # Substitua pelo caminho da sua imagem
        self.logo = self.logo.resize((300, 300), Image.Resampling.LANCZOS)
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.master, image=self.logo_tk, bg="#3181BE")
        self.label_logo.pack(pady=10)

        # Mensagem de título
        label_titulo = tk.Label(self.master, text="O que você quer fazer a seguir?", font=("Arial", 18, "bold"), bg="#3181BE", fg="white")
        label_titulo.pack(pady=20)

        # Frame para os botões
        button_frame = tk.Frame(self.master, bg="#3181BE")
        button_frame.pack(pady=20)

        # Botão Voltar ao Início
        self.create_styled_button(button_frame, "Voltar ao Início", self.voltar_inicio, bg="#FFCC00", active_bg="#FFD700").pack(side="left", padx=10)

        # Botão Continuar
        self.create_styled_button(button_frame, "Continuar", self.continuar_jogo, bg="#087631", active_bg="#065A28").pack(side="left", padx=10)

        # Botão Ranking
        self.create_styled_button(button_frame, "Ranking", self.abrir_ranking, bg="#087631", active_bg="#065A28").pack(side="left", padx=10)

    def resource_path(self, relative_path):
        """Obtenha o caminho absoluto do recurso, usando PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    
    def create_styled_button(self, parent, text, command, bg, active_bg):
        # Criação de botão estilizado com efeito hover
        button = tk.Button(parent, text=text, font=("Arial", 14), command=command,
                           width=15, height=2, bg=bg, fg="black" if bg == "#FFCC00" else "white",
                           activebackground=active_bg, activeforeground="black" if bg == "#FFCC00" else "white",
                           relief="flat", bd=1)
        button.bind("<Enter>", lambda e: button.config(bg=active_bg))
        button.bind("<Leave>", lambda e: button.config(bg=bg))
        button.pack_propagate(False)
        return button

    def voltar_inicio(self):
        musica.play_botao()
        registrar_palavra_resolvida(self.usuario[0], self.palavra[0])
        self.master.destroy()
        root = tk.Tk()
        interface.jogar.Janela_Jogo(root, self.usuario)

    def continuar_jogo(self):
        musica.play_botao()
        registrar_palavra_resolvida(self.usuario[0], self.palavra[0])
        self.master.destroy()
        interface.iniciarjogo.iniciar_jogo(self.usuario, self.tema)

    def abrir_ranking(self):
        musica.play_botao()
        registrar_palavra_resolvida(self.usuario[0], self.palavra[0])
        self.master.destroy()
        iniciar_tela_ranking(self.usuario)

# Função para iniciar a Tela de Opções
def iniciar_tela_opcoes(usuario, tema, palavra):
    root = tk.Tk()
    TelaOpcoes(root, usuario, tema, palavra)
    root.mainloop()
