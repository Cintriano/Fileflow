def renomear_camera():
    pasta = r"C:\Users\danil\OneDrive\Teste"
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo) and arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif', '.CR2', '.JPG')):
            print(f"Arquivo renomeado: {arquivo}")
            extensao = caminho_arquivo[-3:]
            path = Path(caminho_arquivo)
            data = datetime.fromtimestamp(path.stat().st_ctime)
            novo_nome = f"{data.strftime('%d.%m.%Y')}_{random.randint(10000, 99999)}.{extensao}"
            novo_caminho = os.path.join(pasta, novo_nome)
            os.rename(caminho_arquivo, novo_caminho)

def main():
    pasta = r"C:\Users\danil\OneDrive\Temporários\Teste"
    meta_arq = nome_arq = []
    infos1 = infos2 = ''
    try:


            if os.path.isfile(caminho_arquivo) and arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif', '.CR2', '.JPG',
                                                                     '.mp4')):
                image = Image.open(caminho_arquivo)
                exif_data = image.getexif()
                for tag_id, value in exif_data.items():
                    if tag_id == 272:
                        device2 = True
                    if tag_id == 306:
                        data = True
                if device2 and data:
                    meta_arq.append(arquivo)
                else:
                    nome_arq.append(arquivo)
                data = device2 = False
    except Exception as e:
        print(f"Erro ao acessar a pasta {pasta}: {e}")
    if len(meta_arq) != 0:
        for i in meta_arq:
            print(meta_arq)
            infos1 = renomear_meta(pasta, caminho_arquivo, i)
    if len(nome_arq) != 0:
        for i in nome_arq:
            infos2 = renomear_nome(pasta, caminho_arquivo, i)
        #infos = renomear_meta(pasta, caminho_arquivo, arquivo)
    log(infos1 + infos2)