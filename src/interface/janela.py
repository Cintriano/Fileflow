import customtkinter as ctk
from componentes.comp_selec_pasta import *

#  python -m src.interface.janela

# Definindo o tema da interface
ctk.set_appearance_mode("dark")

janela = ctk.CTk() # Criando a instancia da janela
janela.title("Teste-01") # Texto do head da janela
janela.geometry("600x500") # Tamanho da janela

create_label("Selecione a pasta", janela)

janela.mainloop() # Execução da janela
