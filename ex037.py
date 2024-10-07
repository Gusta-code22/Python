try:
    numero = int(input('digite um numero inteiro qualquer: '))
    print('Escolha uma das opçoes')
    print('1/ converter para Binário')
    print('2/ converter para Octal')
    print('3/ converter para hexadecimal')
    opcao = int(input('Sua opçao: '))
    if opcao == 1:
        numero_binário = bin(numero)[2:]
        print(f'o numero {numero} em binário fica \033[32m{numero_binário}\033[m')
    elif opcao == 2:
        numero_octal = oct(numero)[2:]
        print(f'o numero {numero} em octal fica \033[32m{numero_octal}\033[m')
    elif opcao == 3:
        numero_hexadecimal = hex(numero)[2:]
        print(f'o numero {numero} em Hexadecimal fica \033[32m{numero_hexadecimal}\033[m')

except ValueError:
    print('erro. insira um valor válido')