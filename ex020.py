from random import shuffle
from time import sleep

p = str(input('primeiro aluno: ')).capitalize()
s = str(input('segundo aluno: ')).capitalize()
t = str(input('terceiro aluno: ')).capitalize()
q = str(input('quarto aluno: ')).capitalize()
lista = [p, s, t, q]
shuffle(lista)
print('\033[36membaralhando...\033[m')
sleep(2)
print(f'a ordem de apresetançao é \033[35m{lista}\033[m')
