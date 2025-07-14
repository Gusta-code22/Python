def area(l, c):
    print(f'A Area de um  terreno de {l} X {c} é de {l*c}m')


print(f'Controle de terronos')
print('-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
