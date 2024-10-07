from datetime import date

sexo = str(input('voce é do sexo masculino ou feminino?(responda com F/M): ')).lower().strip()
if sexo == 'f':
    print(f'Voce nao precisará se alistar.')
elif sexo == 'm':
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade_atual = ano_atual - ano_nascimento
    if idade_atual < 18:
        print(f'voce nasceu em {ano_nascimento} e ira fazer {idade_atual} anos em {ano_atual}')
        print(f'ainda falta {(18 - idade_atual)} anos para voce se alistar.')
        print(f'seu alistamento será em {ano_nascimento + 18}')

    elif idade_atual == 18:
        print(f'voce nasceu em {ano_nascimento}, tem 18 anos')
        print('VOCE TEM QUE SE ALISTAR IMEDIATAMENTE')

    else:
        print(f'voce nasceu em {ano_nascimento} e tem {idade_atual} anos')
        print(f'voce ja deveria ter se alistado a {(idade_atual - 18)} anos')
        print(f'seu alistamento foi em {(ano_nascimento + 18)}')
else:
    print(f'Entrada inválida. Por favor, responda com F ou M.')