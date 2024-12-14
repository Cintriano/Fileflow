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
        return "Processo Finalizado"
    except Exception as e:
        return f"Erro Função(main_c): {e}"

def main_c(pasta, operacao):
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    infos = []
    try:
        if operacao == "1":
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".CR2"):
                    infos = infos + converter_cr2_jpg(pasta, arquivo)
                    excluir(pasta, arquivo, ".CR2")
        elif operacao == "2":
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".CR2"):
                    infos = infos + converter_cr2_png(pasta, arquivo)
                    excluir(pasta, arquivo, ".CR2")
        elif operacao == "3":
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".jpg") or arquivo.endswith(".JPEG"):
                    infos = infos + converter_jpg_png(pasta, arquivo)
                    excluir(pasta, arquivo, ".jpg")
        elif operacao == "4":
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".png"):
                    infos = infos + converter_png_jpg(pasta, arquivo)
                    excluir(pasta, arquivo, ".png")
        log(infos, "c")
        return "Processo Finalizado"
    except Exception as e:
        return f"Erro Função(main_c): {e}"


#leitura('09.11.2024_16931.jpg')
#renomear_especifico(caminho_pasta, '20.11.2024')
