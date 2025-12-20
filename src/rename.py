import os
import random
from datetime import datetime
from idlelib.replace import replace
from PIL.ExifTags import TAGS, GPSTAGS

from PIL import Image


# RENOMEIA OS ARQUIVOS ATRAVEZ DAS INFORMAÇÕES DO NOME
def renomear_nome(arquivo, pasta):
    try:
        caminho_arquivo = os.path.join(pasta, arquivo)
        data = arquivo
        extensao = extensao_format(caminho_arquivo)
        for caractere in data:
            if not caractere.isdigit():
                data = data.replace(caractere, '')
        # Formato yyyy_mm_dd
        # Assume que 'data' contem yyyymmdd ou ddmmyyyy? 
        # O código original era data[6:8].data[4:6].data[0:4] -> dd.mm.yyyy
        # Isso sugere que a entrada 'data' (após limpar não dígitos) era yyyymmdd (AnoMesDia)
        # Ex: 20231025 -> 25.10.2023
        # Agora queremos yyyy_mm_dd -> 2023_10_25
        data_final = f"{data[0:4]}_{data[4:6]}_{data[6:8]}"
        
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
        extensao = extensao_format(caminho_arquivo)
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 272:
                device = value
            if tag_id == 306:
                # value vem como "yyyy:mm:dd HH:MM:SS"
                # Queremos "yyyy_mm_dd"
                data_final = value.split(" ")[0].replace(":", "_")
                
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
        extensao = extensao_format(caminho_arquivo)
        image = Image.open(caminho_arquivo)
        exif_data = image.getexif()
        for tag_id, value in exif_data.items():
            if tag_id == 306:
                # value vem como "yyyy:mm:dd HH:MM:SS"
                # Queremos "yyyy_mm_dd"
                data_final = value.split(" ")[0].replace(":", "_")
                
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
        extensao = extensao_format(caminho_arquivo)
        # Formato yyyy_mm_dd
        novo_nome = f"{data_personalizada.strftime('%Y_%m_%d')}_{random.randint(10000, 99999)}.{extensao}"
        novo_caminho = os.path.join(pasta, novo_nome)
        os.rename(caminho_arquivo, novo_caminho)
        return novo_nome
    except Exception as e:
        print("Erro Função(renomear_especifico): ", e)


def validacao_meta_data(caminho_arquivo):
    """Essa função Valida a existencia dos metadados (data) do arquivo"""
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
    """Essa função Valida a existencia dos metadados (nome do dispositivo) do arquivo"""
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


def validacao_arq(caminho_arquivo):
    """Essa função valida as extensões de arquivo que o programa ira processar"""
    try:
        if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith((".jpg", "jpeg", ".png", ".gif", ".CR2", ".JPG",
                                                                         ".mp4", ".webp")):
            return True
        return False
    except Exception as e:
        print("Erro Função(validacao_arq): ", e)


#VALIDA SE O ARQUIVO ESTÁ NO PADRÃO DE DATA
def padrao_data(caminho_arquivo):
    data_sistema = datetime.now()
    try:
        nome_arquivo = os.path.basename(caminho_arquivo)
        nome_arquivo = remover_extensao(nome_arquivo)
        if len(nome_arquivo) != 16:
            return False
        # Formato esperado: yyyy_mm_dd_num (ex: 2023_10_25_12345)
        # Índices dos separadores: 4 e 7 (para data) e 10 (para numero)
        if nome_arquivo[4] != "_" or nome_arquivo[7] != "_" or nome_arquivo[10] != "_":
            return False
        parte_data = nome_arquivo[:10]
        parte_numero = nome_arquivo[11:]
        if not parte_numero.isdigit() or len(parte_numero) != 5:
            return False
        try:
            data_arquivo = datetime.strptime(parte_data, "%Y_%m_%d")
        except ValueError:
            return False
        if data_arquivo >= data_sistema:
            return False
        return True
    except Exception as e:
        print("Erro na Função(padrao_data):", e)
        return False


def remover_extensao(caminho_arquivo):
    """Remove a extensão do arquivo independente da quantidade de caracteres retornando o nome do arquivo limpo"""
    extesao = extensao_format(caminho_arquivo)
    extesao = "." + extesao
    return caminho_arquivo.replace(extesao, "")


def extensao_format(caminho_arquivo):
    """Extrai a extensão do arquivo e retorna em formato string"""
    extensao = (caminho_arquivo.split("."))[-1]
    return extensao
