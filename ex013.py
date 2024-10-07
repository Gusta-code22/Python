c = {'l': '\033[m',
     'r': '\033[35m',
     've': '\033[31m',
     'v': '\033[32m', 
     }

salario = float(input(f'{c['r']}qual o salario do funcionario: {c['l']}'))
novo_salario = salario + (salario * 15 / 100)
print(f'o funcionario que recebia {c["ve"]}{salario}{c['l']} vai passar a receber {c["v"]}{novo_salario:.2f}{c['l']}')