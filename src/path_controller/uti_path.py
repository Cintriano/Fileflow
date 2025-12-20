import os
import json
from pathlib import Path

# Define o caminho para o arquivo JSON de configuração na raiz do projeto
JSON_FILE_PATH = Path(__file__).resolve().parents[2] / "paths_master.json"

def busca_path(variavel_de_ambiente: str) -> str:
    """Busca as variáveis e retorna o caminho especificado num arquivo JSON."""
    if not JSON_FILE_PATH.exists():
        default_env_path()
    
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            paths = json.load(file)
            
        if variavel_de_ambiente in paths:
            return paths[variavel_de_ambiente]
        return f"Variavel de ambiente {variavel_de_ambiente} não encontrada"
    except json.JSONDecodeError:
        # Se o JSON for inválido, recria com os padrões
        default_env_path()
        return busca_path(variavel_de_ambiente)
    except Exception as e:
        return f"Erro Função(busca_path): {e}"


def get_all_paths() -> dict:
    """Retorna um dicionário com todas as variáveis e caminhos configurados."""
    if not JSON_FILE_PATH.exists():
        default_env_path()
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {}


def default_env_path():
    """Cria o arquivo JSON com os caminhos padrões."""
    # Usa Path.home() para não chumbar o usuário 'CintraMan' no código
    user_downloads = Path.home() / "Downloads" / "Diem"
    default_paths = {
        "DEFAULT_PATH": str(user_downloads / "Padrao"),
        "PENDENTES_PATH": str(user_downloads / "Padrao"),
        "SD_PATH": "E:\\DCIM\\100CANON",
        "LOG_PATH": str(user_downloads / "LOG"),
        "IMG_PATH": str(Path("Links") / "Titulo.png")
    }
    
    try:
        # Garante que a pasta pai do JSON exista
        JSON_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(default_paths, f, indent=4)
        return "Arquivo JSON criado com sucesso"
    except Exception as e:
        return f"Erro Função(default_env_path): {e}"


def add_path(variavel_ambiente: str, caminho: str) -> str:
    """Adiciona ou atualiza um caminho no arquivo JSON."""
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            paths = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        paths = {}

    paths[variavel_ambiente] = caminho

    try:
        with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(paths, f, indent=4)
    except Exception as e:
        return f"Erro Função(add_path): {e}"


def verify_paths() -> bool:
    """Verifica se todos os caminhos no arquivo JSON existem e retorna uma lista dos que não existem."""
    invalid_paths = []
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            paths = json.load(file)
        
        # Define o diretório base como o local onde este script/json está
        base_dir = JSON_FILE_PATH.parent

        for key, value in paths.items():
            path_obj = Path(value)
            
            # Se o caminho for relativo (não absoluto), resolve a partir do diretório do script
            if not path_obj.is_absolute():
                path_obj = base_dir / path_obj
            
            if not path_obj.exists():
                invalid_paths.append(key)
                
    except (FileNotFoundError, json.JSONDecodeError):
        return f"Arqquivo nao encontrado: {[key]}"
    except Exception as e:
        return f"Erro Função(verify_paths): {e}"
    return invalid_paths


def default_folder_tree():
    """Cria a pasta 'Diem' e as subpastas 'LOG' e 'Padrão' na pasta de ‘Downloads’ do usuário."""
    try:
        # Obtém o caminho da pasta de Downloads do usuário
        downloads_path = Path.home() / "Downloads"
        
        path_diem = downloads_path / "Diem"
        path_log = path_diem / "Log"
        path_padrao_folder = path_diem / "Padrao"

        path_log.mkdir(parents=True, exist_ok=True)
        path_padrao_folder.mkdir(parents=True, exist_ok=True)

        return f"Estrutura de pastas criada com sucesso em: {path_diem}"
    except Exception as e:
        return f"Erro Função(default_folder_tree): {e}"


if __name__ == "__main__":
    pass
    #default_folder_tree()
    #print(verify_paths())
    #print(default_env_path())
    #print(busca_path("LOG_PATH"))
