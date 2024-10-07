numeros = []

iteracao = int(input('Quantidade de iteraçoes: '))

for i in range(iteracao):
    n = int(input(f'{i + 1} Numero: '))
    numeros.append(n)

quantidade_mul_3 = 0
quantidade_pares = 0
soma_pares = 0
maior_numero = 0
divisiveis_3 = []

for numero in numeros:
    # verificando os pares e somando-o
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero

    # verificando o maior numero
    if numero == 1:
        maior_numero = numero
    if numero > maior_numero:
        maior_numero = numero

    # Verificando os multiplos de 3
    if numero % 3 == 0:
        quantidade_mul_3 += 1
        divisiveis_3.append(numero)

print(f'na lista há {quantidade_pares} e a soma deles é {soma_pares}')
print(f'na lista o maior numero é {maior_numero}')
print(f'na lista há {quantidade_mul_3} numeros multiplos de 3, que sao {divisiveis_3}')
