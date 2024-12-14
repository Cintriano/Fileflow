from PIL import Image
import os

def converter_cr2_jpg(pasta, arquivo):
    caminho_completo = os.path.join(pasta, arquivo)
    try:
        img = Image.open(caminho_completo)
        novo_nome = arquivo.replace(".CR2", ".jpg")
        novo_caminho = os.path.join(pasta, novo_nome)
        img.save(novo_caminho, "JPEG")
        infos = [(novo_nome, "cr2", "jpg")]
    except Exception as e:
        print(f"Erro Função(converter_cr2_jpg): {e}")
    return infos

def converter_cr2_png(pasta, arquivo):
    caminho_completo = os.path.join(pasta, arquivo)
    try:
        img = Image.open(caminho_completo)
        novo_nome = arquivo.replace(".CR2", ".png")
        novo_caminho = os.path.join(pasta, novo_nome)
        img.save(novo_caminho, "png")
        infos = [(novo_nome, "cr2", "png")]
    except Exception as e:
        print(f"Erro Função(converter_cr2_png): {e}")
    return infos

def converter_png_jpg(pasta, arquivo):
    caminho_completo = os.path.join(pasta, arquivo)
    try:
        img = Image.open(caminho_completo)
        novo_nome = arquivo.replace(".png", ".jpg")
        novo_caminho = os.path.join(pasta, novo_nome)
        img.save(novo_caminho, "JPEG")
        infos = [(novo_nome, "png", "jpg")]
    except Exception as e:
        print(f"Erro Função(converter_png_jpg): {e}")
    return infos

def converter_jpg_png(pasta, arquivo):
    caminho_completo = os.path.join(pasta, arquivo)
    try:
        img = Image.open(caminho_completo)
        novo_nome = arquivo.replace(".jpg", ".png")
        novo_caminho = os.path.join(pasta, novo_nome)
        img.save(novo_caminho, "png")
        infos = [(novo_nome, "jpg", "png")]
    except Exception as e:
        print(f"Erro Função(converter_jpg_png): {e}")
    return infos

def excluir(pasta, arquivo, extensao):
    try:
        if arquivo.endswith(extensao):
            caminho_completo = os.path.join(pasta, arquivo)
            os.remove(caminho_completo)
    except Exception as e:
        print(f"Erro Função(excluir_cr2): {e}")
