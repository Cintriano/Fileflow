
# Gerenciador de Fotos 📸

Este projeto foi criado para facilitar meu workflow de edição e gerenciamento de fotos, permitindo lidar com grandes volumes de arquivos em poucos segundos.

## ✨ Funcionalidades
-   **Renomear arquivos** automaticamente com base em metadados.
-   **Conversão de arquivos** para diferentes formatos.
-   **Registro das execuções** para rastreamento.
-   **Busca nos registros** para fácil recuperação de informações.

## 📂 Renomeação de Arquivos
O programa FileFlow renomeia os arquivos seguindo um padrão predefinido (**dd.mm.aaaa_XXXXX**), onde a data é extraída automaticamente dos metadados sempre que possível. Caso os metadados não estejam disponíveis, outras fontes de informação podem ser utilizadas. Se nenhuma informação de data for encontrada e eu também não souber essa informação, o arquivo será renomeado sem a data.

Para lidar com diferentes situações, o sistema considera três cenários possíveis:

### ✅ Melhor Caso (Metadados Preservados)
Esse caso se refere a arquivos que vem direetamente do dispositivo de origem, isso significa que todos os metadados estão preservados (como data, hora e dispositivo), permitindo uma renomeação precisa. Portanto o programa extrai os dados necessarios diretamente dos metadados e realiza a renomeação.

### 📑 Caso Médio (Nome do Arquivo)
Quando o arquivo não contém metadados suficientes para a renomeação ideal, o programa utiliza as informações presentes no próprio nome do arquivo (**20250217_82713**, por exemplo).

Nesse caso, ele extrai e limpa os dados relevantes do nome original e os utiliza para realizar a renomeação seguindo o padrão estabelecido.

### ❓ Pior Caso (Sem Informações Disponíveis)
Esse caso se aplica a arquivos que não possuem nenhuma informação de data disponível, seja nos metadados ou no nome do arquivo.

Como o programa FileFlow não tem dados suficientes para determinar uma data, ele segue um padrão específico para esses casos, utilizando um formato genérico, definido **IMG_94264**.

#### ❗Detalhes
Importante resaltar que o programa FileFlow tem a capacidade de diferenciar entre o melhor caso e caso medio, executando a melhor abordagem de acordo com a situação, porem para o pior caso os arquivos precisam ser isolados e executados separadamente.

Também é possível realizar **renomeações manuais**, permitindo que o usuário forneça uma data específica que será aplicada a todos os arquivos de imagem em uma pasta selecionada.

Essa funcionalidade é útil quando os metadados estão ausentes ou imprecisos, garantindo que os arquivos sejam organizados corretamente conforme a necessidade do usuário.

## 🔄 Conversão
Essa funcionalidade é responsável por realizar a **conversão de formatos de imagens**. Os formatos suportados para conversão são: CR2 (arquivos brutos da câmera)

-   **CR2**  → **JPG**
-   **CR2**  → **PNG**
-   **PNG** → **JPG**
-   **JPG** → **PNG**

Essa ferramenta torna o processo de adaptação de imagens para diferentes formatos rápido e simples, sem a necessidade de softwares adicionais, a execução é realizada em toda a pasta selecionada.

## 📜Registro das execuções
O programa FileFlow possui um sistema de criação de **logs**, que armazena informações sobre as operações realizadas em arquivos `.txt`. Esses registros são gerados para cada execução de **renomeação** e **conversão**.

Um exemplo de registro gerado após uma renomeação é o seguinte:

	02.02.2025/22:15:51/r/01.02.2025_55546.CR2/IMG_2496.CR2/Canon EOS REBEL T5i

As informações registradas incluem:

-   **Data** e **hora** da execução
-   **Tipo de execução** (renomeação ou conversão)
-   **Nome novo** e **nome antigo** do arquivo
-   **Dispositivo de origem**

Esses registros permitem um fácil rastreamento e consulta das ações realizadas no sistema, é gerado um arquivo para armazenar os registros a cada mês.

## 🔍Consulta dos registros
O programa FileFlow permite realizar **buscas nos registros de execução**, facilitando a recuperação de informações sobre operações anteriores. A busca é feita com base no **nome pós-execução** do arquivo, ou seja, o nome do arquivo após a renomeação ou conversão.

Ao buscar por um nome, o programa retorna a **linha correspondente** do registro, fornecendo todos os detalhes da execução, como data, hora, tipo de operação, nome antigo, nome novo e dispositivo de origem.

## ➕Funcionalidade extras
Uma funcionalidade extra do **FileFlow** é a capacidade de lidar com alterações no nome de arquivos feitas por programas de edição de imagens.

Por exemplo, programas como o **Adobe Lightroom** podem adicionar sufixos ao nome do arquivo, como **"Enhanced"** ou **"Aprimorado"**, quando há aprimoramentos realizados com **IA** na imagem. O **FileFlow** oferece uma função para **remover automaticamente** esses sufixos adicionados, restaurando o nome original do arquivo sem essas modificações.
