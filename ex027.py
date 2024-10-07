from time import sleep

try:
    nome_completo = str(input('\033[36mdigite seu nome completo: \033[m')).title()
    print('\033[35mAnalizando seu nome...\033[m')
    sleep(1)
    print(f'seu primeiro nome é \033[32m{(nome_completo.split()[0])}\033[m')
    print(f'seu ultimo nome é \033[31m{(nome_completo.split()[-1])}\033[m')
except ValueError:
    print('ERRO.digite uma entrada valida')