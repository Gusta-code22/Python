import random
from time import sleep

while True:
# escolha do computador :)
    lista = ['Pedra', 'Tesoura', 'Papel']
    computador = random.choice(lista)

# escolha do jogador :)
    print('''Sua opcoes: 
    [ 0 ] Pedra
    [ 1 ] Tesoura
    [ 2 ] Papel''')
    jogador = int(input('Qual a sua jogada?: '))
# transformando a escolha do usuario para uma string:

    opcoes = ['Pedra', 'Tesoura' , 'Papel']
    jogada_jogador = opcoes[jogador]

# menu interativo:
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURAA!!')
    print('-=-' * 10)
    print(f'o jogador escolheu \033[36m{jogada_jogador}\033[m')
    print(f'o computador escolheu \033[34m{computador}\033[m')
    print('-=-' * 10)
    # comparacoes
    if jogada_jogador == computador:
        print(f'\033[36mEMPATE\033[m')
    elif jogada_jogador == 'Pedra' and computador == 'Tesoura' or \
         jogada_jogador == 'Tesoura' and computador == 'Papel' or \
         jogada_jogador == 'Papel' and computador == 'Pedra':
        print('\033[32mO Jogador venceu\033[m')
    else:
        print('\033[31mO computador venceu.\033[m')
    sleep(4)
# Pedra ganha de Tesoura
# Tesoura ganha de Papel
# Papel ganha de Pedra
