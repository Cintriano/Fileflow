import os
from datetime import datetime
from PIL import Image
import random


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
def renomear_meta(caminho_arquivo, pasta):
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
        print("Erro Função(renomear_meta): ", e)


#RENOMEIA OS ARQUIVOS COM UMA DATA DEFINIDA ESPECIFICA
def renomear_especifico(pasta, data_personalizada):
    try:
        data_personalizada = datetime.strptime(data_personalizada, "%d.%m.%Y")
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo):
                extensao = caminho_arquivo[-3:]
                novo_nome = f"{data_personalizada.strftime('%d.%m.%Y')}_{random.randint(10000, 99999)}.{extensao}"
                novo_caminho = os.path.join(pasta, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
            infos = [(novo_caminho, novo_caminho, "Desconhecido")]
        return infos
    except Exception as e:
        print("Erro Função(renomear_especifico): ", e)


#VALIDA SE OS ARQUIVOS POSSUEM METADADOS
def validacao_meta(caminho_arquivo):
    try:
        device = data = False
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 272:
                device = True
            if tag_id == 306:
                data = True
        if device and data:
            return True
        return False
    except Exception as e:
        print("Erro Função(validacao_meta): ", e)


#VALIDA SE AS EXTENÇÕES DOS ARQUIVOS SÃO VALIDAS
def validacao_arq(caminho_arquivo):
    try:
        if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif', '.CR2', '.JPG',
                                                                         '.mp4')):
            return True
        return False
    except Exception as e:
        print("Erro Função(validacao_arq): ", e)


#VALIDA SE O ARQUIVO ESTÁ NO PADRÃO DE DATA
def valida_padrao_data(caminho_arquivo):
    try:
        nome_arquivo = caminho_arquivo[42::]
        data_arquivo = datetime.strptime(nome_arquivo[0:10], "%d.%m.%Y")
        data_sistema = datetime.now()
        if (nome_arquivo[2] == "." and nome_arquivo[5] == "." and nome_arquivo[10] == "_" and
                caminho_arquivo[-5:].isdigit()) and len(nome_arquivo) == 16:
            if (1 <= int(nome_arquivo[0:2]) <= 31 and 1 <= int(nome_arquivo[3:5]) <= 12 and
                    1960 <= int(nome_arquivo[6:10]) <= 2174) and data_arquivo <= data_sistema:
                return False
        return True
    except Exception as e:
        print("Erro Função(valida_padrao_data): ", e)


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
