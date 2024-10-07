def calculadarora_tabuada():
    print('-=-' * 10)

    print(f'Calculadora interativa.')

    print('-=-' * 10)

    c = n = 0
    
    while True:
        try:
            n = int(input('Um numero para ver sua tabuada: '))
            print('-=-' * 10)
            if n < 0:
                break
            for i in range(1,11):
                print(f'{n} X {i} = {n * i}')

            print('-=-' * 10)
        except ValueError:
            print('Erro. insira algo valido')
    print(f'Programa Tabuada Encerrado!!')
calculadarora_tabuada()