import os
import json

path = ".\\Links\\paths_master.json"


def busca_path(variavel_de_ambiente: str) -> str:
    """Busca as variáveis e retorna o caminho especificado num arquivo JSON."""
    if not os.path.exists(path):
        path_padrao()
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            paths = json.load(file)
            
        if variavel_de_ambiente in paths:
            return paths[variavel_de_ambiente]
        return f"Variavel de ambiente {variavel_de_ambiente} não encontrada"
    except json.JSONDecodeError:
        # Se o JSON for inválido, recria com os padrões
        path_padrao()
        return busca_path(variavel_de_ambiente)
    except Exception as e:
        return f"Erro Função(busca_path): {e}"


def path_padrao():
    """Cria o arquivo JSON com os caminhos padrões."""
    default_paths = {
        "DEFAULT_PATH": "G:\\Meu Drive\\03_Publicacao\\02_Upload",
        "SD_PATH": "D:\\DCIM\\100CANON",
        "LOG_PATH": "G:\\Meu Drive\\03_Publicacao\\Teste\\Log",
        "IMG_PATH": "C:\\Users\\CintraMan\\Documents\\Projetos\\FileFlow\\Links\\Titulo.png"
    }
    
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default_paths, f, indent=4)
    except Exception as e:
        return f"Erro Função(path_padrao): {e}"


def add_path(variavel_ambiente: str, caminho: str) -> str:
    """Adiciona ou atualiza um caminho no arquivo JSON."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            paths = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        paths = {}

    paths[variavel_ambiente] = caminho

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(paths, f, indent=4)
    except Exception as e:
        return f"Erro Função(add_path): {e}"


def verify_paths() -> bool:
    """Verifica se todos os caminhos no arquivo JSON existem e retorna uma lista dos que não existem."""
    invalid_paths = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            paths = json.load(file)
        
        for key, value in paths.items():
            if not os.path.exists(value):
                invalid_paths.append(key)
                
    except (FileNotFoundError, json.JSONDecodeError):
        return f"Arqquivo nao encontrado: {[key]}"
    except Exception as e:
        return f"Erro Função(verify_paths): {e}"
        
    return invalid_paths

# Exemplo de uso:
# caminhos_invalidos = verify_paths()
# if caminhos_invalidos:
#     print("Caminhos inválidos encontrados:")
#     for key, value in caminhos_invalidos:
#         print(f"  - {key}: {value}")
# else:
#     print("Todos os caminhos são válidos.")

path_padrao()
print(busca_path("LOG_PATH"))