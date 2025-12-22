# Gerenciador de Fotos 📸

Este projeto foi criado para facilitar meu workflow de edição e gerenciamento de fotos, permitindo lidar com grandes 
volumes de arquivos em poucos segundos.

## ✨ Funcionalidades
-   **Renomear arquivos** automaticamente com base em metadados, nome ou data manual.
-   **Registro das execuções** para rastreamento detalhado.
-   **Configuração de caminhos** personalizada via interface gráfica.

## 📂 Renomeação de Arquivos
O programa **Diem** renomeia os arquivos seguindo um padrão predefinido (**yyyy_mm_dd_XXXXX**), onde a data é extraída
automaticamente dos metadados sempre que possível. Caso os metadados não estejam disponíveis, outras fontes de 
informação podem ser utilizadas. Se nenhuma informação de data for encontrada e eu também não souber essa informação, 
o arquivo pode ser renomeado sem a data.

Para lidar com diferentes situações, o sistema considera três cenários possíveis:

### ✅ Melhor Caso (Metadados Preservados)
Esse caso se refere a arquivos que vêm diretamente do dispositivo de origem, isso significa que todos os metadados estão 
preservados (como data, hora e dispositivo), permitindo uma renomeação precisa. Portanto o programa extrai os dados 
necessários diretamente dos metadados e realiza a renomeação.

### 📑 Caso Médio (Nome do Arquivo)
Quando o arquivo não contém metadados suficientes para a renomeação ideal, o programa utiliza as informações presentes 
no próprio nome do arquivo (**20250217_82713**, por exemplo).

Nesse caso, ele extrai e limpa os dados relevantes do nome original e os utiliza para realizar a renomeação seguindo o 
padrão estabelecido.

### ❓ Pior Caso (Sem Informações Disponíveis)
Esse caso se aplica a arquivos que não possuem nenhuma informação de data disponível, seja nos metadados ou no nome 
do arquivo.

Como o programa **Diem** não tem dados suficientes para determinar uma data, ele segue um padrão específico para esses 
casos, utilizando um formato genérico, definido como **IMG_94264** para imagens ou **VID_94264** para vídeos.

#### ❗Detalhes
Importante ressaltar que o programa **Diem** tem a capacidade de diferenciar entre o melhor caso e caso médio, 
executando a melhor abordagem de acordo com a situação, porém para o pior caso os arquivos precisam ser isolados e 
executados separadamente.

Também é possível realizar **renomeações manuais**, permitindo que o usuário forneça uma data específica que será 
aplicada a todos os arquivos de imagem/vídeo na pasta selecionada.

Essa funcionalidade é útil quando os metadados estão ausentes ou imprecisos, garantindo que os arquivos sejam 
organizados corretamente conforme a necessidade do usuário.

## ⚙️ Configuração de Caminhos
O **Diem** agora permite a **configuração dinâmica de diretórios** através da aba de Opções. O usuário pode definir e 
alterar os caminhos padrão para:
-   Pasta de Uploads/Padrão
-   Pasta de Pendentes
-   Cartão SD Externo
-   Pasta de Logs

As configurações são salvas em um arquivo JSON na raiz do projeto, garantindo persistência entre as execuções. A 
interface também oferece botões para selecionar pastas visualmente e uma opção para resetar as configurações aos 
valores padrão.

## 📜 Registro das execuções
O programa **Diem** possui um sistema de criação de **logs**, que armazena informações sobre as operações realizadas 
em arquivos `.txt`. Esses registros são gerados para cada execução de **renomeação**.

Um exemplo de registro gerado após uma renomeação é o seguinte:

	2025_02_02;22:15:51;r;2025_02_01;01;Fevereiro;2025;2025_02_01_55546.CR2;IMG_2496.CR2;Canon EOS REBEL T5i

As informações registradas incluem:

-   **Data** e **hora** da execução
-   **Tipo de execução** (renomeação ou conversão)
-   **Data da captura** (formatada e detalhada)
-   **Nome novo** e **nome antigo** do arquivo
-   **Dispositivo de origem**

Esses registros permitem um fácil rastreamento e consulta das ações realizadas no sistema, sendo gerado um arquivo para 
armazenar os registros a cada mês, agrupados pelo padrão `LOG_yyyy_mm_dd_XXXXX.txt`.

## ➕ Funcionalidades extras
Uma funcionalidade extra do **Diem** é a capacidade de lidar com alterações no nome de arquivos feitas por programas de 
edição de imagens.

Por exemplo, programas como o **Adobe Lightroom** podem adicionar sufixos ao nome do arquivo, como **"Enhanced"** ou 
**"Aprimorado"**, quando há aprimoramentos realizados com **IA** na imagem. O **Diem** oferece uma função para **remover 
automaticamente** esses sufixos adicionados, restaurando o nome original do arquivo sem essas modificações.
