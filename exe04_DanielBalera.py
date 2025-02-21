"""
Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. 
Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
Em seguida, pergunte se ele quer convidar outra pessoa.
Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
"""

confirmacao = 's'
i = 0
while confirmacao == 's':
    nome = input('Insira o nome do convidado para a festa: ')
    print('{} foi adicionado(a) com sucesso no convite!'.format(nome))
    i = i + 1
    confirmacao = input('Deseja adicionar mais um convidado? ("s"/"n") ')

print('{} pessoas foram convidadas para a festa.'.format(i))

print('Daniel Balera')