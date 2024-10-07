from datetime import date

try:
    ano = int(input('digite o ano que quer analizar. Digite 0 para analizar o ano atual: '))
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'\033[32mo ano {ano} é bissexto!\033[m')
    else:
        print(f'\033[31mo ano {ano} nao é bissexto!!\033[m')
except ValueError:
    print('por favor. insira um ano valido')
