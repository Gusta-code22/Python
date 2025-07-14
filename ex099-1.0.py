def maior(* num):
    c = 0
    tam = len(num)
    print(f'-=' * 20)
    if not num:
        maior = 0
        tam = 0
    else:
        for valor in num:
            print(f'{valor}' , end= ' ')
            if c == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
            c += 1
    print(f'Foram digitados {tam} valores')
    print(f'O maior valor foi {maior}')

maior(5, 6, 7, 8)
maior(5, 3, 1, 2, 6)
maior()