import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from buscarPalavras import get_palavras_nao_resolvidas
from interface.menu import iniciar_tela_opcoes
from interface.tentarnovamente import iniciar_tela_novamente
import interface.jogar
import musica
import sys
import os
from PIL import Image, ImageTk

class JanelaJogoForca:
    def __init__(self, master, usuario, tema):
        self.master = master
        self.usuario = usuario
        self.tema = tema
        self.erro = 6  # Tentativas iniciais
        self.letra_digitada = set()  # Letras já tentadas
        
        # Configuração da janela
        self.master.title("Jogo da Forca")
        self.master.geometry("900x600")
        self.master.configure(bg="#3181BE")
        
        
        def get_resource_path(filename):
            base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
            return os.path.join(base_path, filename)  # Remova "interface" daqui



        # Lista de imagens para os estágios do jogo
        self.imagens = [
            get_resource_path("interface/imagem.png"),
            get_resource_path("interface/imagem0.png"),
            get_resource_path("interface/imagem1.png"),
            get_resource_path("interface/imagem2.png"),
            get_resource_path("interface/imagem3.png"),
            get_resource_path("interface/imagem4.png"),
            get_resource_path("interface/imagem5.png")
        ]
        
        # Carregar a imagem inicial
        self.indice_imagem = 0
        self.image = ImageTk.PhotoImage(Image.open(self.imagens[self.indice_imagem]))
        self.label_imagem = tk.Label(self.master, image=self.image, bg="#3181BE")
        self.label_imagem.pack(pady=10)

        # Obtém a lista de palavras com base no usuário e tema
        self.palavras = get_palavras_nao_resolvidas(usuario[0], tema['id'])
        
        # Seleciona uma palavra aleatória da lista
        if self.palavras:
            self.pala = random.choice(self.palavras)
        else:
            messagebox.showerror("Erro", "Você já fez todas as palavras referentes a esse tema 😀")
            self.master.destroy()
            root = tk.Tk()
            interface.jogar.Janela_Jogo(root, self.usuario)
            return
        self.palaEx = self.pala
        self.palavra_id = self.pala[0]
        self.pala = self.pala[1].upper()

        # Exibe a palavra com sublinhados
        self.label_palavra = tk.Label(self.master, text=self.mostrar_palavra(), font=("Arial", 24), bg="#3181BE", fg="white")
        self.label_palavra.pack(pady=20)

        # Entrada de letras
        self.entry_letra = tk.Entry(self.master, font=("Arial", 16))
        self.entry_letra.pack(pady=10)
        self.entry_letra.bind('<Return>', self.checar_tentativa)
        
        # Frame para botões de ação
        button_frame = tk.Frame(self.master, bg="#3181BE")
        button_frame.pack(pady=20)

        # Botão "Tentar"
        self.create_styled_button(button_frame, "Tentar", self.checar_tentativa).pack(side="left", padx=10)

        # Botão "Sair"
        # Botão "Sair"
        self.create_styled_button(button_frame, "Sair", self.voltar_inicio, bg="#FFCC00", active_bg="#FFD700", fg="white").pack(side="left", padx=10)


    def create_styled_button(self, parent, text, command, bg="#087631", active_bg="#065A28", fg="white"):
        button = tk.Button(parent, text=text, font=("Arial", 14), command=command,
                            width=15, height=2, bg=bg, fg=fg, activebackground=active_bg,
                            activeforeground="white", relief="flat", bd=1)
        button.bind("<Enter>", lambda e: button.config(bg=active_bg))
        button.bind("<Leave>", lambda e: button.config(bg=bg))
        button.pack_propagate(False)
        return button


    def mostrar_palavra(self):
        return ' '.join([letra if letra in self.letra_digitada else '_ ' for letra in self.pala])

    def checar_tentativa(self, event=None):
        tentativa = self.entry_letra.get().upper()
        self.entry_letra.delete(0, tk.END)

        if len(tentativa.strip()) > 1:
            if tentativa == self.pala:
                musica.vitoria()
                messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era '{self.pala}'")
                self.abrir_menu()
            else:
                self.atualizar_erro(f"A palavra não é '{tentativa}'.")
            return

        if tentativa in self.letra_digitada:
            messagebox.showwarning("Letra repetida", "Você já tentou essa letra.")
            return

        self.letra_digitada.add(tentativa)

        if tentativa in self.pala:
            self.label_palavra.config(text=self.mostrar_palavra())
            if all(letra in self.letra_digitada for letra in self.pala):
                musica.vitoria()
                messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era '{self.pala}'")
                self.abrir_menu()
        else:
            self.atualizar_erro(f"A letra '{tentativa}' não existe na palavra.")

    def atualizar_erro(self, mensagem):
        self.erro -= 1
        messagebox.showinfo("Erro!", mensagem)

        # Atualiza a imagem do jogo
        if self.erro >= 0 and self.erro < len(self.imagens):
            self.indice_imagem = 6 - self.erro
            nova_imagem = ImageTk.PhotoImage(Image.open(self.imagens[self.indice_imagem]))
            self.label_imagem.config(image=nova_imagem)
            self.label_imagem.image = nova_imagem

        if self.erro == 0:
            self.indice_imagem = 5
            nova_imagem = ImageTk.PhotoImage(Image.open(self.imagens[self.indice_imagem]))
            musica.game_over()
            messagebox.showinfo("Game Over", "Você perdeu! Tente Novamente.")
            self.game_over()

    def abrir_menu(self):
        musica.play_botao()
        self.palavras.remove(self.palaEx)
        self.master.destroy()
        iniciar_tela_opcoes(self.usuario, self.tema, (self.palavra_id, self.pala))
        
    def game_over(self):
        musica.play_botao()
        self.master.destroy()
        iniciar_tela_novamente(self.usuario, self.tema, (self.palavra_id, self.pala))

    def voltar_inicio(self):
        musica.play_botao()
        self.master.destroy()
        root = tk.Tk()
        interface.jogar.Janela_Jogo(root, self.usuario)

def iniciar_jogo(usuario, tema):
    root = tk.Tk()
    JanelaJogoForca(root, usuario, tema)
    root.mainloop()
