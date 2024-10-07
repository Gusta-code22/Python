from time import sleep

opcao = 0
print('-=-' * 10)
pri_valor = float(input('Primeiro Valor: '))
seg_valor = float(input('Segundo valor: '))
print('-=-' * 10)
    
while opcao != 7:

    
    print('-=-' * 10)
    print('[ 1 ] Soma')
    print('[ 2 ] Subtrair')
    print('[ 3 ] Multiplicaçao')
    print('[ 4 ] Divisao')
    print('[ 5 ] Maior')
    print('[ 6 ] Novos numeros')
    print('[ 7 ] Sair do programa')
    opcao = int(input('Sua opcao: '))
    print('-=-' * 10)
    
    if opcao == 1:
        soma = pri_valor + seg_valor
        print(f'A soma de {pri_valor} + {seg_valor} = {soma:.2f}')
    elif opcao == 2:
        subtrair = pri_valor - seg_valor 
        print(f'{pri_valor} - {seg_valor} = {subtrair:.2f}')
    elif opcao == 3:
        multiplicacao = pri_valor * seg_valor
        print(f'{pri_valor} X {seg_valor} = {multiplicacao:.2f}')

    elif opcao == 4:

        if seg_valor == 0:

            print('Erro. o divisor nao pode ser 0.')
        else:
            divisao = pri_valor / seg_valor
            print(f'{pri_valor} dividido por {seg_valor} = {divisao:.2f}')

    elif opcao == 5:
        maior = pri_valor
        if seg_valor > pri_valor:
            maior = seg_valor
        print(f'Entre {pri_valor} e {seg_valor} o maior é {maior}')
    elif opcao == 6:
        pri_valor = float(input('Primeiro Valor: '))
        seg_valor = float(input('Segundo valor: '))
    elif opcao == 7:
        print('Saindo...')
    else:
        print(f'Erro. por favor insira a opcao de 1 a 7')
    sleep(2)
print('programa encerrado.')