import pygame
import tkinter as tk
from tkinter import ttk
import time
import sys
import os

# Variáveis de volume
volumeMusica = 0.5
volumeTock = 0.5

# Inicialize o mixer do pygame
pygame.mixer.init()

# Função para obter o caminho correto dos arquivos de som
def get_resource_path(filename):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, "sons", filename)

# Função para tocar a música de fundo em loop
def play_musica():
    pygame.mixer.music.set_volume(volumeMusica)
    pygame.mixer.music.load(get_resource_path("musica.wav"))
    pygame.mixer.music.play(-1)  # Toca em loop

# Função para tocar o som do botão separadamente
def play_botao():
    click_sound = pygame.mixer.Sound(get_resource_path("click.wav"))
    click_sound.set_volume(volumeTock)
    click_sound.play()

def game_over():
    pygame.mixer.music.set_volume(volumeTock)
    pygame.mixer.music.load(get_resource_path("gameover.wav"))
    pygame.mixer.music.play(1)
    time.sleep(4)
    play_musica()

def vitoria():
    pygame.mixer.music.set_volume(volumeTock)
    pygame.mixer.music.load(get_resource_path("vitoria.wav"))
    pygame.mixer.music.play(2)
    time.sleep(3)
    play_musica()

# Função para atualizar o volume da música de fundo
def atualizar_volume_musica(val):
    global volumeMusica
    volumeMusica = float(val)
    pygame.mixer.music.set_volume(volumeMusica)

# Função para atualizar o volume do som do botão
def atualizar_volume_tock(val):
    global volumeTock
    click_sound = pygame.mixer.Sound(get_resource_path("click.wav"))
    click_sound.set_volume(volumeTock)
    volumeTock = float(val)

def interface():
    # Configuração da interface Tkinter
    root = tk.Tk()
    root.title("Controle de Volume")
    root.geometry("900x600")
    root.configure(bg="#3181BE")

    # Logo ou título
    label_titulo = ttk.Label(root, text="Controle de Volume", font=("Arial", 18), foreground="white", background="#3181BE")
    label_titulo.pack(pady=20)

    # Botões para iniciar a música de fundo e o som do botão
    button_frame = tk.Frame(root, bg="#3181BE")
    button_frame.pack(pady=10)

    # Botão para tocar música de fundo
    btn_play_musica = create_styled_button(button_frame, "Tocar Música", play_musica, bg="#087631", active_bg="#065A28", fg="white")
    btn_play_musica.pack(side="left", padx=10)

    # Botão para testar o som do botão
    btn_play_botao = create_styled_button(button_frame, "Som do Botão", play_botao, bg="#087631", active_bg="#065A28", fg="white")
    btn_play_botao.pack(side="left", padx=10)

    # Slider para controlar o volume da música de fundo
    slider_musica = tk.Scale(root, from_=0, to=1, resolution=0.1, orient="horizontal",
                             label="Volume Música de Fundo", command=atualizar_volume_musica,
                             font=("Arial", 12), bg="#3181BE", fg="white")
    slider_musica.set(volumeMusica)  # Define o valor inicial
    slider_musica.pack(pady=10, fill="x", padx=50)

    # Slider para controlar o volume do som do botão
    slider_tock = tk.Scale(root, from_=0, to=1, resolution=0.1, orient="horizontal",
                           label="Volume Som do Botão", command=atualizar_volume_tock,
                           font=("Arial", 12), bg="#3181BE", fg="white")
    slider_tock.set(volumeTock)  # Define o valor inicial
    slider_tock.pack(pady=10, fill="x", padx=50)

    # Botão Fechar na parte inferior
    btn_fechar = create_styled_button(root, "Fechar", root.destroy, bg="#ff0014", active_bg="#ba0a18", fg="white")
    btn_fechar.pack(pady=20, side="bottom")

    root.mainloop()

def create_styled_button(parent, text, command, bg="#FFCC00", active_bg="#FFD700", fg="black"):
    button = tk.Button(parent, text=text, font=("Arial", 14), command=command, 
                       width=15, height=2, bg=bg, fg=fg, activebackground=active_bg, 
                       activeforeground="black", relief="flat", bd=1)
    button.bind("<Enter>", lambda e: button.config(bg=active_bg))
    button.bind("<Leave>", lambda e: button.config(bg=bg))
    button.config(highlightthickness=0, relief="solid", borderwidth=2)
    button.pack_propagate(False)
    return button
