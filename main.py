import os
from datetime import datetime
from idlelib.replace import replace

from PIL import Image
import random


#FUNÇÃO PRINCIPAL DE RENOMEAÇÃO DE ARQUIVOS, RESPONSAVEL POR VALIDAR E DELEGAR OS ARQUIVOS
def main():
    pasta = r"C:\Users\danil\OneDrive\Temporários\Teste"
    infos = []
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo) and validacao_meta(caminho_arquivo):
                lista = renomear_meta(caminho_arquivo, pasta)
                os.rename(caminho_arquivo, lista[0])
                infos.append((lista[1], arquivo, lista[2]))
            else:
                if validacao_arq(caminho_arquivo):
                    infos = infos + (renomear_nome(arquivo, pasta))
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")
    log(infos)
    return "Processo Finalizado"


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


#CRIA REGISTROS DE TODAS AS EXECUÇÕES
def log(infos):
    pasta = r"C:\Users\danil\OneDrive\Temporários\Teste\Log"
    num = random.randint(10000, 99999)
    data = datetime.now().strftime('%d.%m.%Y')
    hora = datetime.now().strftime("%H:%M:%S")
    nome_arquivo = f"LOG_{data}_{num}.txt"
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    try:
        for arquivo in os.listdir(pasta):
            if data == arquivo[4:14]:
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, 'a') as relatorio:
                    relatorio.write('==========================\n')
                    relatorio.write(f'Execução/{data}/{hora}\n')
                    for info in infos:
                        linha = f'{info[0]}/{info[1]}/{info[2]}\n'
                        relatorio.write(linha)
                    return True
        with open(caminho_arquivo, 'a') as relatorio:
            relatorio.write('==========================\n')
            relatorio.write(f'Execução/{data}/{hora}\n')
            for info in infos:
                linha = f'{info[0]}/{info[1]}/{info[2]}\n'
                relatorio.write(linha)
            return True
    except Exception as e:
        print('Erro:', e)


#FAZ A LEITURA DO LOG PESQUISANDO UM ARQUIVO ESPECIFICO
def leitura_log(busca):
    pasta = r"C:\Users\danil\OneDrive\Temporários\Teste\Log"
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        with open(caminho_arquivo, 'r') as arq:
            for linha in arq.readlines():
                lista = linha.split('/')
                if lista[0] == busca:
                    print(f'{lista[0]} - {lista[1]} - {lista[2]}')


main()
#leitura('09.11.2024_16931.jpg')
#renomear_especifico(caminho_pasta, '20.11.2024')
