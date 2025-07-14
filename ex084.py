pessoas = list()
dados = list()
maior = menor = 0
while True:
    resp = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if not pessoas:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for peso in pessoas:
    if peso[1] == maior:
        print(f'{peso[0]} ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for peso in pessoas:
    if peso[1] == menor:
        print(f'{peso[0]} ', end='')
    