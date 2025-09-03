import sys
from cx_Freeze import setup, Executable

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
    name="FileFlow",
    version="0.1",
    description="Minha 1° Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("interface.py", base=base)],
)

