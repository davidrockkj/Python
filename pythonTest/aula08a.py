import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'
      .format(num, raiz))

print('A raiz de {} é igual a {} - arredondada pra cima'
      .format(num, math.ceil(raiz)))

print('A raiz de {} é igual a {} - arredondada pra baixo'
      .format(num, math.floor(raiz)))