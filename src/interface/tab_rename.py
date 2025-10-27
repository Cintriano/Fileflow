from componentes.comp_selec_pasta import *
from funcionalidades import executar

def setup_rename_tab(parent_tab):
    """Configura a aba 'Rename' com todos os seus componentes e layout."""

    # --- Configuração do Layout em Grade para a Aba ---
    # A coluna 1 (do seletor principal) irá se expandir quando a janela for redimensionada
    parent_tab.grid_columnconfigure(1, weight=1)

    # ============================= Seleção de diretório =================================

    label_pasta = create_label(parent_tab, "Selecione a pasta")

    # Lista de opções disponíveis
    lista_opcoes_pasta = ["Uploads", "Pendentes", "SD-Externo"]

    # Cria o seletor e o novo botão "..."
    selector_pasta = create_selector(
        parent_tab,
        opcoes=lista_opcoes_pasta,
        default_value="Uploads",
    )
    # O comando do botão pode ser definido depois para abrir um seletor de arquivos
    button_browse = create_button(parent_tab, "Nova pasta")

    button_browse.configure(width=90)

    # Posiciona os componentes na primeira linha (3 colunas)
    label_pasta.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="w")
    selector_pasta.grid(row=0, column=1, padx=0, pady=(20, 10), sticky="ew")
    button_browse.grid(row=0, column=2, padx=(5, 20), pady=(20, 10), sticky="w")

    # ============================= Seleção do processo de execução =================================

    label_metodo = create_label(parent_tab, "Selecione o método")

    # Lista de opções disponíveis
    lista_opcoes_metodo = ["Datação Automática", "Datação Manual", "Remover Enhanced", "Nomeação sem Data"]

    # Cria o seletor
    selector_metodo = create_selector(
        parent_tab,
        opcoes=lista_opcoes_metodo,
        default_value="Datação Automática",
    )

    # Posiciona o label e o seletor de método na grade
    label_metodo.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")
    # O seletor agora ocupa as colunas 1 e 2 e se expande (sticky="ew")
    selector_metodo.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=10, sticky="ew")

    # ============================= Switch do Log =================================
    switch_log = create_switch(parent_tab, "Log")
    switch_log.select()
    switch_log.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

    # ============================= Botão de Execução e Feedback =================================

    label_feedback = create_label(parent_tab, "")
    botao_executar = create_button(parent_tab, "Executar", command=lambda: executar(label_feedback))

    # Posiciona o botão e o label de feedback, fazendo-os ocupar as três colunas (columnspan=3)
    botao_executar.grid(row=3, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")
    label_feedback.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

    label_rodape = create_label(parent_tab, "Desenvolvido por Danilo")
    label_rodape.configure(text_color="gray")
    label_rodape.grid(row=7, column=0, columnspan=3, padx=20, pady=10, sticky="s")
