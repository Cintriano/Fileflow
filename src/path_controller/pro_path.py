from .uti_path import default_env_path, default_folder_tree

def reset_paths() -> str:
    try:
        default_env_path()
        default_folder_tree()
    except Exception as e:
        return f"Erro Função(reset_paths): {e}"
    return "Processo Finalizado"