from math import trunc

numero = float(input('\033[34mdigite um numero: \033[m'))
print(f'o valor digitado foi \033[32m{numero}\033[m e sua parcela quebrada fica \033[31m{(trunc(numero))}\033[m')
