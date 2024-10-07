nota1 = float(input('digite a nota do aluno: '))
nota2 = float(input('digite a segunda nota: '))
m = (nota1 + nota2) / 2
if m >= 6:
    print(f'a media do aluno é \033[32m {m}\033[m')
    print(f'Parabens, voce passou\033[32m {m}\033[m!!')
else:
    print(f'a média do aluno é \033[31m{m}\033[m')
    print(f'esta reprovado, \033[31m{m}\033[m!!')
print(f'\033[1;37mtenha bons estudos!!\033[m')
