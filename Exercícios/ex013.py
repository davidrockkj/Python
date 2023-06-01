# Módulo 3

# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento

s = float(input('Qual é o seu salário? '))

print('Você recebeu um aumento de 15%! \n Seu novo'
      ' salário será de R${:.2f}' .format(s*1.15))