# Descrição: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
while True:
    aluno = dict()
    aluno['Nome'] = str(input('Nome: '))
    aluno['media'] = float(input('Média: '))
    print('=' * 20)
    if aluno['media'] >= 7.0:
        aluno['situacao'] = 'Aprovado'
    elif aluno['media'] >= 5.0:
        aluno['situacao'] = 'Recuperação'
    else:
        aluno['situacao'] = 'Reprovado'
    for keys, values in aluno.items():
        print(f'    - {keys}: {values}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [ S / N ]: ')).strip().upper()[0]
    if resp == 'N':
        break
