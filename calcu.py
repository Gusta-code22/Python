from time import sleep
while True:
    print('menu de operaçaos')
    print('1/Soma')
    print('2/subtraçao')
    print('3/multiplicaçao')
    print('4/divisao')
    print('5/Sair.')

    try:
        resultado = float(input('digite o numero para operaçao desejada: '))
        if resultado == 1:
            n = float(input('primeiro valor: '))
            n2 = float(input('segundo valor: '))
            soma = n + n2
            print(f'{n} + {n2} = {soma}')
            sleep(3)
        elif resultado == 2:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            subtraçao = n - n2
            print(f'{n} - {n2} = {subtraçao}')
            sleep(3)
        elif resultado == 3:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            multiplicaçao = n * n2
            print(f'{n} X {n2} = {multiplicaçao}')
            sleep(3)
        elif resultado == 4:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            if n2 == 0:
                print('0 é um valor invalido')
                print('tente novamente:')
            else:
                divisao = n / n2
                print(f'{n} ÷ {n2} = {divisao}')
            sleep(3)
        if resultado == 5:
            print('saindo...')
            sleep(3)
            break
    except ValueError:
        print('erro.por favor insira uma entrada correta.')