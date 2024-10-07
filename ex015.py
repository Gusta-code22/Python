c = {'l': '\033[m',
     'c': '\033[37m',
     'ver': '\033[31m',
     'v': '\033[32m',
     'r': '\033[35m'
     }

km = float(input(f'{c["ver"]}quantidade de km percorrido: {c["l"]}'))
dia = int(input(f'{c['r']}dias alugados: {c['l']}'))
# 60 reais por dia alugado
# 0.15 por km 
dindin = (km * 0.15) + (dia * 60)
print(f'de acordo com a quantidade de km rodados e de dias alugados, o total a ser pagado será de {c["v"]}{dindin:.2f}R${c["l"]}')