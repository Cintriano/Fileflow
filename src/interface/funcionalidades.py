import customtkinter as ctk

def executar(label_feedback):
    try:
        print("este")
        label_feedback.configure(text="Finalizado", text_color="green")
    except Exception as e:
        label_feedback.configure(text="Erro", text_color="red")
