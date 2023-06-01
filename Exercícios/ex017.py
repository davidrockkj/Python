# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

# hi = math.hypot(co, ca) -> guanabara

print('O valor da hipotenusa é {}' .format(hi))