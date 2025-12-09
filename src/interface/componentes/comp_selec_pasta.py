import customtkinter as ctk

def create_label(janela, text: str):
    """Cria um CTkLabel (rótulo de texto) e o retorna."""
    label = ctk.CTkLabel(janela, text=text)
    return label


def create_input(janela, placeholder_text: str):
    """Cria um CTkEntry (campo de input) e o retorna."""
    input_widget = ctk.CTkEntry(janela, placeholder_text=placeholder_text)
    return input_widget


def create_selector(janela, opcoes: list, default_value: str, command=None):
    """
    Cria um CTkOptionMenu (seletor de opções) com um estilo moderno.
    """
    selector = ctk.CTkOptionMenu(
        master=janela,
        values=opcoes,
        height=30,  # Aumenta a altura do seletor
        font=("Calibri", 14), # Define a fonte e o tamanho do texto
        corner_radius=5, # Adiciona cantos arredondados

        # --- Paleta de Cores Azul Escuro ---
        fg_color="#243B55",  # Cor de fundo principal (azul acinzentado)
        button_color="#141E30",  # Cor do botão da seta (azul escuro)
        button_hover_color="#3A5F85",  # Cor do hover no botão (azul mais claro)
        dropdown_fg_color="white",  # Cor de fundo da lista dropdown
        dropdown_hover_color="#3A5F85",  # Cor do hover nos itens da lista
        dropdown_text_color="black", # Cor do texto na lista de opções
        text_color="white",  # Cor do texto principal do seletor
        # ------------------------------------
        command=command
    )
    # Define o valor inicial (se não for passado, será o primeiro da lista)
    selector.set(default_value)
    return selector  # Retornar o seletor é útil para obter o valor depois


def create_button(janela, text: str, command=None):
    """Cria um CTkButton (botão) e o retorna."""
    # Se 'command' for nulo, use uma função padrão (ou não defina um comando)
    cmd = command if command else lambda: print(f"Botão '{text}' clicado sem comando.")
    button = ctk.CTkButton(janela, text=text, command=cmd)
    return button


def create_tab_view(janela, tab_names: list):
    """
    Cria uma instancia de abas que preenche a janela e a retorna.
    """
    tab_view = ctk.CTkTabview(janela)
    tab_view.pack(padx=20, pady=20, fill="both", expand=True)

    for name in tab_names:
        tab_view.add(name)

    return tab_view


def create_switch(janela, text: str, command=None):
    """Cria um CTkSwitch (interruptor ON/OFF) e o retorna."""
    switch = ctk.CTkSwitch(master=janela, text=text, command=command, font=("Calibri", 14))
    return switch

def input_text(janela, text: str, placeholder_text: str = "", command=None):
    """
    Cria um componente composto por um rótulo e uma caixa de texto.
    Opcionalmente, associa um comando ao evento <Return> na caixa de texto.
    Retorna o frame que contém os widgets. O widget de entrada pode ser
    acessado através do atributo 'entry' do frame retornado.
    """
    frame = ctk.CTkFrame(janela, fg_color="transparent")

    label = create_label(frame, text=text)
    label.pack(side="left", padx=(0, 10), pady=5)

    entry = create_input(frame, placeholder_text=placeholder_text)
    entry.pack(side="left", fill="x", expand=True, padx=(0, 0), pady=5)

    if command:
        # O evento passa um argumento, então a lambda deve aceitá-lo
        entry.bind("<Return>", lambda event: command())

    frame.entry = entry  # Anexa o widget de entrada ao frame
    return frame
