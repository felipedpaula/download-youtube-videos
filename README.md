## Visão Geral do Programa:

O programa é uma aplicação de desktop desenvolvida em Python com interface gráfica usando a biblioteca tkinter. Ele permite aos usuários baixar vídeos do YouTube fornecendo a URL do vídeo desejado e escolhendo uma opção de qualidade de vídeo para download.

## Configuração do Ambiente Virtual e Instalação de Dependências

**1. Instale o pacote python3.8-venv usando o comando:**
```shell
sudo apt install python3.8-venv
```

**2. Navegue até o diretório onde o programa está localizado e crie um ambiente virtual usando o comando:**
```shell
python3 -m venv venv
```

**3. Ative o ambiente virtual utilizando o comando adequado ao seu sistema operacional:**
```shell
source venv/bin/activate
```

**4. Com o ambiente virtual ativado, instale a biblioteca pytube e tkinter usando o pip:**
```shell
pip install pytube
pip install tkinter
```

## Executando o Programa:
Após configurar o ambiente virtual e instalar as dependências necessárias, você pode executar o programa seguindo estes passos:

Certifique-se de que o ambiente virtual esteja ativado.
Execute o programa Python usando o seguinte comando:

```shell
python3 download_youtube.py
```

## Explicação das Importações:

As importações import tkinter as tk e from pytube import YouTube são utilizadas para acessar funcionalidades específicas das bibliotecas Tkinter e Pytube.

- **Tkinter:**
    - A importação `import tkinter as tk` permite o acesso às funcionalidades da biblioteca `Tkinter`, que é uma biblioteca gráfica padrão do Python utilizada para criar interfaces gráficas de usuário (GUI). O alias `tk` é comumente utilizado para encurtar o nome da biblioteca e facilitar sua referência. No contexto deste programa, a biblioteca `Tkinter` é utilizada para criar uma interface gráfica onde o usuário pode interagir para inserir a URL de um vídeo do YouTube e realizar o download desse vídeo.
- **Pytube:**
    - A importação `from pytube import YouTube` permite o acesso à classe `YouTube` da biblioteca `Pytube`. Essa classe fornece métodos para interagir com a API do YouTube e realizar operações como baixar vídeos, obter informações sobre vídeos, extrair metadados, entre outros. No contexto deste programa, a biblioteca `Pytube` é utilizada para baixar vídeos do YouTube com base na URL fornecida pelo usuário.

## Função pesquisar_video():

Esta função é responsável por buscar e exibir as opções de stream disponíveis para download de um vídeo do YouTube, com base na URL fornecida pelo usuário.

- **Funcionamento:**
  - A função obtém a URL do vídeo inserida pelo usuário a partir do campo de entrada na interface gráfica.
  - Utilizando a biblioteca Pytube, a função cria uma instância da classe `YouTube` com a URL fornecida, permitindo assim o acesso às informações e opções do vídeo.
  - As opções de stream disponíveis para download são obtidas a partir da atribuição da lista de streams do vídeo à variável global `streams`.
  - Para cada opção de stream disponível, a função gera uma string formatada contendo o índice da opção e as informações da stream (resolução, formato, tipo de arquivo, etc.).
  - Essas strings formatadas são então atribuídas à variável `options`.
  - Por fim, a função atualiza os rótulos na interface gráfica para exibir as opções de stream disponíveis para o usuário, utilizando a variável `options` para isso.

Essa função é crucial para permitir que o usuário escolha a opção de stream desejada antes de iniciar o processo de download do vídeo do YouTube.

## Função download_video():

Esta função é responsável por iniciar o processo de download do vídeo do YouTube, com base na opção de stream escolhida pelo usuário.

- **Funcionamento:**
  - A função obtém o número da opção de stream escolhida pelo usuário a partir do campo de entrada na interface gráfica.
  - Utilizando essa opção, a função acessa a lista global `streams`, que contém as opções de stream disponíveis para download.
  - Em um bloco `try-except`, a função tenta realizar o download do vídeo utilizando a opção de stream selecionada. Se ocorrer algum erro durante o processo de download, ele será capturado pelo bloco `except`.
  - Se o download for bem-sucedido, a função cria o caminho do arquivo de vídeo resultante utilizando o título do vídeo e o salva no diretório 'videos'. Em seguida, uma mensagem de sucesso é exibida na interface gráfica, indicando o caminho do arquivo de vídeo salvo.
  - Caso ocorra algum erro durante o processo de download, uma mensagem de erro é exibida na interface gráfica, informando ao usuário sobre o problema encontrado.

Essa função desempenha um papel crucial no processo de download do vídeo do YouTube e fornece feedback ao usuário sobre o resultado da operação.

## Função criar_interface():

Esta função é responsável por criar a interface gráfica para o aplicativo de download de vídeos do YouTube.

- **Funcionamento:**
  - A função cria a janela principal do aplicativo utilizando a classe `Tk` da biblioteca Tkinter e define o título da janela como "Baixar Vídeo do YouTube".
  - Em seguida, a função cria um rótulo (`Label`) para instruir o usuário a inserir a URL do vídeo do YouTube.
  - Um campo de entrada (`Entry`) é criado para que o usuário possa inserir a URL do vídeo.
  - Um botão (`Button`) com o texto "Pesquisar" é criado e associado à função `pesquisar_video()`. Este botão permite que o usuário pesquise as opções de stream disponíveis para o vídeo.
  - Um rótulo vazio (`Label`) é criado para exibir as opções de stream disponíveis após a pesquisa.
  - Outro rótulo é criado para instruir o usuário a escolher uma opção de stream digitando o número correspondente.
  - Um segundo campo de entrada é criado para que o usuário possa inserir o número da opção de stream desejada.
  - Um botão com o texto "Baixar Vídeo" é criado e associado à função `download_video()`. Este botão inicia o processo de download do vídeo selecionado.
  - Por fim, um rótulo vazio é criado para exibir feedback ao usuário, como mensagens de sucesso ou erro durante o processo de download.

Essa função é crucial para criar uma interface amigável e intuitiva para os usuários interagirem com o aplicativo de download de vídeos do YouTube.

## Função main():

Esta função é o ponto de entrada principal do programa. Ela controla a interação com o usuário, permite que o usuário escolha entre converter uma imagem específica ou todas as imagens em uma pasta e direciona o fluxo de execução do programa com base na escolha do usuário.

- **Funcionamento:**
  - A função inicia solicitando ao usuário que escolha entre duas opções: converter uma imagem específica (digitando '1') ou todas as imagens na pasta (digitando '2'). Isso é feito usando a função `input()`.
  - Se o usuário escolher converter uma imagem específica (opção '1'), o programa solicita ao usuário que insira o nome da imagem, incluindo a extensão do arquivo. Em seguida, verifica se o arquivo de imagem especificado existe no diretório 'toConvert'. Se não existir, exibe uma mensagem de erro e retorna.
  - Em seguida, o programa solicita ao usuário que selecione o formato para a conversão da imagem, apresentando uma lista de opções numeradas ('1' para PNG, '2' para JPG e '3' para WEBP'). O usuário fornece o número correspondente ao formato desejado.
  - O programa utiliza um dicionário `format_dict` para mapear os números de escolha do formato para os formatos de saída correspondentes ('PNG', 'JPEG' e 'WEBP').
  - Se o formato escolhido pelo usuário estiver presente no dicionário `format_dict`, o programa determina o caminho de saída para o arquivo convertido com base no nome da imagem de entrada e no formato de saída escolhido. Em seguida, chama a função `convert_image()` para realizar a conversão da imagem especificada.
  - Se o usuário escolher converter todas as imagens na pasta (opção '2'), o programa exibe uma mensagem indicando que todas as imagens da pasta 'toConvert' serão convertidas. Em seguida, o programa solicita ao usuário que selecione o formato para a conversão de todas as imagens, seguindo o mesmo processo descrito acima.
  - Se o usuário inserir uma opção inválida que não seja '1' ou '2', o programa exibe uma mensagem de erro pedindo ao usuário que escolha entre as opções válidas.

Essa função coordena o fluxo de execução do programa, permitindo que o usuário interaja com ele e escolha as operações desejadas de forma intuitiva. 
