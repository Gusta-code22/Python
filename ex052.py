contador = 0
n = int(input('Digite um numero inteiro: '))
for c in range(1, n + 1 ):
    if n % c == 0:
        contador += 1
        print(f'\033[32m{c}\033[m',end=(' '))
    else:
        print(f'\033[31m{c}\033[m', end = (' '))
if contador > 2:
    print(f'\no numero {n} é divisivel {contador} vezes\ne por isso ele NAO é primo.')
else:
    print(f'\no numero {n} foi divisivel apenas {contador} vezes e por isso ele é PRIMO.')
