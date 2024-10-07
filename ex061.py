print('-=-' * 10)
print('10 termos de uma PA')
print('-=-' * 10)

pt = int(input('Primeiro Termo: '))
ra = int(input('razao: '))
c = 0
pa = pt
while c < 10:
    print(f'{pa}',end=(' '))
    pa += ra
    print('->' if c < 9 else ' Fim.',end=(' '))
    c += 1
