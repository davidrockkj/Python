# Módulo 3

# Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60/dia e
# R$0.15/km rodado.

km = float(input('Quantos Kms o carro percorreu? '))
dias = int(input('Quantos dias o carro ficou alugado? '))

print('O preço a pagar é de R${:.2f}'
      .format((km * 0.15) + (dias * 60)))