'''
Módulo 04 -  Estrutura de dados - Listas

Módulo 04 -  Estrutura de dados - Tuplas

Módulo 04 -  Estrutura de dados -Dicionários
'''
print ("\Módulo 04 - Estruturas de dados - Dicioário \n ")

#tem q usar o if e o else nn precisa do elif
dias_semana = ( "Segunda","Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo" )

print ( "olá, seja bem vindo!" )


cardapio_semana = {
    "Segunda-feira": "Strogonoff",
    "Terça-feira" : "Pizza",
    "Quarta-feira":"Lasanha",
    "Quinta-feira": "Escondidinho",
    "Sexta-feira": "Carne a molho madeira ",
    "Sabádo": "Churrasco",
    "Domingo":"macarronada"
}
print ("\Módulo 04 - Estruturas de dados - Dicioário \n ")
print( '-' * 48)

nome_usuário = input ("antes de começar, nos informe seu nome")

dia_escolhido =(input ("digite o dia da semana para saber o menu: "))

if dia_escolhido in cardapio_semana:

    comida = cardapio_semana [dia_escolhido]

    print (f'no {dia_escolhido}, o dia é de comer:{comida}!')

else: 
    print ('Desculpe, não temos esse dia no nosso cardápio.')