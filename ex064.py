n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        c += 1
        soma += n
print(f'voce digitou {c} numeros e a soma deles é {soma}')