num = list()

for i in range(5):
    valor = int(input('Digite um valor: '))
    if not num or valor >= num[-1]:
        print('Valor adicionado no final da lista')
        num.append(valor)
    elif valor <= num[0]:
        num.insert(0, valor)
        print('Valor adicionado na posicao 0')
    else:
        for pos in range(len(num)):
            if valor <= num[pos]:
                num.insert(pos,valor)
                print(f'Valor adicionado na posicao {pos}')
                break
    print(f'{' - '.join(map(str,num))}')                
