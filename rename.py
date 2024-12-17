import os
import random
from datetime import datetime

from PIL import Image


# RENOMEIA OS ARQUIVOS ATRAVEZ DAS INFORMAÇÕES DO NOME
def renomear_nome(arquivo, pasta):
    try:
        caminho_arquivo = os.path.join(pasta, arquivo)
        data = arquivo
        extensao = caminho_arquivo[-3:]
        for caractere in data:
            if not caractere.isdigit():
                data = data.replace(caractere, '')
        data_final = f"{data[6:8]}.{data[4:6]}.{data[0:4]}"
        novo_nome = f"{data_final}_{random.randint(10000, 99999)}.{extensao}"
        novo_caminho = os.path.join(pasta, novo_nome)
        os.rename(caminho_arquivo, novo_caminho)
        infos = [(novo_nome, arquivo, "Desconhecido")]
        return infos
    except Exception as e:
        print("Erro Função(renomear_nome): ", e)


#RENOMEIA OS ARQUIVOS ATRAVEZ DAS INFORMAÇÕES DOS METADADOS
def renomear_meta_completo(caminho_arquivo, pasta):
    try:
        Image.MAX_IMAGE_PIXELS = None
        extensao = caminho_arquivo[-3:]
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 272:
                device = value
            if tag_id == 306:
                data = value.split(" ")[0].replace(":", ".")
                data_final = ".".join(data.split(".")[::-1])
                novo_nome = f"{data_final}_{random.randint(10000, 99999)}.{extensao}"
                novo_caminho = os.path.join(pasta, novo_nome)
                image.close()
                infos = [novo_caminho, novo_nome, device]
        return infos
    except Exception as e:
        print("Erro Função(renomear_meta_completo): ", e)

def renomear_meta_parcial(caminho_arquivo, pasta):
    try:
        Image.MAX_IMAGE_PIXELS = None
        extensao = caminho_arquivo[-3:]
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 306:
                data = value.split(" ")[0].replace(":", ".")
                data_final = ".".join(data.split(".")[::-1])
                novo_nome = f"{data_final}_{random.randint(10000, 99999)}.{extensao}"
                novo_caminho = os.path.join(pasta, novo_nome)
                image.close()
                infos = [novo_caminho, novo_nome, "Desconhecido"]
        return infos
    except Exception as e:
        print("Erro Função(renomear_meta_parcial): ", e)


#RENOMEIA OS ARQUIVOS COM UMA DATA DEFINIDA ESPECIFICA
def renomear_especifico(caminho_arquivo, data_personalizada, pasta):
    try:
        extensao = caminho_arquivo[-3:]
        novo_nome = f"{data_personalizada.strftime('%d.%m.%Y')}_{random.randint(10000, 99999)}.{extensao}"
        novo_caminho = os.path.join(pasta, novo_nome)
        os.rename(caminho_arquivo, novo_caminho)
        infos = [(novo_caminho, novo_caminho, "Desconhecido")]
        return infos
    except Exception as e:
        print("Erro Função(renomear_especifico): ", e)


#VALIDA SE OS ARQUIVOS POSSUEM METADADOS
def validacao_meta_data(caminho_arquivo):
    try:
        data = False
        Image.MAX_IMAGE_PIXELS = None
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 306:
                data = True
        if data:
            return True
        return False
    except Exception as e:
        print("Erro Função(validacao_meta_data): ", e)

def validacao_meta_dispositivo(caminho_arquivo):
    try:
        device = False
        Image.MAX_IMAGE_PIXELS = None
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 272:
                device = True
        if device:
            return True
        return False
    except Exception as e:
        print("Erro Função(validacao_meta_dispositivo): ", e)


#VALIDA SE AS EXTENÇÕES DOS ARQUIVOS SÃO VALIDAS
def validacao_arq(caminho_arquivo):
    try:
        if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith((".jpg", ".png", ".gif", ".CR2", ".JPG",
                                                                         ".mp4",)):
            return True
        return False
    except Exception as e:
        print("Erro Função(validacao_arq): ", e)


#VALIDA SE O ARQUIVO ESTÁ NO PADRÃO DE DATA
def padrao_data(caminho_arquivo):
    data_sistema = datetime.now()
    try:
        nome_arquivo = os.path.basename(caminho_arquivo)
        nome_arquivo = nome_arquivo[:-4]
        if len(nome_arquivo) != 16:
            return False
        if nome_arquivo[2] != "." or nome_arquivo[5] != "." or nome_arquivo[10] != "_":
            return False
        parte_data = nome_arquivo[:10]
        parte_numero = nome_arquivo[11:]
        if not parte_numero.isdigit() or len(parte_numero) != 5:
            return False
        try:
            data_arquivo = datetime.strptime(parte_data, "%d.%m.%Y")
        except ValueError:
            return False
        if data_arquivo >= data_sistema:
            return False
        return True
    except Exception as e:
        print("Erro na Função(padrao_data):", e)
        return False


#REMOVE O ENCHANCED DOS ARQUIVOS
def remove_enhanced(pasta):
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo):
                novo_nome = arquivo.replace(arquivo[-16:-4:], "")
                novo_caminho = os.path.join(pasta, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
    except Exception as e:
        print("Erro Função(remover_enhanced): ", e)
    # -Enhanced-NR
