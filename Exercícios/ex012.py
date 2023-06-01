# Módulo 3

# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

p = float(input('Preço do produto: '))

print('Com 5% de desconto, o preço a pagar será de'
      ' R${:.2f}' .format(p*0.95))