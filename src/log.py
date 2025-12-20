import random
from datetime import datetime
import os
from rename import validacao_arq, padrao_data
from path_controller.uti_path import busca_path

log_path = busca_path("LOG_PATH")

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


def log(infos: list[tuple], tipo: str, log_ativo: bool) -> bool:
    """Essa função cria registros das execuções de renomeação e conversão de imagens"""
    if len(infos) == 0 or not log_ativo:
        return False

    pasta = log_path
    num = random.randint(10000, 99999)
    data = datetime.now().strftime('%d.%m.%Y')
    hora = datetime.now().strftime("%H:%M:%S")
    
    # Define o arquivo alvo (procura um existente do mesmo mês ou cria novo)
    caminho_arquivo = None
    mes_ano_atual = data[3:10] # mm.yyyy
    
    try:
        if os.path.exists(pasta):
            for arquivo in os.listdir(pasta):
                # Verifica se é um arquivo de log válido e se pertence ao mês atual
                if arquivo.startswith("LOG_") and arquivo.endswith(".txt") and len(arquivo) >= 14:
                    if arquivo[7:14] == mes_ano_atual:
                        caminho_arquivo = os.path.join(pasta, arquivo)
                        break
        
        # Se não encontrou arquivo compatível, define caminho para um novo
        novo_arquivo = False
        if caminho_arquivo is None:
            caminho_arquivo = os.path.join(pasta, f"LOG_{data}_{num}.txt")
            novo_arquivo = True

        with open(caminho_arquivo, 'a', encoding='utf-8') as relatorio:
            if novo_arquivo:
                relatorio.write("data_execucao;hora_execucao;tipo_processo;data_captura;dia_captura;mes_captura;ano_captura;nome_novo;nome_antigo;dispositivo\n")
            
            for info in infos:
                try:
                    # Tenta formatar a linha. Se falhar, não quebra o loop dos outros arquivos
                    if padrao_data(info[0]):
                        data_str = info[0].split('_')[0]
                        # Garante que o split gerou 3 partes antes de desempacotar
                        partes_data = data_str.split('.')
                        if len(partes_data) == 3:
                            dia_captura, mes_captura, ano_captura = partes_data
                            nome_mes = dic_mes.get(mes_captura, "Desconhecido")
                            data_captura_fmt = f"{dia_captura}.{mes_captura}.{ano_captura}"
                            
                            linha = f'{data};{hora};{tipo};{data_captura_fmt};{dia_captura};{nome_mes};{ano_captura};{info[0]};{info[1]};{info[2]}\n'
                            relatorio.write(linha)
                            continue # Pula para o próximo info se deu certo

                    # Caso não seja padrao_data ou falhe a validação acima, escreve log genérico
                    linha = f'{data};{hora};{tipo};0:0:0:0;{info[0]};{info[1]};{info[2]}\n'
                    relatorio.write(linha)
                
                except Exception as e_linha:
                    print(f"Erro ao logar arquivo {info[0]}: {e_linha}")
                    # Continua para o próximo arquivo da lista
        
        return True

    except Exception as e:
        print('Erro Função(Log):', e)
        return False
