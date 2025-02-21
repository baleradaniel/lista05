"""
Crie uma variável chamada “adivinha” e defina o valor como 50. 
Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
"""

adivinha = 50
palpite = int(input('Palpite: '))
i = 0

while palpite != 50:
    i = i + 1
    if palpite > 50:
        print('Muito alto!')
        palpite = int(input('Palpite: '))
    elif palpite < 50:
        print('Muito baixo!')
        palpite = int(input('Palpite: '))

print('Parabéns, você acertou o palpite em {} tentativas.'.format(i))

print('Daniel Balera')
