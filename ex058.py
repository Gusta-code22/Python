from random import randint

tot_tentativas = 0
jogada_pc = randint(0,1000)
acertou = False

print('Sou seu computador...')
print(f'irei pensa em um numero de 0 a 10')
print('Tente advinhar')

while not acertou:
    jogada = int(input('Seu palpite: '))
    tot_tentativas += 1

    if jogada == jogada_pc:
        acertou = True
    else:
        if jogada > jogada_pc:
            print('Menos...Tente mais uma vez')
        else:
            print('Mais...Tente mais uma vez')
            
print(f'Parabéns!!. Voce acertou com {tot_tentativas} tentativas!')
        