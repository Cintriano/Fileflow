import customtkinter as ctk
from componentes.comp_selec_pasta import *

#  python -m src.interface.janela

# Definindo o tema da interface
ctk.set_appearance_mode("dark")

janela = ctk.CTk() # Criando a instancia da janela
janela.title("FileFlow") # Texto do head da janela
janela.geometry("600x500") # Tamanho da janela

create_label(janela, "Selecione a pasta", 10)

# Lista de opções disponíveis
lista_opcoes = ["Uploads", "Pendentes", "SD-Externo"]

# Cria o seletor
selector_pasta = create_selector(
    janela,
    opcoes=lista_opcoes,
    default_value="Uploads",
    pady_size=10
)

create_label(janela, "Selecione o método", 10)

create_button(janela, "Executar", 0, command=lambda: executar(label_feedback))
label_feedback = create_label(janela,"", 10)

janela.mainloop() # Execução da janela
