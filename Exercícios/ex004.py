#

msg = input('Digite alo: ')
print('Só tem espaços? ', msg.isspace())
print('É um número? ', msg.isnumeric())
print('É um alfabético? ', msg.isalpha())
print('É alfanumérico? ', msg.isalnum())
print('Está em maiúsculas? ', msg.isupper())
print('Está em minúsculas? ', msg.islower())
print('Está capitalizada? ', msg.istitle())