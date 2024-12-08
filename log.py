import random
from datetime import datetime
import os

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
