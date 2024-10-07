from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade_atual = ano_atual - ano_nascimento
print(f'o atleta que nasceu em {ano_nascimento} tem {idade_atual} anos.')
if idade_atual < 9:
    print(f'Atleta MIRIM.')
elif idade_atual <= 14:
    print(f'Atleta INFANTIL')
elif idade_atual <= 19:
    print(f'Atleta JÚNIOR')
elif idade_atual <= 25:
    print('Atleta SÉNIOR')
else:
    print(f'Atleta MASTER')
