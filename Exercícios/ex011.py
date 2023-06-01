# Módulo 3

# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule sua área e a quantidade de
# tinta para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m²

l = float(input('Largura em metros: '))
h = float(input('Altura em metros: '))
a = l * h


print('A área é de {}m²' .format(a))
print('Serão necessários {} baldes de tinta'
      .format(a/2))