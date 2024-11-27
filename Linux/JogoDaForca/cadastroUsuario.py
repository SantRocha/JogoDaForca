import tkinter as tk
from tkinter import messagebox
from cadastro import cadastrar_usuario
import interface.inicial
import musica

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo Da Forca")
        self.master.geometry("900x600")
        self.master.configure(bg="#3181BE")

        # Título
        self.label_titulo = tk.Label(self.master, text="Cadastro de Usuário", font=("Arial", 18, "bold"), bg="#3181BE", fg="white")
        self.label_titulo.pack(pady=10)

        # Campo Nome
        self.label_nome = tk.Label(self.master, text="Nome de Usuário:", font=("Arial", 14), bg="#3181BE", fg="white")
        self.label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(self.master, font=("Arial", 14))
        self.entry_nome.pack(pady=5)

        # Campo Senha
        self.label_senha = tk.Label(self.master, text="Senha:", font=("Arial", 14), bg="#3181BE", fg="white")
        self.label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.master, font=("Arial", 14), show="*")
        self.entry_senha.pack(pady=5)

        # Botões estilizados
        self.create_styled_button("Cadastrar", self.cadastrarUsuario).pack(pady=15)
        self.create_styled_button("Voltar", self.voltar_menu).pack(pady=5)

    def create_styled_button(self, text, command):
        # Criação de botão estilizado com efeito hover
        button = tk.Button(self.master, text=text, font=("Arial", 14), command=command,
                           width=20, height=2, bg="#FFCC00", fg="black", activebackground="#FFD700",
                           activeforeground="black", relief="flat", bd=1)
        button.bind("<Enter>", lambda e: button.config(bg="#FFD700"))  # Cor ao passar o mouse
        button.bind("<Leave>", lambda e: button.config(bg="#FFCC00"))  # Cor ao sair do hover
        button.config(highlightthickness=0, relief="solid", borderwidth=2)
        button.pack_propagate(False)
        return button

    def cadastrarUsuario(self):
        musica.play_botao()
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        # Validação de campos vazios
        if not nome or not senha:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
            return

        # Chama a função de cadastro e exibe o resultado
        resultado = cadastrar_usuario(nome, senha)
        messagebox.showinfo("Cadastro", resultado)

        # Limpa os campos e retorna à tela inicial se o cadastro for bem-sucedido
        if resultado == "Usuário cadastrado com sucesso.":
            self.master.destroy()
            root = tk.Tk()
            interface.inicial.Janela_Inicial(root)

    def voltar_menu(self):
        musica.play_botao()
        """Fecha a janela de cadastro e retorna ao menu inicial"""
        self.master.destroy()
        root = tk.Tk()
        interface.inicial.Janela_Inicial(root)

# Função para iniciar a tela de cadastro
def iniciar_tela_cadastro():
    root = tk.Tk()
    TelaCadastro(root)
    root.mainloop()
