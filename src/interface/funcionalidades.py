import os
from tkinter import filedialog
from dotenv import load_dotenv
from main import main_datacao_auto, main_remover_enchanced, main_nomeacao_sem_data, main_datacao_manual

# Load environment variables from .env file
load_dotenv()
PATH_UPLOADS = os.getenv("PATH_UPLOADS")
PATH_PENDENTES = os.getenv("PATH_PENDENTES")
PATH_SD_EXTERNO = os.getenv("PATH_SD_EXTERNO")


def botao_nova_pasta(label_diretorio, combobox):
    """Abre uma janela para o usuário selecionar um novo diretório.
    Se um diretório for selecionado, atualiza o texto do label e o valor da combobox."""
    diretorio = filedialog.askdirectory(title="Escolha um diretório")
    if diretorio:
        label_diretorio.configure(text=f"Selecione a pasta*")
        combobox.set(diretorio)

def verificar_log(switch_log):
    """Verifica o estado de um widget CTkSwitch e retorna um booleano (True se ligado, false se desligado)."""
    return switch_log.get() == 1


def obter_caminho_selecionado(selector_pasta) -> str:
    """Obtém o caminho do diretório com base na seleção do combobox."""
    opcao = selector_pasta.get()
    if opcao == "Uploads":
        return PATH_UPLOADS
    elif opcao == "Pendentes":
        return PATH_PENDENTES
    elif opcao == "SD-Externo":
        return PATH_SD_EXTERNO
    return opcao  # Caso um caminho customizado seja selecionado

def executar_rename(selector_pasta, selector_metodo, switch_log, input_data, label_feedback):
    """Função principal chamada pelo botão 'Executar'.
    Ela lê os seletores, chama a função de lógica apropriada e exibe o ‘feedback’."""
    try:
        caminho = obter_caminho_selecionado(selector_pasta) # Passamos o seletor como argumento
        metodo = selector_metodo.get()
        log_ativo = verificar_log(switch_log) # Agora switch_log é um parâmetro

        # TODO: A lógica de log está atualmente dentro das funções 'main_*'.
        # O estado de 'log_ativo' precisaria ser passado para essas funções para controlá-la.

        resultado = ""
        if metodo == "Datação Automática":
            resultado = main_datacao_auto(caminho, log_ativo)
        elif metodo == "Datação Manual":
            data_fornecida = input_data.entry.get() # Acessa o widget de entrada dentro do frame
            if not data_fornecida:
                raise ValueError("A data manual não foi fornecida.")
            resultado = main_datacao_manual(caminho, data_fornecida, log_ativo)
        elif metodo == "Remover Enhanced":
            resultado = main_remover_enchanced(caminho)
        elif metodo == "Nomeação sem Data":
            resultado = main_nomeacao_sem_data(caminho)
        label_feedback.configure(text=resultado, text_color="green")
    except Exception as e:
        label_feedback.configure(text=f"Erro: {e}", text_color="red")
