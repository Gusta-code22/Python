from time import sleep

c = {'l': '\033[m',
     'verme': '\033[31m',
     'verde': '\033[32m',
     'azul': '\033[36m',
     'roxo': '\033[35m'}



nome = str(input('\033[34mdigite seu nome completo: \033[m')).strip()
nome_sem_espacos = nome.replace(' ', '')
nome_dividido = nome.split()
print('\033[36manalizando seu nome...\033[m')
sleep(2)
print(f'seu nome em maiúsculas fica {c["roxo"]}{(nome.upper())}{c["l"]}\nseu nome em minúsculas fica {c["azul"]}{(nome.lower())}{c['l']}\n'
      f'seu nome tem um total de {c["verde"]}{(len(nome_sem_espacos))}{c['l']} letras\nseu primeiro nome tem {c["verme"]}{(len(nome_dividido[0]))}{c["l"]} letras')