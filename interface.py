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
combobox.pack(pady=10)
combobox.current(0)  # Define a primeira opção como selecionada

label = ttk.Label(rename, text="Tipo de Pocesso:")
label.pack(pady=5)

opcoes = ["Datação", "Remover Enchanced"]  # Lista de opções
combobox = ttk.Combobox(rename, values=opcoes, state="readonly")
combobox.pack(pady=15)
combobox.current(0)

btn1 = ttk.Button(rename, text="Executar")
btn1.pack(pady=5)


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


#ABA DE CONSULTA DO LOG
consulta = ttk.Frame(barra_aba)
barra_aba.add(consulta, text="Consulta")

label = ttk.Label(consulta, text="Nome do arquivo:")
label.pack(pady=10)

input_pesquisa = ttk.Entry(consulta, width=50)
input_pesquisa.pack(pady=10)

btn1 = ttk.Button(consulta, text="Executar")
btn1.pack(pady=5)

frame_resultado = ttk.LabelFrame(consulta, text="Resultado da Pesquisa")
frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)

text_resultado = tk.Text(frame_resultado, wrap="word", height=10, width=50)
text_resultado.pack(padx=5, pady=5)


# Executar o loop principal da interface
janela.mainloop()
