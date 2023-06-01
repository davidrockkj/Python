# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente
# desse ângulo
from math import radians, sinn, cos, tan

n = float(input('Digite um ângulo qualquer: '))
cos = cos(radians(n))
sen = sin(radians(n))
tan = tan(radians(n))

print('Levando {} como ângulo, temos: \n'
      '{} valor do cosseno\n{} valor do seno\n'
      '{} valor da tangente'
      .format(n, cos, sen, tan))