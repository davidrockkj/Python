# Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela sua porção inteira
import math

n = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}'
      .format(n, math.trunc(n)))
