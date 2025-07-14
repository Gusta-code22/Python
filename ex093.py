jogador = dict()
try:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['gols'] = []
    jogador['tot'] = 0

    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(partidas):
        jogador['gols'].append(int(input(f'Quantos Gols na Partida {i + 1}: ')))
        jogador['tot'] += jogador['gols'][i]
    print('-=' * 30)
    # método 1
    print(jogador)
    print('-=' * 30)
    #metodo 2
    for k, v in jogador.items():
        print(f'o campo {k} tem valor {v}')

    print('-=' * 30)
    print(f'O jogador {jogador['nome']} jogou {partidas} Partidas')
    for i, v in enumerate(jogador['gols']):
        print(f'    -> Na partida {i}, fez {v} gols')
    print(f'Fez um total de {jogador["tot"]} gols')
except ValueError:
    print(f'Dados errados; tente novamente')