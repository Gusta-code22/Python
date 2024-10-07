try:
    salario = float(input('digite o valor do salario: '))
    if salario > 1250.00:
        novo_salario = salario + (salario * 10 / 100)
    if salario <= 1250.00 :
        novo_salario = salario + (salario * 15 / 100)
    print(f'quem ganhava {'\033[1;31m'}{salario:.2f}{'\033[m'} seu novo salario vai ser de \033[1;32m{novo_salario:.2f}\033[m')
except ValueError:
    print('erro.por favor informe um salario válido.')