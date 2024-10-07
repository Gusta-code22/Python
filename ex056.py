mulher_abaixo_20 = 0
homem_mais_velho = 0 
juncao_idade = 0
nome_homem_velho = ''

for i in range(1,5):
    print(f'-----{i} Pessoa-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    juncao_idade += idade #Somando as idades

    if sexo == 'F' and idade < 20: 
        mulher_abaixo_20 += 1
    
    if sexo == 'M':
        if i == 1:
            homem_mais_velho = idade 
            nome_homem_velho = nome
        if idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem_velho = nome
# Media de idade
media_idade = juncao_idade / 4

print(f'a media de idade do grupo é {media_idade:.2f} anos.')
if mulher_abaixo_20 == 0:
    print(f'no grupo nao ha mulheres')
else:
    print(f'no grupo á {mulher_abaixo_20} mulheres abaixo dos 20 anos.')

print(f'A idade do homem mais velho é {homem_mais_velho} cujo nome é {nome_homem_velho}')
