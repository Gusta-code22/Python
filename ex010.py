cor = {'verde': '\033[32m',
       'vermelho': '\033[31m',
       'limpa': '\033[m'
       }
c = float(input('quantos reais voce tem na sua carteira? R$ '))
# considerando dolár a 3,27 reais
dolar = c / 3.27
print(f'se voce tem {cor["vermelho"]}{c:.2f}R${cor["limpa"]} na sua carteira entao tem {cor["verde"]}{dolar:.2f}{cor["limpa"]} dolares.')
      
