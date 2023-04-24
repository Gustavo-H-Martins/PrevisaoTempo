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
3. Execute o arquivo [`chat_temperatura.py`](./chat_temperatura.py).
4. Digite o nome e a localidade do usuário para exemplos tem o arquivo das [capitais](./capitais.csv).
5. Selecione uma opção no menu e veja a resposta do bot.
6. Para brincar e treinar use o [notebook - PrevisãoTempo](./PrevisaoTempo.ipynb)

## Recursos

Este chatbot usa a API do [OpenWeatherMap](https://openweathermap.org/) para obter informações sobre a temperatura e as condições climáticas da localidade fornecida pelo usuário. Ele também usa a biblioteca `requests` do Python para fazer as solicitações de API.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [`LICENSE`](./LICENCE) para obter mais informações.


## Créditos
Este projeto foi criado com vídeos do canal do [Jefferson Navarausckas - Nerd dos Dados](https://www.youtube.com/@nerddosdados)
[Como obter a PREVISÃO DO TEMPO com Python](https://www.youtube.com/watch?v=A6Nv3oY5lYc)
[Como criar um ChatBot inteligente com Python estilo ChatGPT](https://www.youtube.com/watch?v=UvaUdZBLo9Y)