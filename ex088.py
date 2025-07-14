from random import randint

lista = list()
print('-' * 30)
print(f'{'Joga da Mega-Sena':^60}')
print('-' * 30)

jogo = int(input('Quantos jogos voce quer jogar?: '))

for i in range(jogo):
    lista.append([])
    for j in range(6):
        while True:
            num = randint(0,60)
            if not num in lista[i]:
                lista[i].append(num)
                break
        lista[i].sort()
print(f'\033[31m{f'Sorteado {jogo} jogos':-=-^30}')
for index,jogos in enumerate(lista, start=1):
    print(f'Jogo {index}: {jogos}')