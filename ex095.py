jogador = dict()
jogadores = list()

while True:
    total = 0
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input(f'quantas partidas {jogador["nome"]} jogou?: '))
    jogador['gols'] = []
    for i in range(partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}: ')))
        total += jogador['gols'][i]
    jogador['total'] = total
    jogadores.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [ S / N ]: ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=-' * 30)
print(f'{'cod':<3} {'nome':<9} {'gols':^3} {'total':>7}')
print('-' * 40)

for i in range(len(jogadores)):
    print(f"{i + 1:<3} {jogadores[i]['nome']:<9} {' - '.join(map(str, jogadores[i]['gols'])):^3} {jogadores[i]['total']:>7}")

while True:
    try:
        
        print('-' * 40)
        dados = int(input('Mostrar dados de qual jogador?: (999 interrompe) '))
        if dados == 999:
            break
        elif 1 <= dados <= len(jogadores):
            print(f'-- Levantamento do jogador {jogadores[dados - 1]['nome']}')
            if not jogadores[dados - 1]['gols']:
                print(f'O jogador {jogadores[dados - 1]['nome']} nao fez nenhum gol.')
            else:
                for index, gols in enumerate(jogadores[dados - 1]['gols'],start=1):
                    print(f'No jogo {index}, fez {gols} gols')
        else:
            print(f'Nao existe jogador com o codigo {dados}')
                
    except ValueError:
        print('Erro')
        