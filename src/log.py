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
    # Alterado para o novo padrão yyyy_mm_dd
    data = datetime.now().strftime('%Y_%m_%d')
    hora = datetime.now().strftime("%H:%M:%S")
    
    # Define o arquivo alvo (procura um existente do mesmo mês ou cria novo)
    caminho_arquivo = None
    # Pega yyyy_mm para agrupar logs do mesmo mês
    mes_ano_atual = data[0:7] 
    
    try:
        if os.path.exists(pasta):
            for arquivo in os.listdir(pasta):
                # Verifica se é um arquivo de log válido e se pertence ao mês atual
                # Nome esperado: LOG_yyyy_mm_dd_num.txt
                # LOG_ (4 chars) + yyyy (4) + _ (1) + mm (2) = 11 chars até o fim do mês
                if arquivo.startswith("LOG_") and arquivo.endswith(".txt") and len(arquivo) >= 14:
                    # Verifica se os caracteres de yyyy_mm batem
                    if arquivo[4:11] == mes_ano_atual:
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
                        # info[0] está no formato yyyy_mm_dd_num.ext (validado por padrao_data)
                        data_str = info[0][:10] # Pega "yyyy_mm_dd"
                        ano_captura, mes_captura, dia_captura = data_str.split('_')
                        
                        nome_mes = dic_mes.get(mes_captura, "Desconhecido")
                        # Formata para o log mantendo o padrão yyyy_mm_dd
                        data_captura_fmt = f"{ano_captura}_{mes_captura}_{dia_captura}"
                        
                        linha = f'{data};{hora};{tipo};{data_captura_fmt};{dia_captura};{nome_mes};{ano_captura};{info[0]};{info[1]};{info[2]}\n'
                        relatorio.write(linha)
                        continue # Pula para o próximo info se deu certo

                    # Caso não seja padrao_data ou falhe a validação acima, escreve log genérico
                    linha = f'{data};{hora};{tipo};0000_00_00;0;0;0;{info[0]};{info[1]};{info[2]}\n'
                    relatorio.write(linha)
                
                except Exception as e_linha:
                    print(f"Erro ao logar arquivo {info[0]}: {e_linha}")
                    # Continua para o próximo arquivo da lista
        
        return True

    except Exception as e:
        print('Erro Função(Log):', e)
        return False
