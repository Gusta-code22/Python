def maior(lst):
    print(f'Lista:')
    for num in lst:
        print(f'{num}', end=' ')
    print()
    for index, num in enumerate(lst):
        
        if index == 0:
            maior = num
        else:
            if num > maior:
                maior = num
    print(f'ao todo foram digitados {len(lst)} numeros')
    print(f'O maior numero digitado da lista é {maior}')

c = -1
numeros = list()
while True:
    c += 1
    numeros.append(int(input('Digite um numero: ')))
    print(f'Numero {numeros[c]} adicionado com sucesso')
    while True:
        resp = str(input('Deseja continuar?: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'Resposta inválida, digite apenas S ou N')
    if resp == 'N':
        break
maior(numeros)
