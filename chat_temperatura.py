# Python - Chatboot para responder questões do meu portifólio de skils
import os
import time
from requests import get

# chave da api para consulta
API_KEY = "21c151cef324aa5da381fddbb22e397c"

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Este é o link do meu GitHub:https://github.com/Gustavo-H-Martins{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Muito simples, basta seguir o link:https://www.linkedin.com/in/gustavo-henrique-lopes-martins-361789192/ {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Você me encontra no e-mail:gustavojoana10@gmail.com estarei disponível!{os.linesep}')    

    else:
        print("""
        No momento estou em desenvolvimento, 
        portanto ainda não tenho mais opções de respostas.
        """)    


def start():
    # Apresentar o chatbot
    # Definir horário e printar saudação inicial.

    agora = time.strftime("%H:%M:%S", time.localtime()) 
    if int(int(agora[0:2])) < 12:
        print('Olá, bom dia!')
    elif int(agora[0:2]) >= 12 | int(agora[0:2]) < 18:
        print('Olá, boa Tarde!')
    elif int(agora[0:2]) > 18:
        print('Olá, boa noite!')
    
    print(f'Bem vindo autochat - Gustavo Martins LM Tech {os.linesep}')

    # Pedir o nome
    nome = input(f'Por gentileza, digite seu nome: ')
    localidade = input(f'Por favor informe a sua localidade atual, só o nome da cidade mesmo :D ')
    # Oferecer um menu de opções
    contador = 0
    get_temperatura(local = localidade, usuario=nome)
    print("O que gostaria de saber hoje? ")
    while True:
        
        if contador == 0:
            
            resposta = input(
                f"""
                {os.linesep}[1] - Como acesso o seu Github? 
                {os.linesep}[2] - Como acesso o seu LinkedIn? 
                {os.linesep}[3] - Como entro em contato com você?
                """)
            
            # Processar a resposta enviada
            processar_resposta(resposta, nome)
        else :
            continuar = input(f"""Gostaria de continuar esta conversa por aqui? 
            {os.linesep}[1] - Sim
            {os.linesep}[2] - Não 
            {os.linesep} """)
            if continuar == '1':
                contador = 0
            else:
                print(f"""
                {os.linesep}
                {os.linesep}
                {os.linesep}
                {os.linesep} Obrigado pelo seu momento! 
                {os.linesep} Para mais informações me mande um e-mail : gustavojoana10@gmail.com
                {os.linesep} Será um prazer te responder! 
                {os.linesep}""")

        contador += 1 

def get_temperatura(latitude:str = '', longitude:str = '', local:str='', usuario:str=''):
    link = f'https://api.openweathermap.org/data/2.5/weather?'#lat={lat}&lon={lon}&appid={API_KEY}&lang=pt_br'
    params = {
        'lat' : latitude,
        'lon' : longitude,
        'appid':API_KEY,
        'lang':'pt_br',
        'q': local
    }
    # 400,401,404 Não Funcionou
    try: 
        requisicao = get(link, params=params)
        # Observe que ele irá retornar um dicionaário com outros dicionário e listas dentro
        """print(requisicao.json())"""

        # Primeiro Passo - Capturar somente a temperatura
        # Segundo Passo - Capturar o clima
        # Converter a temperatura para graus celsius, pois ela vem em Kelvin por padrão
        # Converter o clima para Português do Brasil
        # Vamos armazenar o Json em uma variável chamada requisicao_dic
        requisicao_dic = requisicao.json()
        # Vamos armazenar o clima em uma variavel chamada descrição
        # Observe que temos uma lista dentro do dicionário...e Essa lista só tem um único item, então pegaremos o índice 0 (zero)
        descricao = requisicao_dic['weather'][0]['description']
        # Vamos armazenar a temperatura em uma variavel chamada descrição
        # Observe que a temperatura está dentro de um dicionario, chamado main
        temperatura = requisicao_dic['main']['temp'] - 273.15
        temp_max = requisicao_dic['main']['temp_max'] - 273.15
        temp_min = requisicao_dic['main']['temp_min'] - 273.15
        umidade = requisicao_dic['main']['humidity']
        # Apenas arredondando a temperatura
        # Inserindo o simbolo de ºC
        print (f"""
        {os.linesep}Olá {usuario}
        {os.linesep}O tempo em {requisicao_dic['name']} é : {descricao} 
        {os.linesep}Temperatura de {round(temperatura,2)}ºC 
        {os.linesep}Máxima de {round(temp_max,2)}ºC, Mínima de {round(temp_min,2)}ºC
        {os.linesep}Mmidade relativa do ar em {umidade}%""")
    except Exception as e:
        print(f"Não encontrado informação para o local solicitado, deu erro em : {e}")
        pass
if __name__ =='__main__':
    start()