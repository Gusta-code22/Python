n = int(input('\033[31mdigite um numero de ate 4 digitos: \033[m'))

m = n // 1000
n1 = n % 1000

c = n1 // 100
n2 = n % 100

d = n2 // 10
n3 = n % 10

u = n3 // 1
print(f'\033[32mmilhar: \033[m{m}\n\033[33mcentena: \033[m{c}\n\033[34mdezena: \033[m{d}\n\033[35munidade: \033[m{u}')
