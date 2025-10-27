import customtkinter as ctk
# Importa a função para criar a estrutura de abas
from componentes.comp_selec_pasta import create_tab_view
# Importa a função que configura a aba 'Rename'
from tab_rename import setup_rename_tab

# Definindo o tema da interface
ctk.set_appearance_mode("dark")

# --- Criação da Janela Principal ---
janela = ctk.CTk() # Criando a instancia da janela
janela.title("FileFlow") # Texto do head da janela
janela.geometry("600x500") # Tamanho da janela

# ============================= Configuração das Abas =================================

# 1. Cria a estrutura de abas na janela principal
abas = create_tab_view(janela, ["Rename"]) # Adicione mais nomes na lista para criar mais abas

# 2. Seleciona a aba específica que queremos configurar
aba_rename = abas.tab("Rename")

# 3. Executa a função que popula a aba 'Rename' com seus componentes
setup_rename_tab(aba_rename)

# Se você tivesse outras abas, configuraria elas aqui. Por exemplo:
# aba_outra = abas.tab("OutraAba")
# setup_outra_aba(aba_outra)

# ====================================================================================

janela.mainloop() # Inicia a execução da interface gráfica
