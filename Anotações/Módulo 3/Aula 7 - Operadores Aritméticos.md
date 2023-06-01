# Operadores Aritméticos
ADIÇÃO -> +
SUBTRAÇÃO -> -
MULTIPLICAÇÃO -> *
DIVISÃO -> /
POTÊNCIA -> **
DIVISÃO INTEIRA -> //
RESTO DE DIVISÃO -> %

# Exemplos:
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2 *Dividir sem vírgula*
5 % 2 == 1 *O que sobra da divisão inteira*


**Obs.: 1 símbolo de igualdade '=' significa atrubuição**
*a = 12*
**Obs.: 2 símbolos de igualdade '==' significam igualdade**
*a + b == 36*

# Ordem de precedência
1 - ()
2 - **
3 - *, /, //, %
4 - +, -

*No Python, colchetes e chaves são para outras coisas.*

# Exemplos:
5 + 3 * 2
# 11 - valor correto (ordem de precedência)

3 * 5 + 4 ** 2
# 31 - valor correto (ordem de precedência)

3 * (5 + 4) ** 2
# 243 - valor correto (ordem de precedência)

- Raiz quadrada de um número:
81 ** (1/2)
# 9 - já que raiz quadrada é a mesma coisa que elevar um número a meio (0,5)

- Raiz cúbica de um número:
127 ** (1/3)
# 5.026525695313479







# Dicas do Python #1
- Consigo trabalhar com quantidade limitada, no print:

```py ex1
nome = input('Qual o seu nome? ')
print('Olá {:20}!' .format(nome))

# Olá David               !
```

```py ex2
nome = input('Qual o seu nome? ')
print('Olá {:>20}!'.format(nome))

# Olá                David!
```

```py ex3
nome = input('Qual o seu nome? ')
print('Olá {:^20}!'.format(nome))

# Olá        David        !
```

```py ex4
nome = input('Qual o seu nome? ')
print('Olá {:=^20}!'.format(nome))

# Olá =======David========!
```



# Dicas do Python #2
- Consigo calcular dentro do format:

```py
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale: {}' .format(n1+n2))

# A soma vale: x
```



# Dicas do Python #3
- Caso eu queira limitar as casas decimais de uma divisão:

```py
n1 = int(input('Um valor: '))
# 4
n2 = int(input('Outro valor: '))
# 3
print('O resultado é: {:.3f}' .format(n1/n2))

# O resultado é: 1.333
```



# Dicas do Python #4
- Caso não queira quebrar a linha usando 2 print:

```py
n1 = int(input('Um valor: '))
# 12
n2 = int(input('Outro valor: '))
# 4

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ')
print('Divisão inteira é {} e potência {}' .format(di, e))

# A soma é 16, o produto é 48 e a divisão é 3.000 Divisão inteira 3 e potência 20736
```



# Dicas do Python #5
- Caso queira quebrar a linha, basta adicionar \n:

```py
n1 = int(input('Um valor: '))
# 12
n2 = int(input('Outro valor: '))
# 4

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é \n {} e a divisão é \n {:.3f}' .format(s, m, d), end=' ')
print('Divisão inteira é {} e potência {}' .format(di, e))

# A soma é 16, o produto é
# 48 e a divisão é
# 3.000 Divisão inteira 3 e potência 20736
```

## pythonTest > aula07a ##