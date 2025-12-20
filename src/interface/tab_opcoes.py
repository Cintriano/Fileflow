import customtkinter as ctk
from tkinter import filedialog
from componentes.comp_selec_pasta import create_label, create_button, create_input
from funcionalidades import reset_paths_action
from path_controller.uti_path import get_all_paths, add_path

def setup_opcoes_tab(parent_tab):
    """Configura a aba 'Opções' com todos os seus componentes e layout."""

    # --- Configuração do Layout em Grade para a Aba ---
    parent_tab.grid_columnconfigure(0, weight=0) # Labels
    parent_tab.grid_columnconfigure(1, weight=1) # Inputs
    parent_tab.grid_columnconfigure(2, weight=0) # Botões de seleção

    # Dicionário para armazenar os widgets de entrada para salvamento posterior
    path_entries = {}

    # ============================= Campos de Caminhos Dinâmicos =================================
    paths = get_all_paths()
    row_idx = 0

    for key, value in paths.items():
        # Label com o nome da variável
        label = create_label(parent_tab, f"{key}:")
        label.grid(row=row_idx, column=0, padx=(20, 10), pady=5, sticky="w")

        # Input com o caminho atual
        entry = create_input(parent_tab, placeholder_text=value)
        entry.insert(0, value)
        entry.grid(row=row_idx, column=1, padx=(0, 10), pady=5, sticky="ew")
        
        # Armazena a referência do entry
        path_entries[key] = entry

        # Função para selecionar diretório e atualizar o entry
        def select_directory(e=entry):
            directory = filedialog.askdirectory()
            if directory:
                # Converte barras normais para invertidas (padrão Windows)
                directory = directory.replace("/", "\\")
                e.delete(0, 'end')
                e.insert(0, directory)

        # Botão para selecionar diretório
        btn_select = create_button(parent_tab, "Selecionar", command=select_directory)
        btn_select.configure(width=80)
        btn_select.grid(row=row_idx, column=2, padx=(0, 20), pady=5, sticky="e")

        row_idx += 1

    # ============================= Área de Ações (Salvar e Reset) =================================
    
    label_feedback = create_label(parent_tab, "")
    label_feedback.grid(row=row_idx, column=0, columnspan=3, padx=20, pady=(20, 5), sticky="ew")
    row_idx += 1

    # Frame para botões inferiores para organizar
    frame_actions = ctk.CTkFrame(parent_tab, fg_color="transparent")
    frame_actions.grid(row=row_idx, column=0, columnspan=3, pady=10, sticky="ew")
    frame_actions.grid_columnconfigure(0, weight=1)
    frame_actions.grid_columnconfigure(1, weight=1)

    def save_all_paths():
        for k, e in path_entries.items():
            new_path = e.get()
            # Garante barras invertidas ao salvar
            new_path = new_path.replace("/", "\\")
            add_path(k, new_path)
        label_feedback.configure(text="Todos os caminhos foram atualizados!", text_color="green")

    def perform_reset():
        """Reseta os caminhos e atualiza a interface gráfica."""
        reset_paths_action(label_feedback)
        
        # Recarrega os caminhos atualizados do JSON
        new_paths = get_all_paths()
        
        # Atualiza os campos de texto na interface
        for k, value in new_paths.items():
            if k in path_entries:
                path_entries[k].delete(0, 'end')
                path_entries[k].insert(0, value)

    # Botão Salvar
    btn_save_all = create_button(frame_actions, "Salvar Alterações", command=save_all_paths)
    btn_save_all.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Botão Reset
    btn_reset = create_button(
        frame_actions,
        "Resetar Padrões",
        command=perform_reset
    )
    # Opcional: cor diferente para o botão de reset para diferenciar
    btn_reset.configure(fg_color="#555555", hover_color="#333333") 
    btn_reset.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

    # ============================= Espaçador e Rodapé =================================
    
    # Configura a linha logo após os botões para expandir e empurrar o rodapé para baixo
    parent_tab.grid_rowconfigure(row_idx + 1, weight=1)

    label_rodape = create_label(parent_tab, "Desenvolvido por Cintra Labs")
    label_rodape.configure(text_color="gray")
    # row=99 garante que fique no final, e o grid_rowconfigure acima empurra ele
    label_rodape.grid(row=99, column=0, columnspan=3, padx=20, pady=10, sticky="s")
