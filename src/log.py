import random
from datetime import datetime
import os
from rename import validacao_arq, padrao_data

from dotenv import load_dotenv

load_dotenv()
log_path = os.getenv("LOG_PATH")

dic_mes = {
        '01': 'Janeiro',
        '02': 'Fevereiro',
        '03': 'Marco',
        '04': 'Abril',
        '05': 'Maio',
        '06': 'Junho',
        '07': 'Julho',
        '08': 'Agosto',
        '09': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }

def log(infos, tipo):
    """Essa função cria registros das execuções de renomeação e conversão de imagens"""
    pasta = log_path
    num = random.randint(10000, 99999)
    data = datetime.now().strftime('%d.%m.%Y')
    hora = datetime.now().strftime("%H:%M:%S")
    nome_arquivo = f"LOG_{data}_{num}.txt"

    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    try:
        for arquivo in os.listdir(pasta):
            if data[3:10] == arquivo[7:14]:
                caminho_arquivo = os.path.join(pasta, arquivo)
                with open(caminho_arquivo, 'a') as relatorio:
                    for info in infos:
                        if padrao_data(info[0]):
                            data_str = info[0].split('_')[0]
                            dia_captura, mes_captura, ano_captura = data_str.split('.')
                            data_captura = dia_captura + "." + mes_captura + "." + ano_captura
                            linha = f'{data};{hora};{tipo};{data_captura};{dia_captura};{dic_mes.get(mes_captura)};{ano_captura};{info[0]};{info[1]};{info[2]}\n'
                        else:
                            linha = f'{data};{hora};{tipo};0:0:0:0;{info[0]};{info[1]};{info[2]}\n'
                        relatorio.write(linha)
                    return True
        with open(caminho_arquivo, 'a') as relatorio:
            relatorio.write("data_execucao;hora_execucao;tipo_processo;data_captura;dia_captura;mes_captura;ano_captura;nome_novo;nome_antigo;dispositivo\n")
            for info in infos:
                if padrao_data(info[0]):
                    data_str = info[0].split('_')[0]
                    dia_captura, mes_captura, ano_captura = data_str.split('.')
                    data_captura = dia_captura + "." + mes_captura + "." + ano_captura
                    linha = f'{data};{hora};{tipo};{data_captura};{dia_captura};{dic_mes.get(mes_captura)};{ano_captura};{info[0]};{info[1]};{info[2]}\n'
                else:
                    linha = f'{data};{hora};{tipo};0:0:0:0;{info[0]};{info[1]};{info[2]}\n'
                relatorio.write(linha)
            return True
    except Exception as e:
        print('Erro Função(Log):', e)
