# Chatbot em Python para responder perguntas do portfólio de habilidades

Este é um chatbot em Python que responde a algumas perguntas sobre meu portfólio de habilidades. Ele apresenta um menu de opções e permite que o usuário faça uma seleção, que é processada pelo bot para fornecer uma resposta adequada.

## Como Usar

1. Clone este repositório usando `git clone https://github.com/Gustavo-H-Martins/PrevisaoTempo`.
2. #### Configurando o ambiente virtual com Pipenv
    1. Instale o Pipenv: `pip install pipenv`
    2. Crie um novo ambiente virtual: `pipenv install`
    3. Ative o ambiente virtual: `pipenv shell`
    4. Instale as dependências do projeto: `pipenv install --dev`

    #### Ativando o ambiente virtual com Pipenv
    Para ativar o ambiente virtual criado com Pipenv, execute o seguinte comando:
    `pipenv shell`
3. Execute o arquivo `chat_temperatura.py`.
4. Digite o nome e a localidade do usuário.
5. Selecione uma opção no menu e veja a resposta do bot.

## Recursos

Este chatbot usa a API do OpenWeatherMap para obter informações sobre a temperatura e as condições climáticas da localidade fornecida pelo usuário. Ele também usa a biblioteca `requests` do Python para fazer as solicitações de API.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.