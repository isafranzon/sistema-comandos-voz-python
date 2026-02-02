# Sistema de Reconhecimento de Voz em Python

Este projeto consiste em um sistema simples de reconhecimento de voz desenvolvido em Python, capaz de identificar comandos falados em português e executar ações no sistema operacional Windows, como abrir programas e sites.

O objetivo do projeto é praticar conceitos de automação, integração com o sistema operacional e uso de bibliotecas externas para reconhecimento de voz.

---

## Funcionalidades

O sistema reconhece comandos de voz e executa as seguintes ações:

- Abrir o navegador Google Chrome
- Abrir o Microsoft Excel
- Abrir o Microsoft Edge
- Abrir o ChatGPT no navegador
- Encerrar a execução do programa por comando de voz

Os comandos são reconhecidos em português (pt-BR) e podem ser facilmente estendidos para incluir novas aplicações.

---

## Tecnologias Utilizadas

- Python 3
- Biblioteca `speech_recognition`
- Biblioteca `webbrowser`
- Biblioteca `os`

---

## Funcionamento do Sistema

1. O programa ativa o microfone do usuário.
2. É realizado um ajuste automático para reduzir ruídos do ambiente.
3. A fala do usuário é capturada e convertida em texto utilizando o serviço de reconhecimento de voz do Google.
4. O texto reconhecido é analisado por palavras-chave.
5. Caso uma palavra-chave seja identificada, a ação correspondente é executada.

O sistema permanece em execução contínua até que o usuário diga um comando de encerramento.

---

## Ajustes e Correções Realizadas

Durante o desenvolvimento, alguns ajustes foram necessários:

- Padronização dos comandos para evitar falhas causadas por letras maiúsculas e minúsculas.
- Substituição da abertura direta de executáveis por URLs em casos mais confiáveis, como a abertura do ChatGPT via navegador.
- Correção de erros relacionados à identificação de caminhos de programas no Windows.
- Testes e validações dos comandos para garantir o funcionamento correto.

Esses ajustes contribuíram para tornar o sistema mais estável e funcional.

---

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/isafranzon/sistema-comandos-voz-python.git

2. Acesse a pasta do projeto:
    ```bash
   cd sistema-comandos-voz-python

3. Instale as dependências:
    ```bash
   pip install -r requirements.txt

4. Observação:
   No Windows, a biblioteca PyAudio pode exigir instalação adicional. Caso ocorra erro, utilize:

    ```bash
    pip install pipwin
    pipwin install pyaudio

5. Execute o arquivo principal:
   ```bash
   python sistema-comandos-voz-python.py

6. Fale um dos comandos configurados no sistema.

---

## Observações:

* O projeto foi desenvolvido e testado no sistema operacional Windows.

* É necessário que o microfone esteja funcionando corretamente.

* O reconhecimento de voz depende de conexão com a internet.


 ## Possíveis Melhorias Futuras:

* Adicionar novos comandos de voz

* Criar um menu de ajuda por voz

* Implementar suporte a outros idiomas

* Transformar o sistema em uma aplicação com interface gráfica
  

---


## Contexto do Projeto

Este projeto foi desenvolvido como parte do Bootcamp **Nexa - Machine Learning e GenAI na Prática**, oferecido pela **DIO (Digital Innovation One)**, sob orientação do professor **Dr. Diego Renan Bruno**.

O projeto tem caráter educacional e foi utilizado para aplicação prática dos conceitos estudados durante o bootcamp.


