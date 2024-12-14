from rename import *
from log import *
from conversor import *

#FUNÇÃO PRINCIPAL DE RENOMEAÇÃO DE ARQUIVOS, RESPONSAVEL POR VALIDAR E DELEGAR OS ARQUIVOS
def main_r(pasta):
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    infos = []
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo) and not (padrao_data(caminho_arquivo)):
                if validacao_meta(caminho_arquivo):
                    lista = renomear_meta(caminho_arquivo, pasta)
                    os.rename(caminho_arquivo, lista[0])
                    infos.append((lista[1], arquivo, lista[2]))
                else:
                    infos = infos + (renomear_nome(arquivo, pasta))
        if len(infos) != 0:
            log(infos, "r")
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")
    return "Processo Finalizado"

def main_c(pasta, operacao):
    infos = []
    if operacao == "1":
        return converter_cr2_jpg(pasta)
    elif operacao == "2":
        return converter_cr2_png(pasta)
    elif operacao == "3":
        return converter_jpg_png(pasta)
    elif operacao == "4":
        converter_png_jpg(pasta)
#leitura('09.11.2024_16931.jpg')
#renomear_especifico(caminho_pasta, '20.11.2024')
