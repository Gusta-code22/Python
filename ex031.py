from time import sleep

distancia = float(input('\033[36mQual é a distancia da viagem: \033[m'))
print(f'\033[34mvoce está prestes a iniciar um viagem de {distancia}KM\033[m')
print('\033[35mCalculando valor...\033[m')
sleep(1)
if distancia < 200:
    valor = distancia * 0.50
else:
    valor =  distancia * 0.45
print(f'o valor da viagem é \033[31mR${valor:.2f}\033[m')