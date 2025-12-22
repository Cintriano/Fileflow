import sys
import os
import customtkinter as ctk

# Adiciona o diretório 'src' ao sys.path
# Isso permite que os módulos sejam importados como se o script estivesse sendo executado da raiz do 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a função para criar a estrutura de abas
from componentes.comp_selec_pasta import create_tab_view
# Importa a função que configura a aba 'Rename'
from tab_rename import setup_rename_tab
from tab_opcoes import setup_opcoes_tab

# Definindo o tema da interface
ctk.set_appearance_mode("dark")

# --- Criação da Janela Principal ---
janela = ctk.CTk() # Criando a instancia da janela
janela.title("Diem") # Texto do head da janela
janela.geometry("600x500") # Tamanho da janela

# ============================= Aba rename =================================

# 1. Cria a estrutura de abas na janela principal
abas = create_tab_view(janela, ["Rename", "Opções"]) # Adicione mais nomes na lista para criar mais abas

# 2. Seleciona a aba específica que queremos configurar
aba_rename = abas.tab("Rename")
aba_opcoes = abas.tab("Opções")

# 3. Executa a função que popula a aba 'Rename' com seus componentes
setup_rename_tab(aba_rename)
setup_opcoes_tab(aba_opcoes)

# Se você tivesse outras abas, configuraria elas aqui. Por exemplo:
# aba_outra = abas.tab("OutraAba")
# setup_outra_aba(aba_outra)

# ============================= Aba relatorio =================================

# 2. Seleciona a aba específica que queremos configurar
#aba_relatorio = abas.tab("Relatório")

# 3. Executa a função que popula a aba 'Rename' com seus componentes

janela.mainloop() # Inicia a execução da interface gráfica
