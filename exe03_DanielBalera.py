"""
Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
Depois que o loop for interrompido, exiba o total.
"""

total = 0
numero = int(input('Insira um numero: '))
total = total + numero
numero = int(input('Insira outro numero: '))
total = total + numero
sim = input('Deseja adicionar outro numero? ("s"/"n")')

while sim == 's':
    numero = int(input('Insira um numero: '))
    total = total + numero
    sim = input('Deseja adicionar outro numero?')

print(total)

print('Daniel Balera')