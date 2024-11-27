import tkinter as tk
from tkinter import ttk
from temas import ver_todos_temas  # Importa a função ver_todos_temas para obter a lista de temas
from interface.iniciarjogo import iniciar_jogo  # Importa o módulo iniciarjogo para abrir a tela de jogo
import interface.jogar  # Importa a tela inicial para o botão "Voltar ao Início"
import musica

def iniciar_temas(usuario):
    # Cria a janela principal para a tela de temas
    janela_temas = tk.Tk()
    janela_temas.title("Jogo Da Forca")
    janela_temas.geometry("900x600")
    janela_temas.configure(bg="#3181BE")

    # Exibe o título
    label_usuario = ttk.Label(janela_temas, text="Escolha um tema para Jogar", font=("Arial", 18, "bold"), foreground="white", background="#3181BE")
    label_usuario.pack(pady=10)

    # Frame para centralizar a área de rolagem
    frame_central = tk.Frame(janela_temas, bg="#3181BE")
    frame_central.pack(pady=10, expand=True)

    # Configuração da área de rolagem
    canvas = tk.Canvas(frame_central, bg="#3181BE", width=220, height=400, highlightthickness=0)  # Define largura limitada para o canvas
    scrollbar = tk.Scrollbar(frame_central, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#3181BE")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Posicionamento do canvas e scrollbar
    canvas.pack(side="left", fill="y", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Obtem a lista de temas
    temas = ver_todos_temas()

    # Cria um botão para cada tema
    for tema_id, tema_nome in temas:
        btn_tema = tk.Button(scrollable_frame, text=tema_nome, font=("Arial", 12), width=20, height=2,
                             bg="#087631", fg="white", activebackground="#065A28", activeforeground="white",
                             command=lambda t={'id': tema_id, 'nome': tema_nome}: abrir_jogo(janela_temas, usuario, t))
        btn_tema.pack(pady=5)

    # Botão Voltar ao Início
    btn_voltar_inicio = tk.Button(janela_temas, text="Voltar ao Início", font=("Arial", 14),
                                  width=15, height=2, bg="#FFCC00", fg="black", activebackground="#FFD700", 
                                  activeforeground="black", command=lambda: voltar_inicio(janela_temas, usuario))
    btn_voltar_inicio.pack(pady=20)

    janela_temas.mainloop()

def abrir_jogo(janela_temas, usuario, tema):
    musica.play_botao()
    # Fecha a janela de temas e abre a tela iniciarjogo com usuario e tema
    janela_temas.destroy()  # Fecha a janela atual
    iniciar_jogo(usuario, tema)  # Chama a função iniciar_jogo passando usuario e tema

def voltar_inicio(janela_temas, usuario):
    musica.play_botao()
    # Fecha a tela de temas e volta para a tela inicial
    janela_temas.destroy()  # Fecha a janela de temas
    root = tk.Tk()  # Cria uma nova instância de janela principal
    interface.jogar.Janela_Jogo(root, usuario)  # Abre a tela inicial passando o usuário
