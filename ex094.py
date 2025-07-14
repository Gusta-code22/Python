galera = []
pessoa = dict()
soma = 0
while True:

    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M / F]: ')).upper().strip()
        if pessoa['sexo'] in 'MF':
            break
        print(f'Erro. insira apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Deseja continuar?: [S / N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'Erro, insira apenas S ou N')
    if resp == 'N':
        break
media = soma / len(galera)
print(f'Foi cadastrado {len(galera)} pessoas')
print(f'media de idade: {media:.2f}')
print(f'Mulheres: ', end=' ')
for pessoa in galera:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa['nome']}',end=' ')
print()
print(f'Pessoas com idade acima da media: ')
for pessoa in galera:
    if pessoa['idade'] > media:
        print('       ')
        for k , v in pessoa.items():
            print(f'{k} = { v} ;', end= '')
