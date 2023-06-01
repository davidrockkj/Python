# Um professor quer sortear um dos quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

from random import randint

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

n = randint(1, 4)

# lista = [a1, a2, a3, a4]
# escolhido = random.choice(lista)
# -> guanabara

if n == 1:
    print('O aluno escolhido é {}' .format(a1))
if n == 2:
    print('O aluno escolhido é {}' .format(a2))
if n == 3:
    print('O aluno escolhido é {}' .format(a3))
if n == 4:
    print('O aluno escolhido é {}' .format(a3))
