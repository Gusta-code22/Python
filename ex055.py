maior = 0
menor = 0

for pesso in range(1,6):
    peso = float(input(f'Peso da {pesso}° pessoa: '))

    if pesso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior}KG.')
print(f'O menor peso lido foi {menor}')
