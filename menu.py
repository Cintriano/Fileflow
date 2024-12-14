from main import *

operacao = ""
pasta = None

while operacao != "sair":
    print("1 - Renomear \n2 - Converter \n3 - Consultar")
    try:
        operacao = input(str("\nOperação: "))

        if operacao == "sair":
            print("Processo Encerrado")
            break

        if operacao != "3":
            print("P - Padrão(Teste) \nC - Cartão-SD \nN - Novo")

            tipo_caminho = input(str("Tipo Caminho:"))

            if tipo_caminho == "p" or tipo_caminho == "P":
                pasta = r"C:\Users\danil\OneDrive\Temporários\Teste"
            elif tipo_caminho == "c" or tipo_caminho == "C":
                pasta = r"D:\DCIM\100CANON"
            elif tipo_caminho == "n" or tipo_caminho == "N":
                nova_pasta = input("Nova Pasta: ")
                pasta = nova_pasta
            else:
                print("Tipo de Caminho Invalido")

        if operacao == "1" and pasta is not None:
            print(main_r(pasta))
        elif operacao == "2" and pasta is not None:
            print("1 - CR2 -> jpg \n2 - CR2 -> png \n3 - jpg -> png \n4 - png -> jpg")
            operacao = input(str("\nOperação:"))
            print(main_c(pasta, operacao))
        elif operacao == "3" and pasta is None:
            pasta = r"C:\Users\danil\OneDrive\Temporários\Teste\Log"
            nome_arquivo = input(str("Nome do Arquivo: "))
            print(main_b(pasta, nome_arquivo))
        else:
            print('Caracteres Invalidos')
    except Exception as e:
        print(f'Erro Função(Menu): {e}')
