from random import randint
from time import sleep

participantes = [
    {'Nome': 'Participante - 1', 'Dados': randint(1, 6)},
    {'Nome': 'Participante - 2', 'Dados': randint(1, 6)},
    {'Nome': 'Participante - 3', 'Dados': randint(1, 6)},
    {'Nome': 'Participante - 4', 'Dados': randint(1, 6)},
]
for pos, valor in enumerate(participantes, start= 1):
    print(f'{valor["Nome"]} tirou {valor['Dados']}.')
print('===' * 10)
ranking = sorted(participantes, key=lambda x: x['Dados'], reverse= True)

for index, valor in enumerate(ranking, start= 1):
    print(f'{index}° Lugar: {valor["Nome"]} com {valor["Dados"]}')
