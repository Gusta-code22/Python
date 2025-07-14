import datetime
pessoa = dict()




ano_atual = datetime.date.today().year

pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = ano_atual - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se nao possui): '))
pessoa['sexo'] = 'False'
while pessoa['sexo'] not in 'MF':
    pessoa['sexo'] = str(input('Sexo: [ M / F]: '))
if pessoa['ctps'] == 0:
    print('-=' * 30)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor de {v}')
        
else:
    
    if pessoa['sexo'] == 'M':
        tempo_contribuicao_minimo = 35
    else:
        tempo_contribuicao_minimo = 30
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('Salário: '))
    # a idade que ele comecou a trabalhar mais a tempo minimo
    pessoa['aposentadoria'] = (ano_atual - pessoa['contratacao']) + tempo_contribuicao_minimo
    pessoa['ano_aposentadoira'] = pessoa['contratacao'] + 35
    
    print('-=' * 30)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor de {v}')
        