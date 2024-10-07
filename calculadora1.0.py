from time import sleep
while True:
    print('Menu de operacoes.')
    print('1/Soma')
    print('2/Subtracao')
    print('3/multiplicaçao')
    print('4/divisao')
    print('5/potência')
    print('6/raiz')
    print('7/sair')

    try:
        operacao = int(input('digite um numero de acordo com a operacao desejada: '))
        if operacao == 1:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            soma = n + n2
            print(f'{n} + {n2} = {soma}')
            sleep(3)

        elif operacao == 2:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            subtracao = n - n2
            print(f'{n} - {n2} = {subtracao}')
            sleep(3)

        elif operacao == 3:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            multiplicacao = n * n2
            print(f'{n} X {n2} = {multiplicacao}') 
            sleep(3)

        elif operacao == 4:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            if n2 == 0:
                print('0 nao é uma entrada válida.')
            else:
                divisao = n / n2
                print(f'{n} ÷ {n2} = {divisao}')
                sleep(3)
        elif operacao == 5:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            potencia = n ** n2
            print(f'{n} ^ {n2} = {potencia}')
            sleep(3)
        elif operacao == 6:
            n = float(input('Primeiro valor: '))
            if n < 0:
                print('erro. Raiz quadrada negativa nao é permitida')
            else:
                raiz = n ** (1/2)
                print(f'√{n} = {raiz}')
                sleep(3)
        elif operacao == 7:
            print('saindo..')
            sleep(3)
            break
        else:
            print('so é permitido numeros de 1 a 7')

    except ValueError:
        print('erro. por favor digite um valor correto.')