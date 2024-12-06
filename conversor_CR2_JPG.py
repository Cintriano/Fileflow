from PIL import Image
import os

def converter_cr2_jpg(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".CR2"):
            caminho_completo = os.path.join(pasta, arquivo)
            try:
                img = Image.open(caminho_completo)
                novo_nome = arquivo.replace(".CR2", ".jpg")
                novo_caminho = os.path.join(pasta, novo_nome)
                img.save(novo_caminho, "JPEG")
                os.remove(caminho_completo)
                print(f"Arquivo convertido e excluído: {novo_caminho}")
            except Exception as e:
                print(f"Erro ao converter ou excluir {arquivo}: {e}")

def excluir_cr2(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".CR2"):
            caminho_completo = os.path.join(pasta, arquivo)
            os.remove(caminho_completo)


caminho_pasta = r"C:\Users\danil\OneDrive\Teste"
converter_cr2_jpg(caminho_pasta)
excluir_cr2(caminho_pasta)
