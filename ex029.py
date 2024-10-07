from time import sleep

c = {'limpa': '\033[m',
     "verde": '\033[32m',
     'vermelho': '\033[31m',
     "roxo": '\033[35m',
     'azul': '\033[34m'}


velocidade = int(input(f'{c["azul"]}velocidade atual do carro: {c["limpa"]}'))
if velocidade > 80:
    print(f'{c["vermelho"]}VOCE FOI MULTADO POR EXCESSO DE VELOCIDADE{c["limpa"]}')
    print(f'sua multa vai custar {c["vermelho"]}{((velocidade - 80) * 7):.2f}R${c["limpa"]}')
else: 
    print(f'{c["verde"]}voce nao foi multado.{c["limpa"]}')
if velocidade > 150:
    print(F'{c["vermelho"]} DIRIJA DEVAGAR!!{c["limpa"]}')
print(f'{c["azul"]}tenha um bom dia e dirija com cuidado :){c["limpa"]}')