import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from interface.jogar import Janela_Jogo
from cadastroUsuario import iniciar_tela_cadastro
import sys
import os
from login import verificar_login
import musica

class Janela_Inicial:
    def __init__(self, master):
        self.janela_inicial = master
        self.janela_inicial.title("Jogo Da Forca")
        self.janela_inicial.geometry("900x600")
        self.janela_inicial.configure(bg="#3181BE")
        musica.play_musica()

        # Logo
        self.logo = Image.open(self.resource_path("interface/nua.jpg"))
        self.logo = self.logo.resize((300, 300))
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = ttk.Label(self.janela_inicial, image=self.logo_tk)
        self.label_logo.pack(pady=10)

        self.label_usuario = ttk.Label(self.janela_inicial, text="Usuário:", font=("Arial", 14), foreground="white", background="#3181BE")
        self.label_usuario.pack()
        self.entry_usuario = ttk.Entry(self.janela_inicial, font=("Arial", 14))
        self.entry_usuario.pack(pady=5)

        self.label_senha = ttk.Label(self.janela_inicial, text="Senha:", font=("Arial", 14), foreground="white", background="#3181BE")
        self.label_senha.pack()
        self.entry_senha = ttk.Entry(self.janela_inicial, show="*", font=("Arial", 14))
        self.entry_senha.pack(pady=5)
        self.entry_senha.bind('<Return>', self.realizar_login)

        # Frame para os botões
        button_frame = tk.Frame(self.janela_inicial, bg="#3181BE")
        button_frame.pack(pady=20)

        # Botões estilizados
        self.create_styled_button(button_frame, "Fechar", self.fechar, bg="#ff0014", active_bg="#ba0a18").pack(side="left", padx=10)
        self.create_styled_button(button_frame, "Entrar", self.realizar_login, bg="#087631", active_bg="#065A28", fg="white").pack(side="left", padx=10)
        self.create_styled_button(button_frame, "Cadastrar", self.abrir_tela_cadastro).pack(side="left", padx=10)

        self.janela_inicial.mainloop()

    def create_styled_button(self, parent, text, command, bg="#FFCC00", active_bg="#FFD700", fg="black"):
        button = tk.Button(parent, text=text, font=("Arial", 14), command=command, 
                           width=15, height=2, bg=bg, fg=fg, activebackground=active_bg, 
                           activeforeground="black", relief="flat", bd=1)
        button.bind("<Enter>", lambda e: button.config(bg=active_bg))
        button.bind("<Leave>", lambda e: button.config(bg=bg))
        button.config(highlightthickness=0, relief="solid", borderwidth=2)
        button.pack_propagate(False)
        return button

    def resource_path(self, relative_path):
        """Obtenha o caminho absoluto do recurso, usando PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def fechar(self):
        musica.play_botao()
        self.janela_inicial.destroy()
    
    def realizar_login(self, event=None):
        musica.play_botao()
        email = self.entry_usuario.get()
        senha = self.entry_senha.get()
        usuario = verificar_login(email, senha)

        if len(usuario) > 1:
            self.janela_inicial.destroy()
            root = tk.Tk()
            Janela_Jogo(root, usuario)
            root.mainloop()
        else:
            messagebox.showerror("Erro", usuario[0])

    def abrir_tela_cadastro(self):
        musica.play_botao()
        """Fecha a janela atual e abre a tela de cadastro"""
        self.janela_inicial.destroy()
        iniciar_tela_cadastro()
