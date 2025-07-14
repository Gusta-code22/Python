num = list()
while True:
    resp = ' '
    try:
        valor = int(input('Digite um numero: '))
    
        if valor not in num:
            print(f'Valor adicionado com sucesso')
            num.append(valor)
        else:
            print(f'Valor duplicado, nao vou adicionar. Tente novamente')
        while resp not in 'SN':
            resp = str(input('Deseja continuar? [ S / N ]: ')).upper()
        if resp == 'N':
            break
    except ValueError:
        print(f'Insira uma entrada numerica!!')
num.sort()
print(f'Voce digitou os numeros: {' - '.join(map(str,num))}')