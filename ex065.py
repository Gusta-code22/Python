c = n = soma = menor = maior = 0
resp = 'S'
while resp in 'sS':
    n = int(input('Digite um numero: '))
    resp = str(input('Quer continuar? [S/N]: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma / c
print(f'A quantidades de numeros digitados foi {c}, sua soma {soma} e sua media {media:.2f}')
print(f'O maior valor foi {maior} e o menor {menor}')