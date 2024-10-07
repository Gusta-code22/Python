# importar as bibliotecas.
from random import randint
from time import sleep

# menu interativo
print('-=-' * 10)
print(f'PAR OU íMPAR.')
print('-=-' * 10)

# contadores.
vitorias = 0

# repeticao
while True:
    try:
        opcao = ' '
        # perguntas.

        valor_player = int(input('Diga o valor: '))

        while opcao not in 'PI':
            opcao = str(input('Par ou Ímpar? [ P / I ]: ')).strip().upper()[0]

        # jogada do computador

        valor_pc = randint(0, 1000)

        # jogada final
        valor_final = valor_pc + valor_player

        # verificando oque for
        if valor_final % 2 == 0:
            rodada = 'Par'
        else:
            rodada = 'ÍMPAR'
            
        # mensagem inicial
        print('-' * 20)
        print(f'Voce jogou {valor_player} e o pc jogou {valor_pc}. Total de {valor_final}, Deu {rodada}')
        print('-' * 20)
        # verificaçao do player.

        if (rodada == 'Par' and opcao == 'P') or (rodada == 'ÍMPAR' and opcao == 'I'):
            print(f'Voce ganhou')
            vitorias += 1
            print(f'Vamos jogar Novamente...')
            sleep(1)  
        else:
            print(f'Voce perdeu!!')
            break
    
    except ValueError:
        print(f'erro.insira uma entrada válida.')
print(f'-=-' * 20)
print(f'GAME OVER!!. voce me venceu {vitorias} vezes.')