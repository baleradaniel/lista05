"""
Escreva um programa que permaneça em laço lendo números inteiros. 
O laço termina quando for digitado 0 (zero).
Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
Ao final exiba a lista e a quantidade de elementos que ela contém.
"""
numeros = []
numero = int(input('Insira um numero: '))
numeros.append(numero)

while numero != 0:
    numero = int(input('Insira um numero: '))
    if numero in numeros:
        print('Número ja está incluso na lista.')
        numeros.append(numero)
        i = numeros.index(numero)
        numeros.pop(i)
    else:
        numeros.append(numero)
     
print(numeros)