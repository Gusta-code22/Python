valor_casa = float(input('valor da casa: '))
salario = float(input('seu salário: '))
quantos_anos = int(input('quantos anos voce pretende pagar essa casa? '))
prestacao_mensal = (valor_casa / quantos_anos) / 12
print(f'Para financiar uma casa de R${valor_casa} em {quantos_anos} anos terá que pagar R${prestacao_mensal:.2f} por mês.')
if prestacao_mensal > (salario * 30 / 100):
    print(f'Seu empréstimo foi \033[31mnegado!\033[m')
else:
    print(f'seu empréstimo foi \033[32mAceito!\033[m')