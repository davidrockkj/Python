# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ela

algo = input('Digite algo: ')
print(type(algo), algo.isnumeric(), algo.isalpha(), algo.isascii(),
      algo.islower())
