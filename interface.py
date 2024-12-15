import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from main import *

# Criar a janela principal
janela = tk.Tk()
janela.title("FileFlow")
janela.geometry("501x400")  # Define o tamanho da janela

# Adicionar o titulo da janela
label = tk.Label(janela, text="File Flow", font=("Arial", 20))
label.place(x=190, y=5)

barra_aba = ttk.Notebook(janela)
barra_aba.pack(expand=True, fill="both")  # Expande para ocupar o espaço disponível

# Aba ranema
rename = ttk.Frame(barra_aba)
barra_aba.add(rename, text="Rename")  # Adiciona a aba

label = ttk.Label(rename, text="Escolha diretório de imagens:")
label.pack(pady=10)

# Combobox para escolher opções
opcoes = ["Padrão", "Externo(cartão SD)"]  # Lista de opções
combobox = ttk.Combobox(rename, values=opcoes, state="readonly")
combobox.pack(pady=5)
combobox.current(0)  # Define a primeira opção como selecionada

#botão executar
btn1 = ttk.Button(rename, text="Executar")
btn1.pack(pady=10)

# Aba de conversão
conversor = ttk.Frame(barra_aba)
barra_aba.add(conversor, text="Conversor")

label = ttk.Label(conversor, text="Escolha diretório de imagens:")
label.pack(pady=10)

# Combobox para escolher opções
opcoes = ["Padrão", "Externo(cartão SD)"]  # Lista de opções
combobox = ttk.Combobox(conversor, values=opcoes, state="readonly")
combobox.pack(pady=10)
combobox.current(0)  # Define a primeira opção como selecionada

label = ttk.Label(conversor, text="Tipo de conversão:")
label.pack(pady=5)

# Combobox para escolher opções
opcoes = ["CR2 -> jpg", "CR2 -> png", "jpg -> png", "png -> jpg"]  # Lista de opções
combobox = ttk.Combobox(conversor, values=opcoes, state="readonly")
combobox.pack(pady=15)
combobox.current(0)  # Define a primeira opção como selecionada

btn1 = ttk.Button(conversor, text="Executar")
btn1.pack(pady=5)

# Executar o loop principal da interface
janela.mainloop()
