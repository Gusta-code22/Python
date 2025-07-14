from random import randint
from time import sleep

def sorteia(numeros):
    for i in range(5):
        numeros.append(randint(0, 10))
    print(f'Sorteado 5 numeros: ',end='')
    for num in numeros:
        print(f'{num}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO')
    

def soma(numeros):
    soma_par = 0
    for num in numeros:
        if num % 2 == 0:
            soma_par += num
    print(f'Somando os valores pares de {numeros}, temos {soma_par}')


numeros = []

sorteia(numeros)
soma(numeros)
