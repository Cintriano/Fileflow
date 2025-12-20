import sys
from cx_Freeze import setup, Executable

caminho_setup = r".\src\interface\janela.py"

build_exe_options = {
    "packages": [
        "os", "tkinter", "numpy", "matplotlib", "pandas", "scipy",
        "seaborn", "sklearn", "joblib", "mutagen"
    ],
    "include_files": [],
}

# Base para interface gráfica
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Configuração do setup
setup(
    name="Diem",
    version="0.3",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable(caminho_setup, base=base)],
)

