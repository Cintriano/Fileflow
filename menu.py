from main import renomear_celular, renomear_camera, renomear_especifico

device = ''

while device.islower() != 'sair':
    print('1 - Celular \n2 - Camera \n3 - Externo')

    try:
        device = input('\nQual o Dispositivo:')

        if device == '1':
            renomear_celular()
        elif device == '2':
            renomear_camera()
        elif device == '3':
            caminho = input('\nCaminho da Pasta:')
            data = input('Data:')
            renomear_especifico(caminho, data)
        else:
            print('Caracteres Invalidos')
    except Exception as e:
        print(f'Erro: {e}')


