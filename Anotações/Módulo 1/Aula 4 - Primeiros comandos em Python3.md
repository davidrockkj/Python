## Aula 4 - Primeiros comandos em Python3

Os dados, se forem mensagem, possuem delimitadores. No Python, esses demilitadores são aspas simples ou duplas: **‘Olá, Mundo!’** ou **“Olá, Mundo!”.**

Todos os Comandos, em Python3, são funções, precisam vir dentro de parênteses: **(‘Olá, Mundo!’).**

A função de escrever na tela **print()** fica assim: **print(’Olá, Mundo!’)** → Olá, Mundo!

Caso eu queira apresentar o resultado dos números **7** e **4**: **print(7+4)** → 11

**print(’7’+’4’)** → 74 (Pois o computador entende como: me mostre 7 e depois me mostre 4)

Ou seja, quando adicionamos **aspas**, o computador entende que aqui é uma mensagem que deve ser retornada. Caso eu deseje juntar mensagens, incluo o caractere **+** ou **,** entre as mensagens.

*Obs.: o **+** funciona quando queremos **mensagem + mensagem**. Quando queremos **mensagem + número**, usamos a vírgula **,***

- Variáveis
    - nome = ‘Guanabara’
    - idade = 25
    - peso = 75.8
- Apresentando resultados
    - **print(nome , idade , peso)** → Guanabara 25 75.8

- Variáveis recebendo valores do input
    - nome = input(”Qual é o seu nome? ”)
        - Juvenal
    - idade = input(”Qual é a sua idade? ”)
        - 22
    - peso = input(”Qual é o seu peso? ”)
        - 44.5
- Apresentando resultados
    - **print(nome, idade, peso)** → Juvenal 22 44.5

### Criando scripts

- Cria uma pasta para os scripts
- File > New file
- Digita o script
    - nome = input(’Qual é o seu nome? ‘)
    - idade = input(’Qual é a sua idade? ‘)
    - peso = input(’Qual é o seu peso? ‘)
    - print(nome, idade, peso)
- Salva o script na pasta
- Run > Run Module (F5)

O modo interativo do IDLE serve para testes. Quando eu quero criar um programa, vou para o Module.