# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome = input('Digite o seu nome: ')

# Posso fazer assim
# print('É um prazer te conhecer,', nome + '!')

# O recomendado é usar a saída formatada
print('É um prazer te conhecer, {}!' .format(nome))