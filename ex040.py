nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'tirando {nota_1} e {nota_2}, a média fica {media:.1f}')
if media < 5.0:
    print(f'\033[31mREPROVADO\033[m')
elif media > 5.0 and media < 7.0:
    print(f'\033[34mRECUPERAÇÃO\033[m')
elif media >= 7.0:
    print(f'\033[32mAPROVADO\033[m')
