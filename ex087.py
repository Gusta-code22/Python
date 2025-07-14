matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 15)
soma_pares = soma_terceira =  soma_2_linha = maior =0
for linha in range(3):
    for coluna in range(3):
        if linha == 1:
            soma_2_linha += matriz[linha][1]
        if coluna == 2:
            soma_terceira += matriz[linha][coluna]
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        for index,num in enumerate(matriz[1]):
            if index == 0 or num > maior:
                maior = num
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira}')
print(f'A soma dos valores da segunda linha é {soma_2_linha}')
print(f'O maior valor da segunda linha é {maior}')
                