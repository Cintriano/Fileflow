import sys
import os
from cx_Freeze import setup, Executable

# 1. Configuração de Caminhos
# Garante que o cx_Freeze encontre a pasta 'interface' e a raiz 'src'
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./interface"))

# 2. Definição do Script Principal
script_principal = os.path.join("interface", "janela.py")

# 3. Pacotes (Bibliotecas que seu código usa)
# Nota: "Pillow" deve ser importado como "PIL"
packages = [
    "os",
    "sys",
    "ctypes",           # Importante para interfaces Windows
    "tkinter",
    "customtkinter",    # Sua interface gráfica
    "PIL",              # Pillow (Manipulação de imagens)
    "striprtf",         # Processamento de texto
    "tabulate",         # Tabelas
    "darkdetect"        # Dependência do CustomTkinter
]

# 4. Inclusão dos SEUS arquivos (Módulos do Projeto)
# Isso corrige o erro de "Missing modules" que você teve antes
includes = [
    "componentes",   # Sua pasta de componentes
    "tab_opcoes",    # O arquivo tab_opcoes.py
    "tab_rename"     # O arquivo tab_rename.py
]

# 5. Configurações de Build
build_exe_options = {
    "packages": packages,
    "includes": includes,
    "include_files": [], # Se tiver ícones ou imagens soltas, coloque aqui: ("origem", "destino")
}

# 6. Configuração da Janela (Console vs GUI)
# Deixei como 'None' para aparecer o console e vermos erros se existirem.
# Quando estiver tudo perfeito, mude para: base = "Win32GUI"
base = None
if sys.platform == "win32":
    # base = "Win32GUI" # <--- Descomente esta linha APENAS quando finalizar
    pass

setup(
    name="Diem",
    version="0.4", # Atualizei a versão
    description="Automatizador Diem",
    options={"build_exe": build_exe_options},
    executables=[Executable(script_principal, base=base, target_name="Diem.exe")],
)