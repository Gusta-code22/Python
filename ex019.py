from random import choice
from time import sleep

aluno1 = str(input('Primeiro aluno: ')).capitalize()
aluno2 = str(input('Segundo aluno: ')).capitalize()
aluno3 = str(input('Terceiro aluno: ')).capitalize()
aluno4 = str(input('Quarto aluno: ')).capitalize()
lista = [aluno1, aluno2, aluno3, aluno4]
print('\033[36mescolhendo...\033[m')
sleep(2)
print(f'o aluno escolhido foi \033[1;32m{(choice(lista))}\033[m')
