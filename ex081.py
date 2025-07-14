numeros = list()

while True:
    resp = ' '
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    while resp not in 'SN':
        resp = str(input('Deseja continuar:? [ S / N ]')).upper().strip()
    if resp == 'N':
        break
print(f'Na lista {' - '.join(map(str, numeros))}:')
lista_decrescente = numeros.copy()
lista_decrescente.sort(reverse=True)
print(f'temos {len(numeros)} elementos')
print(f'Em ordem decrecente {' - '.join(map(str, lista_decrescente))}')

if numeros.count(5) >= 1:
    print(f'Na lista temos o 5 e se aparece {numeros.count(5)} vezes nas posicoes',end = ' ')
    posicoes = list()
    for index, num in enumerate(numeros):
        if num == 5:
            posicoes.append(index)
    print(f'{' - '.join(map(str, posicoes))}')
else:
    print('Nao temos 5 na lista ')
