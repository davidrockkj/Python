# Módulo 3

# Faça um programa que leia um número inteiro qualquer
# e mostre na tela sua tabuada

n1 = int(input('Tabuada do número: '))
i = 0

while i <= 10:
    print('{} x {:2} = {}' .format(n1, i, n1*i))
    i += 1