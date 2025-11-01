import os
from tkinter import filedialog
from dotenv import load_dotenv

load_dotenv()

# --- Funções dos Botões e Switches ---

def botao_nova_pasta(label_diretorio, combobox):
    """Abre uma janela para o usuário selecionar um novo diretório.
    Se um diretório for selecionado, atualiza o texto do label e o valor da combobox."""
    diretorio = filedialog.askdirectory(title="Escolha um diretório")
    if diretorio:
        label_diretorio.configure(text=f"Diretório Selecionado")
        combobox.set(diretorio)

def verificar_log(switch_log):
    """Verifica o estado de um widget CTkSwitch e retorna um booleano (True se ligado, False se desligado)."""
    return switch_log.get() == 1
