import os
import sys
# Adiciona a raiz do projeto ao sys.path para permitir imports de pastas superiores
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if project_root not in sys.path:
    sys.path.append(project_root)

from tkinter import filedialog
from main import main_datacao_auto, main_remover_enchanced, main_nomeacao_sem_data, main_datacao_manual
from path_controller.uti_path import busca_path
from path_controller.pro_path import reset_paths as reset_paths_core


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
        return busca_path("DEFAULT_PATH")
    elif opcao == "Pendentes":
        return busca_path("PENDENTES_PATH")
    elif opcao == "SD-Externo":
        return busca_path("SD_PATH")
    return opcao  # Caso um caminho customizado seja selecionado (e.g., de um filedialog)


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


def reset_paths_action(label_feedback):
    """Reseta os caminhos padrão e atualiza o feedback na interface."""
    try:
        reset_paths_core()
        label_feedback.configure(text="Caminhos resetados com sucesso!", text_color="green")
    except Exception as e:
        label_feedback.configure(text=f"Erro ao resetar caminhos: {e}", text_color="red")
