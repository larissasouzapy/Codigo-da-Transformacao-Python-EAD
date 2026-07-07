'''
Módulo 04 -  Estrutura de dados - Listas

Módulo 04 -  Estrutura de dados - Tuplas

'''
dias_semana = ( "Segunda","Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo" )

print ( "olá, seja bem vindo!" )
nome_usuário = input ("antes de começar, nos informe seu nome")

print(f'{nome_usuário}, qual dia da semana seria melhor para você') 

dia_escolhido =(input ("digite o dia que deseja: "))
# a variável  é: novo_dia

print(f'olá{nome_usuário}! você escolheu o dia {dia_escolhido}')

if dia_escolhido == "Domingo":
    print ("domingo é dia de macarronada.")

elif dia_escolhido == dias_semana:
    print ("Nada de especial hoje.")


# \n = pular de linha