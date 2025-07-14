expressao = str(input('Digite a expressão: '))
parenteses = list()

for simbolo in expressao:
    if simbolo == '(':
        parenteses.append(simbolo)
    elif simbolo == ')':
        if parenteses:
            parenteses.pop()
        else:
            print('Expressao inválida')
            break
else:
    if len(parenteses) == 0:
        print('Expressao válida')
    else:
        print('Expressao inválida')
