s = 0
cont = 0
for contador in range(0,6):
    n = int(input(f'Digite o {contador} valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'a soma de todos os {cont} valores pares digitados é {s}')
