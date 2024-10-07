print('-=-' * 10)
print('10 termos de uma PA')
print('-=-' * 10)

pt = int(input('Primeiro Termo: '))
ra = int(input('razao: '))
c = 0
termo = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(f'{termo}',end=(' -> '))
        termo += ra
        c += 1
    mais = int(input('Quantas mais? '))
print(f'Progressao finalizada com {total} termos mostrados')