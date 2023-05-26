# Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
#     1. Dia = 17
#     2. Mes = Mar
#     3. Ano = 1978
#     4. Você nasceu no dia 17 de Mar de 1978. Correto?

dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mês do seu nascimento (3 primeiras letras)? ')
ano = input('Qual o ano de seu nascimento? ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano + '. Correto?')