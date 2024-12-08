from rename import *
from log import *

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


main()
#leitura('09.11.2024_16931.jpg')
#renomear_especifico(caminho_pasta, '20.11.2024')
