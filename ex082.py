numeros = list()
numeros_pares = list()
numeros_impares = list()
while True:
    resp = ' '
    numeros.append(int(input('Digite um valor: ')))
    while resp not in 'SN': 
        resp = str(input('Deseja continuar? [ S / N ]')).upper().strip()
    if resp == 'N':
        break
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)
print(f'Os numeros digitados foram: {" - ".join(map(str, numeros))}')
print(f'Os numeros pares sao: {" - ".join(map(str, numeros_pares))}' if  numeros_pares else 'Nao foram digitados numeros pares')
print(f'Os numeros impares sao: {" - ".join(map(str, numeros_impares))}' if numeros_impares else 'Nao foram digitados numeros impares')