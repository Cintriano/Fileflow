import customtkinter as ctk

def create_label(label: str, janela):
    campo_escolha_pasta = ctk.CTkLabel(janela, text=label)
    campo_escolha_pasta.pack()