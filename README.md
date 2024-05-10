# The Voice

O **The Voice** é um projeto que utiliza reconhecimento de voz e conversão de texto em fala para interações por voz.

## Descrição

Este projeto tem como objetivo criar um sistema de reconhecimento de voz que captura a entrada de áudio do usuário, transcreve a fala em texto, processa a entrada de texto usando um modelo de linguagem natural (GPT da OpenAI) e, em seguida, converte a resposta em áudio para reprodução.

## Funcionalidades

- Gravação de áudio
- Reconhecimento de voz
- Conversão de texto para fala
- Interação por voz

## Como Usar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/diegolim4/the_voice.git
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o aplicativo:**

    ```bash
    frask run
    ```

4. **Testar o aplicativo em seu navegador (get):**

    ```
    http://localhost:5000/api/about
    ```

5. **Endpoint para capturar a voz (post):**

    ```
    http://localhost:5000/api/import_voice
    ```

## Tecnologias Utilizadas

- Python
- Flask
- PyAudio
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- GPT (OpenAI's Generative Pre-trained Transformer)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.
