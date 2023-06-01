# Módulo 3

# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar

n1 = float(input('Quantos R$ você tem na sua carteira? '))
do = 3.27

print('Com R${} você pode comprar'
      ' ${:.2f}' .format(n1, n1/do))