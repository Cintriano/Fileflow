import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from main import main_datacao_auto, main_datacao_manual, main_conversao, main_busca_log, main_remover_enchanced


#Abre o seletor de diretório e atualiza o label e a combobox com o caminho escolhido.
def escolher_diretorio(label_diretorio, combobox):
    diretorio = filedialog.askdirectory(title="Escolha um diretório")
    if diretorio:
        label_diretorio.config(text=f"Diretório Selecionado")
        combobox.set(diretorio)


#Obtém o caminho do diretório com base na seleção do combobox.
def obter_caminho_diretorio(combobox):
    opcao = combobox.get()
    if opcao == "Padrão":
        return r"C:\Users\danil\OneDrive\Temporários\Upload"
    elif opcao == "Externo (cartão SD)":
        return r"D:\DCIM\100CANON"
    return opcao  # Caso o botão (...) seja usado


#Exibe ou oculta o campo de entrada de data dependendo da seleção do combobox.
def atualizar_interface_tipo_processo(event, frame_data_manual):
    if combobox_processo.get() == "Datação Manual":
        frame_data_manual.pack(pady=5)
    else:
        frame_data_manual.pack_forget()


#Exibe uma mensagem no final da página.
def exibir_mensagem(label_mensagem, texto):
    label_mensagem.config(text=texto)


# Criar a janela principal
janela = tk.Tk()
janela.title("FileFlow")
janela.geometry("500x500")  # Define o tamanho da janela

# Adicionar uma imagem no topo da janela
imagem_titulo = tk.PhotoImage(file=r"C:\Users\danil\OneDrive\Arquivos\Projetos\FileFlow\Links\Titulo.png")
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
    label_diretorio = tk.Label(container)
    label_diretorio.pack(side="left", padx=5)

    botao_diretorio = tk.Button(
        container, text="...", command=lambda: escolher_diretorio(label_diretorio, combobox)
    )
    botao_diretorio.pack(side="left", padx=5)

    return combobox, label_diretorio


# ----------------- Aba Rename ----------------- #
rename = ttk.Frame(barra_aba)
barra_aba.add(rename, text="Rename")

combobox_diretorio_rename, _ = criar_seletor_diretorio(rename, "Escolha diretório de imagens:")

# Combobox Tipo de Processo
label_processo = tk.Label(rename, text="Tipo de Processo:")
label_processo.pack(pady=5)

opcoes_processo = ["Datação automatica", "Datação Manual", "Remover Enhanced"]
combobox_processo = ttk.Combobox(rename, values=opcoes_processo, state="readonly")
combobox_processo.current(0)
combobox_processo.pack(pady=5)

# Frame para entrada de data manual (inicialmente oculto)
frame_data_manual = tk.Frame(rename)
label_data_manual = tk.Label(frame_data_manual, text="Digite a data (dd.mm.yyyy):")
label_data_manual.pack(side="left", padx=5)
entry_data_manual = ttk.Entry(frame_data_manual, width=15)
entry_data_manual.pack(side="left", padx=5)

# Adicionar evento para atualizar interface ao mudar o tipo de processo
combobox_processo.bind(
    "<<ComboboxSelected>>", lambda event: atualizar_interface_tipo_processo(event, frame_data_manual)
)

# Botão Executar
label_mensagem_rename = tk.Label(rename, text="", fg="green")
btn_executar_rename = tk.Button(
    rename,
    text="Executar",
    command=lambda: exibir_mensagem(
        label_mensagem_rename,
        main_datacao_manual(entry_data_manual.get(), obter_caminho_diretorio(combobox_diretorio_rename))
        if combobox_processo.get() == "Datação Manual"
        else (
            main_remover_enchanced(obter_caminho_diretorio(combobox_diretorio_rename))
            if combobox_processo.get() == "Remover Enhanced"
            else main_datacao_auto(obter_caminho_diretorio(combobox_diretorio_rename))
        ),
    ),
)
btn_executar_rename.pack(pady=10)
label_mensagem_rename.pack(pady=5)


# ----------------- Aba Conversor ----------------- #
conversor = ttk.Frame(barra_aba)
barra_aba.add(conversor, text="Conversor")

combobox_diretorio_conversor, _ = criar_seletor_diretorio(conversor, "Escolha diretório de imagens:")

# Combobox Tipo de Conversão
label_conversao = tk.Label(conversor, text="Tipo de Conversão:")
label_conversao.pack(pady=5)

opcoes_conversao = ["CR2 -> jpg", "CR2 -> png", "jpg -> png", "png -> jpg"]
combobox_conversao = ttk.Combobox(conversor, values=opcoes_conversao, state="readonly")
combobox_conversao.current(0)
combobox_conversao.pack(pady=5)

# Botão Executar
label_mensagem_conversor = tk.Label(conversor, text="", fg="green")
btn_executar_conversor = tk.Button(
    conversor,
    text="Executar",
    command=lambda: exibir_mensagem(
        label_mensagem_conversor,
        main_conversao(
            obter_caminho_diretorio(combobox_diretorio_conversor),
            str(opcoes_conversao.index(combobox_conversao.get()) + 1),
        ),
    ),
)
btn_executar_conversor.pack(pady=10)
label_mensagem_conversor.pack(pady=5)


# ----------------- Aba Consulta ----------------- #
consulta = ttk.Frame(barra_aba)
barra_aba.add(consulta, text="Consulta")

label_consulta = tk.Label(consulta, text="Nome do arquivo:")
label_consulta.pack(pady=5)

input_pesquisa = ttk.Entry(consulta, width=50)
input_pesquisa.pack(pady=5)

# Área de texto para exibir o output
text_output = tk.Text(consulta, height=10, wrap="word")
text_output.pack(pady=5)

# Botão Executar
btn_executar_consulta = tk.Button(
    consulta,
    text="Executar",
    command=lambda: text_output.insert(
        "end",  # Insere no topo do widget
        main_busca_log(r"C:\Users\danil\OneDrive\Temporários\Upload\Log", input_pesquisa.get()),
    ),
)
btn_executar_consulta.pack(pady=10)

# Executar o loop principal da interface
janela.mainloop()
