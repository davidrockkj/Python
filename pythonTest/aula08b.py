from math import sqrt
# Fazendo a importação assim, eu não preciso colocar
# math. antes da função

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'
      .format(num, raiz))