# Imports for path management and main logic
import os
from dotenv import load_dotenv
from main import main_datacao_auto, main_remover_enchanced, main_nomeacao_sem_data, main_datacao_manual

# UI components and functionality helpers
from componentes.comp_selec_pasta import *
from funcionalidades import botao_nova_pasta, verificar_log

# Load environment variables from .env file
load_dotenv()
PATH_UPLOADS = os.getenv("PATH_UPLOADS")
PATH_PENDENTES = os.getenv("PATH_PENDENTES")
PATH_SD_EXTERNO = os.getenv("PATH_SD_EXTERNO")


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
    button_browse = create_button(parent_tab, "Nova pasta", command=lambda: botao_nova_pasta(label_pasta, selector_pasta))

    button_browse.configure(width=90)

    # Posiciona os componentes na primeira linha (3 colunas)
    label_pasta.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="w")
    selector_pasta.grid(row=0, column=1, padx=0, pady=(20, 10), sticky="ew")
    button_browse.grid(row=0, column=2, padx=(5, 20), pady=(20, 10), sticky="w")

    # ============================= Campo de Texto para Data Manual =================================
    # O campo de data é criado aqui, mas inicialmente fica oculto.
    input_data = input_text(parent_tab, "Data", "dd.mm.aaaa")
    # Oculta o campo de data até que a opção "Datação Manual" seja selecionada.
    # Usamos 'grid_remove()' para que o widget não ocupe espaço no layout.
    input_data.grid_remove()

    # ============================= Seleção do processo de execução =================================

    def on_metodo_selecionado(metodo):
        """
        Callback executado quando uma nova opção no seletor de método é escolhida.
        Mostra ou oculta o campo de data com base na seleção.
        """
        if metodo == "Datação Manual":
            # Posiciona o campo de data na grade para torná-lo visível.
            input_data.grid(row=2, column=1, columnspan=3, padx=20, pady=10, sticky="ew")
        else:
            # Remove o campo de data da grade para ocultá-lo.
            input_data.grid_remove()

    label_metodo = create_label(parent_tab, "Selecione o método")

    # Lista de opções disponíveis
    lista_opcoes_metodo = ["Datação Automática", "Datação Manual", "Remover Enhanced", "Nomeação sem Data"]

    # Cria o seletor e associa a função de callback ao seu comando.
    selector_metodo = create_selector(
        parent_tab,
        opcoes=lista_opcoes_metodo,
        default_value="Datação Automática",
        command=on_metodo_selecionado
    )

    # Posiciona o label e o seletor de método na grade
    label_metodo.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")
    # O seletor agora ocupa as colunas 1 e 2 e se expande (sticky="ew")
    selector_metodo.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=10, sticky="ew")

    # ============================= Switch do Log =================================
    switch_log = create_switch(parent_tab, "Log")
    switch_log.select()
    switch_log.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="w")

    # ============================= Botão de Execução e Feedback =================================

    label_feedback = create_label(parent_tab, "")

    # --- Funções de Lógica ---
    def obter_caminho_selecionado() -> str:
        """Obtém o caminho do diretório com base na seleção do combobox."""
        opcao = selector_pasta.get()
        if opcao == "Uploads":
            return PATH_UPLOADS
        elif opcao == "Pendentes":
            return PATH_PENDENTES
        elif opcao == "SD-Externo":
            return PATH_SD_EXTERNO
        return opcao  # Caso um caminho customizado seja selecionado

    def executar_rename():
        """Função principal que é chamada pelo botão 'Executar'.
        Ela lê os seletores, chama a função de lógica apropriada e exibe o feedback."""
        try:
            caminho = obter_caminho_selecionado()
            metodo = selector_metodo.get()
            log_ativo = verificar_log(switch_log)

            # TODO: A lógica de log está atualmente dentro das funções 'main_*'.
            # O estado de 'log_ativo' precisaria ser passado para essas funções para controlá-la.

            resultado = ""
            if metodo == "Datação Automática":
                resultado = main_datacao_auto(caminho)
            elif metodo == "Datação Manual":
                data_fornecida = input_data.entry.get()
                if not data_fornecida:
                    raise ValueError("A data manual não foi fornecida.")
                resultado = main_datacao_manual(caminho, data_fornecida)
                label_feedback.configure(text_color="orange")
            elif metodo == "Remover Enhanced":
                resultado = main_remover_enchanced(caminho)
            elif metodo == "Nomeação sem Data":
                resultado = main_nomeacao_sem_data(caminho)

            label_feedback.configure(text=resultado, text_color="green")

        except Exception as e:
            label_feedback.configure(text=f"Erro: {e}", text_color="red")


    botao_executar = create_button(parent_tab, "Executar", command=executar_rename)

    # Posiciona o botão e o label de feedback, fazendo-os ocupar as três colunas (columnspan=3)
    botao_executar.grid(row=4, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")
    label_feedback.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

    label_rodape = create_label(parent_tab, "Desenvolvido por Danilo")
    label_rodape.configure(text_color="gray")
    label_rodape.grid(row=7, column=0, columnspan=3, padx=20, pady=10, sticky="s")
