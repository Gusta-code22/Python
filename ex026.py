from time import sleep
frase = str(input('\033[35mdigite uma frase: \033[m')).strip().upper()
print('\033[36mAnalizando a frase...\033[m')
sleep(2)
print(f'a letra A aparece \033[31m{frase.count('A')}\033[m vezes na frase.')
print(f'a letra A aparece pela primeira vez na posiçao \033[32m{frase.find('A') + 1}\033[m')
print(f'a letra A aparece pela ultima vez na posiçao \033[34m{frase.rfind('A') + 1}\033[m')
