try:
    print('-=-' * 20)
    print('\033[1;35mAnalizador de Triangulos\033[m')
    print('-=-' * 20)
    a = float(input('primeiro segmento: '))
    b = float(input('segundo segmento: '))
    c = float(input('terceiro segmento: '))
    if a + b > c and a + c > b and b + c > a:
        print(f'os segmentos {a} , {b} e {c} podem formar um triangulo.')
    else: 
        print(f'os segmentos {a} , {b} e {c} NAO podem formar um triangulo.')
except ValueError:
    print('\033[31mpor favor. informe valores corretos.\033[m')
