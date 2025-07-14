try:
    tupla = tuple(int(input('Digite um numero: ')) for _ in range(4))
    print(tupla)
    if 3 in tupla:
        print(f'O 3 se encontra na posiçao {tupla.index(3) + 1 }')
    else:
        print(f'O 3 nao está na Tupla')
    if 9 in tupla:
        print(f'O 9 aparece {tupla.count(9)} vezes')
    else:
        print(f'Nao existe o numero 9 nessa tupla')
    print(f'Os numeros pares sao: ',end=' ')
    for num in tupla:
        if num % 2 == 0:
            print(num,end=' ')
except ValueError:
    print(f'Erro, Insira algo válido')