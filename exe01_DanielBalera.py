"""
Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado 
e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
"""

total = 0
numero = 0

while numero <= 50:
    numero = int(input('Insira o numero: '))
    total = total + numero

print('O total é ', total)
print('Daniel Balera')
