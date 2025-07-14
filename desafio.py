from random import randint
from time import sleep

print(f'Escolha a dificuldade')
print(f'[ 1 ] Fácil.(Numero entre 1 a 50)')
print(f'[ 2 ] Médio.(Numero entre 1 a 100)')
print(f'[ 3 ] Dificil.(Numero entre 1 a 200 E apenas 10 chances)')
while True:
    dificuldade = 0
    while dificuldade not in [1, 2, 3]:
        dificuldade = int(input('Digite o Numero de acordo com a dificuldade desejada: '))
    break
if dificuldade == 1:
    x = 50
elif dificuldade == 2:
    x = 100
elif dificuldade == 3:
    x = 200
numero_secreto = randint(0, x)
print(f'o computador ira pensar em um numero de 0 a {x}\nTente Advinhar.')
chance = 0

tentativas = 0
acertou = False

while not acertou:
    if dificuldade == 3:
        chance += 1
        if chance == 10:
            break
    palpite = int(input(f'Seu palpite: '))
    tentativas += 1
    if palpite == numero_secreto:
        acertou = True
    elif palpite > numero_secreto:
        if chance < 9:
            print(f'Menos...\nTente novamente')
            sleep(1)
    elif palpite < numero_secreto:
        if chance < 9:
            print(f'Mais...\nTente novamente')
            sleep(1)
if dificuldade == 3 and chance < 10:
    print(f'Voce ganhou faltando {10 - chance} Chances!!. Parabéns')
    if tentativas > 0:
        print(f'Voce ganhou com {tentativas} Tentativas')
elif dificuldade == 3 and chance == 10:
    print(f'Suas chances acabaram...\nO numero secreto era {numero_secreto}')
else:
    print(f'Voce ganhou!! Parabéns')
    if tentativas > 0:
        print(f'Voce ganhou com {tentativas} Tentativas')
    else:
        print(f'UAU. Voce ganhou de primeira!!')
