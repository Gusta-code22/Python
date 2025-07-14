lista = list()
pessoas = list()
while True:
    resp = ' '
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    pessoas.append(lista.copy())
    lista.clear()
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [ S / N ]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 30)
print(f'{'N.O':<5}{'Nome'}   {'média':>5}')
print('-'*20)
for index,pessoa in enumerate(pessoas, start = 1):
    media = (pessoa[1] + pessoa[2]) / 2
    print(f'{index:<5}{pessoa[0]}   {media:>5.2f}')
print('-'*20)

while True:
    try:
        num = int(input('Mostrar notas de qual Aluno? (999 interrompe): '))
        if num == 999:
            print('Finalizando Programa...')
            break
        elif 1 <= num <= len(pessoas):
            print(f'Notas de {pessoas[num-1][0]} sao {pessoas[num-1][1:]}')
            print('---' * 10)
        else:
            print('Numero Inválido, insira novamente')
    except ValueError:
        print(f'Erro')