from datetime import date

ano_atual = date.today().year
cont_maior_idade = 0
cont_menor_idade = 0

for i in range(1,8):
    data = int(input(f'Ano de nascimento da {i} pessoa: '))
    idade = ano_atual - data
    if idade >= 21:
        cont_maior_idade += 1
    else:
        cont_menor_idade += 1
print(f'Entre os anos de nascimento fornecidos, {cont_maior_idade} pessoas são maiores de idade.')
print(f'E {cont_menor_idade} pessoas são menores de idade.')