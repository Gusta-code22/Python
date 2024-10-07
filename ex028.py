from random import randint
from time import sleep

c = {'l': '\033[m',
    'azul': '\033[36m',
    'verm': '\033[31m',
    'roxo': '\033[35m',
    'verde': '\033[32m'
     }

pensa_computador = randint(0,5)
print(f'\033[34mvou pensar em um numero de 0 a 5{c["l"]}')
pensa_humano = int(input(f'{c["azul"]}tente advinhar o numero que o Computador esta pensando:  {c["l"]}'))
print(f'{c["roxo"]}Analizando quem ganhou...\033[m')
sleep(2)
if pensa_humano == pensa_computador:
    print(f'{c["verde"]}VOCE ME GANHOU!!!{c['l']}')
else:
    print(f'{c["verm"]}O COMPUTADOR TE VENCEU!!{c["l"]}. estava pensando no numero {pensa_computador}')
