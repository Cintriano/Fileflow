from rename import *
from log import *
from conversor import *

#FUNÇÃO PRINCIPAL DE RENOMEAÇÃO DE ARQUIVOS, RESPONSAVEL POR VALIDAR E DELEGAR OS ARQUIVOS
def main_datacao_auto(pasta):
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    infos = []
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo) and not (padrao_data(caminho_arquivo)):
                if validacao_meta_data(caminho_arquivo) and validacao_meta_dispositivo(caminho_arquivo):
                    lista = renomear_meta_completo(caminho_arquivo, pasta)
                    os.rename(caminho_arquivo, lista[0])
                    infos.append((lista[1], arquivo, lista[2]))
                elif validacao_meta_data(caminho_arquivo):
                    lista = renomear_meta_parcial(caminho_arquivo, pasta)
                    os.rename(caminho_arquivo, lista[0])
                    infos.append((lista[1], arquivo, lista[2]))
                else:
                    infos = infos + (renomear_nome(arquivo, pasta))
        if len(infos) != 0:
            log(infos, "r")
        return "Processo Finalizado"
    except Exception as e:
        return f"Erro Função(main_auto_r): {e}"

def main_datacao_manual(data_personalizada, pasta):
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    infos = []
    try:
        data_personalizada = datetime.strptime(data_personalizada, "%d.%m.%Y")
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo):
                novo_nome = renomear_especifico(caminho_arquivo, data_personalizada, pasta)
                infos.append((novo_nome, arquivo, "Desconhecido"))
        if len(infos) != 0:
            log(infos, "r")
        return "Processo Finalizado"
    except Exception as e:
        return f"Erro Função(main_manual_r): {e}"

def main_conversao(pasta, operacao):
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

#FAZ A LEITURA DO LOG PESQUISANDO UM ARQUIVO ESPECIFICO
def main_busca_log(pasta, nome_arquivo):
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'r') as arq:
                for linha in arq.readlines():
                    lista = linha.split('/')
                    if lista[0] == nome_arquivo:
                        return f'{lista[0]} - {lista[1]} - {lista[2]}'
    except Exception as e:
        return "Erro Função(main_b):", e

def main_remover_enchanced(pasta):
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo) and arquivo[-16:-4:] == "-Enhanced-NR":
                novo_nome = arquivo.replace("-Enhanced-NR", "")
                novo_caminho = os.path.join(pasta, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
                return "Processo Finalizado"
    except Exception as e:
        return "Erro Função(main_e):", e
