import os
from datetime import datetime
from PIL import Image
import random


# RENOMEIA OS ARQUIVOS ATRAVEZ DAS INFORMAÇÕES DO NOME
def renomear_nome(arquivo, pasta):
    infos = []
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
        infos.append((novo_nome, arquivo, "Desconhecido"))
    except Exception as e:
        print(f"Erro {e}")
    return infos


#RENOMEIA OS ARQUIVOS ATRAVEZ DAS INFORMAÇÕES DOS METADADOS
def renomear_meta(caminho_arquivo, pasta):
    extensao = caminho_arquivo[-3:]
    image = Image.open(caminho_arquivo)
    exif_data = image.getexif()
    for tag_id, value in exif_data.items():
        if tag_id == 272:
            device = value
        if tag_id == 306:
            date = value.split(" ")[0].replace(":", ".")
            date_final = ".".join(date.split(".")[::-1])
            novo_nome = f"{date_final}_{random.randint(10000, 99999)}.{extensao}"
            novo_caminho = os.path.join(pasta, novo_nome)
            image.close()
            lista = [novo_caminho, novo_nome, device]
    return lista


#RENOMEIA OS ARQUIVOS COM UMA DATA DEFINIDA ESPECIFICA
def renomear_especifico(pasta, data_personalizada):
    data_personalizada = datetime.strptime(data_personalizada, '%d.%m.%Y')
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif', '.CR2')):
            caminho_completo = os.path.join(pasta, arquivo)
            extensao = caminho_completo[-3:]
            novo_nome = f"{data_personalizada.strftime('%d.%m.%Y')}_{random.randint(10000, 99999)}.{extensao}"
            novo_caminho = os.path.join(pasta, novo_nome)
            os.rename(caminho_completo, novo_caminho)
            print(f"Arquivo renomeado: {novo_caminho}")


#VALIDA SE OS ARQUIVOS POSSUEM METADADOS
def validacao_meta(caminho_arquivo):
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


#VALIDA SE AS EXTENÇÕES DOS ARQUIVOS SÃO VALIDAS
def validacao_arq(caminho_arquivo):
    if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif', '.CR2', '.JPG',
                                                                     '.mp4')):
        return True
    return False


def remove_enhanced():
    pasta = r"C:\Users\danil\OneDrive\Temporários\Teste"
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if validacao_arq(caminho_arquivo):
            novo_nome = arquivo.replace(arquivo[-16:-4:], "")
            novo_caminho = os.path.join(pasta, novo_nome)
            os.rename(caminho_arquivo, novo_caminho)
    # -Enhanced-NR
