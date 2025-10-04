import customtkinter as ctk
from funcionalidades import executar

def create_label(janela, text: str, pady_size):
    label = ctk.CTkLabel(janela, text=text)
    label.pack(pady=pady_size)
    return label

def create_input(janela, text: str, pady_size):
    input = ctk.CTkEntry(janela, placeholder_text=text)
    input.pack(pady=pady_size)

    return input


def create_selector(janela, opcoes: list, default_value: str, pady_size: int = 10):
    """
    Cria um CTkOptionMenu (seletor de opções).
    """

    selector = ctk.CTkOptionMenu(
        master=janela,
        values=opcoes,

        # --- DEFININDO AS CORES ---
        fg_color = ("gray", "#2B2B2B"),  # Cor de fundo do seletor
        button_color = ("gray", "#2B2B2B"),  # Cor do botão da seta
        button_hover_color = ("blue", "#144870"),  # Cor do hover no botão
        dropdown_fg_color = "gray",  # Cor de fundo da lista dropdown
        dropdown_hover_color = ("blue", "#144870"),  # Cor do hover nos itens da lista
        dropdown_text_color= "white", # Cor do texto na lista de opções
        text_color = "white"  # Cor do texto do seletor
        # --------------------------
    )
    # Define o valor inicial (se não for passado, será o primeiro da lista)
    selector.set(default_value)
    selector.pack(pady=pady_size)

    return selector  # Retornar o seletor é útil para obter o valor depois

def create_button(janela, text: str, pady_size, command=None):
    # Se 'command' for nulo, use uma função padrão (ou não defina um comando)
    cmd = command if command else lambda: print(f"Botão '{text}' clicado sem comando.")

    button = ctk.CTkButton(janela, text=text, command=cmd)
    button.pack(pady=pady_size)

    return button
