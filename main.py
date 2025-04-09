from rename import *
from log import *
from conversor import *

def main_datacao_auto(pasta):
    """Função main de renomeação que reliza as validações necessarias para datar os arquivos automaticamente
    de acordo com a disponibilidade dos metadados, a renomeação pode ser feito com os dados
    completos (renomear_meta_completo) com data e dispositivo, ou parcial (renomear_meta_parcial) apenas data"""
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
        return f"Erro Função(main_datacao_auto): {e}"


def main_datacao_manual(data_personalizada, pasta):
    """Essa função recebe a pasta uma data no padrão (dd.mm.aaaa) e renomeia todos os arquivos de uma pasta com ela"""
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
        return f"Erro Função(main_datacao_manual): {e}"


def main_nomeacao_sem_data(pasta):
    """Essa função renomeia todos os arquivos da pasta recebida que estejam sem nenhuma informação de data
     disponivel, usando esse padrão (IMG_82173)"""
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if validacao_arq(caminho_arquivo):
                extensao = extensao_formt(caminho_arquivo)
                if extensao == "mp4":
                    novo_nome = f"VID_{random.randint(10000, 99999)}.{extensao}"
                else:
                    novo_nome = f"IMG_{random.randint(10000, 99999)}.{extensao}"
                novo_caminho = os.path.join(pasta, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
    except Exception as e:
        return f"Erro Função(main_nomeacao_sem_data): {e}"


def main_conversao(pasta, operacao):
    """Essa função oferece converções de extenção de arquivos de imagem
     CR2 -> PNG, CR2 -> JPG, JPG -> PNG, PNG -> JPG"""
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
        return f"Erro Função(main_conversao): {e}"


def main_busca_log(pasta, nome_arquivo):
    """Função para realizar buscas nos arquivos de log por meio do nome do arquivo"""
    if not os.path.exists(pasta):
        return "Pasta não Existente"
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'r') as arq:
                for linha in arq.readlines():
                    lista = linha.split('/')
                    if lista[3] == nome_arquivo:
                        return f'{lista[0]} - {lista[1]} - {lista[2]} - {lista[3]} - {lista[4]} - {lista[5]}'
    except Exception as e:
        return "Erro Função(main_busca_log):", e


def main_remover_enchanced(pasta):
    """Função que remove o texto (-Enchanced-NR) do final do nome dos arquivos de imagem de uma pasta
       inteira"""
    try:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            nome_arquivo = remover_extensao(arquivo)
            if validacao_arq(caminho_arquivo):
                delecao = ""
                if nome_arquivo[-12:] == "-Enhanced-NR":
                    delecao = "-Enhanced-NR"
                elif nome_arquivo[-14:] == "-Aprimorado-NR":
                    delecao = "-Aprimorado-NR"
                elif nome_arquivo[-14:] == "-Aprimorado-SR":
                    delecao = "-Aprimorado-SR"
                novo_nome = arquivo.replace(delecao, "")
                novo_caminho = os.path.join(pasta, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
        return "Processo Finalizado"
    except Exception as e:
        return "Erro Função(main_remover_enchanced):", e
