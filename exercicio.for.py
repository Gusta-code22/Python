
quantidade = int(input('Quantos numero inserir: '))

numeros = []
soma = 0
for i in range(quantidade):
    n = int(input(f'{i + 1} Numero: '))
    numeros.append(n)
    soma += n

media = soma / quantidade
menor_numero = 0
quantidade_negativos = 0
quantidade_menor_10 = 0

for numero in numeros:
    if numero == 1:
        menor_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    if numero < 0:
        quantidade_negativos += 1
    if numero < 10:
        quantidade_menor_10 += 1

porcentagem_menor_10 = (quantidade_menor_10 / quantidade) * 100

print(f'a media dos numeros é {media:.2f}')
print(f'o menor numero é {menor_numero}')
print(f'há {quantidade_negativos} numeros negativos')
print(f'há {quantidade_menor_10} numeros menores que 10 e equivale {porcentagem_menor_10}% do total')
