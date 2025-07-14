from random import randint

n = tuple(randint(0,10) for _ in range(5))

print(f'Os numeros sorteados foram:',end=' ')
for num in n:
    print(num,end=' ')
print(f'\no Maior numero é {max(n)}')
print(f'O menor numero é {min(n)}')