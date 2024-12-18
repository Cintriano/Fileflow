import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def escolher_diretorio(label_diretorio):
    diretorio = filedialog.askdirectory(title="Escolha um diretório")
    if diretorio:
        label_diretorio.config(text=f"Diretório Selecionado: {diretorio}")


# Criar a janela principal
janela = tk.Tk()
janela.title("FileFlow")
janela.geometry("500x400")  # Define o tamanho da janela

# Adicionar uma imagem no topo da janela
imagem_titulo = tk.PhotoImage(file=r"C:\Users\danil\OneDrive\Arquivos\Programas\FileFlow\Links\Titulo.png")
label_imagem = tk.Label(janela, image=imagem_titulo)
label_imagem.pack(pady=10)  # Adiciona padding vertical

# Adicionar uma barra de abas
barra_aba = ttk.Notebook(janela)
barra_aba.pack(expand=True, fill="both")  # Expande para ocupar o espaço disponível

# Função para criar um seletor de diretórios com botão (...)
def criar_seletor_diretorio(frame, texto):
    container = tk.Frame(frame)
    container.pack(pady=5)

    label_titulo = tk.Label(container, text=texto)
    label_titulo.pack()

    # Combobox
    opcoes = ["Padrão", "Externo (cartão SD)"]
    combobox = ttk.Combobox(container, values=opcoes, state="readonly")
    combobox.current(0)
    combobox.pack(side="left", padx=5)

    # Botão de escolha de diretório
    botao_diretorio = tk.Button(container, text="...", command=lambda: escolher_diretorio(label_diretorio))
    botao_diretorio.pack(side="left", padx=5)

    # Rótulo para mostrar diretório selecionado
    label_diretorio = tk.Label(frame, text="Nenhum diretório selecionado", wraplength=600, justify="center")
    label_diretorio.pack(pady=5)

    return container


# Aba Rename
rename = ttk.Frame(barra_aba)
barra_aba.add(rename, text="Rename")

# Adicionar seletor de diretório
criar_seletor_diretorio(rename, "Escolha diretório de imagens:")

# Combobox Tipo de Processo
label_processo = tk.Label(rename, text="Tipo de Processo:")
label_processo.pack(pady=5)

opcoes_processo = ["Datação", "Remover Enhanced"]
combobox_processo = ttk.Combobox(rename, values=opcoes_processo, state="readonly")
combobox_processo.current(0)
combobox_processo.pack(pady=5)

# Botão Executar
btn_executar_rename = tk.Button(rename, text="Executar")
btn_executar_rename.pack(pady=10)

# Aba Conversor
conversor = ttk.Frame(barra_aba)
barra_aba.add(conversor, text="Conversor")

# Adicionar seletor de diretório
criar_seletor_diretorio(conversor, "Escolha diretório de imagens:")

# Combobox Tipo de Conversão
label_conversao = tk.Label(conversor, text="Tipo de Conversão:")
label_conversao.pack(pady=5)

opcoes_conversao = ["CR2 -> jpg", "CR2 -> png", "jpg -> png", "png -> jpg"]
combobox_conversao = ttk.Combobox(conversor, values=opcoes_conversao, state="readonly")
combobox_conversao.current(0)
combobox_conversao.pack(pady=5)

# Botão Executar
btn_executar_conversor = tk.Button(conversor, text="Executar")
btn_executar_conversor.pack(pady=10)

# Aba Consulta
consulta = ttk.Frame(barra_aba)
barra_aba.add(consulta, text="Consulta")

label_consulta = tk.Label(consulta, text="Nome do arquivo:")
label_consulta.pack(pady=5)

input_pesquisa = ttk.Entry(consulta, width=50)
input_pesquisa.pack(pady=5)

btn_executar_consulta = tk.Button(consulta, text="Executar")
btn_executar_consulta.pack(pady=5)

# Frame de Resultado
frame_resultado = ttk.LabelFrame(consulta, text="Resultado da Pesquisa")
frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)

text_resultado = tk.Text(frame_resultado, wrap="word", height=10, width=50)
text_resultado.pack(padx=5, pady=5)

# Executar o loop principal da interface
janela.mainloop()
