numero = [[], []]
for i in range(1, 8):
    while True:
        try:
            num = int(input(f'Digite o {i}º número: '))
            break
        except:
            print('Digite um número inteiro válido.')
    if num % 2 == 0:
        numero[0].append(num)
    else:
        numero[1].append(num)
print(f'\033[31mNumeros classificados:\033[m')
print(f'\033[35mOs números pares são: {sorted(numero[0])}\033[m')
print(f'\033[36mOs números ímpares são: {sorted(numero[1])}\033[m')
