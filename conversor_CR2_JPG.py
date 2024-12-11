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
            except Exception as e:
                print(f"Erro Função(converter_cr2_jpg): {e}")

def excluir_cr2(pasta):
    try:
        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".CR2"):
                caminho_completo = os.path.join(pasta, arquivo)
                os.remove(caminho_completo)
    except Exception as e:
        print(f"Erro Função(excluir_cr2): {e}")
