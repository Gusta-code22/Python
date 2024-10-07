import math

s = float(input('\033[35mqual angulo voce deseja? \033[m'))
r = math.radians(s)
seno = math.sin(r)
cosseno = math.cos(r)
tangente = math.tan(r)
print(f'o ângulo \033[32m{s}\033[m tem o SENO de \033[31m{seno:.2f}\033[m')
print(f'o ângulo \033[32m{s}\033[m tem o COSSENO de \033[31m{cosseno:.2f}\033[m')
print(f'o ângulo \033[32m{s}\033[m tem o TANGENTE de \033[31m{tangente:.2f}\033[m')
