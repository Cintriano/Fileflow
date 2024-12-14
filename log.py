import random
from datetime import datetime
import os
from rename import validacao_arq


#CRIA REGISTROS DE TODAS AS EXECUÇÕES
def log(infos, tipo):
    pasta = r"C:\Users\danil\OneDrive\Temporários\Teste\Log"
    num = random.randint(10000, 99999)
    quant_arq = len(infos)
    data = datetime.now().strftime('%d.%m.%Y')
    hora = datetime.now().strftime("%H:%M:%S")
    nome_arquivo = f"LOG_{data}_{num}.txt"
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    try:
        for arquivo in os.listdir(pasta):
            if data == arquivo[4:14]:
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, 'a') as relatorio:
                    relatorio.write(f'Execução/{data}/{hora}/{quant_arq}/{tipo}\n')
                    for info in infos:
                        linha = f'{info[0]}/{info[1]}/{info[2]}\n'
                        relatorio.write(linha)
                    return True
        with open(caminho_arquivo, 'a') as relatorio:
            relatorio.write(f'Execução/{data}/{hora}/{quant_arq}/{tipo}\n')
            for info in infos:
                linha = f'{info[0]}/{info[1]}/{info[2]}\n'
                relatorio.write(linha)
            return True
    except Exception as e:
        print('Erro Função(Log):', e)
