numero = int(input('digite um numero: '))
if numero % 2 != 0:
    print('é \033[31mIMPAR\033[m')
else:
    print('é \033[32mPAR\033[m')