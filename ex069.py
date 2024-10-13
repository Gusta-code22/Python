# variaveis
maior_idade = 0
nome_maior = []
total_homens = 0
total_mulher = 0
total_mulher_menos_20 = 0
total_adolecentes = 0
# repeticao
while True:
    # Verificaçao de strings
    sexo = ' '
    opcao = ' '
    # mensagem inicial.
    print(f'-=-' * 10)
    print('Cadastro Pessoas')
    print('-=-' * 10)
    # perguntas

    idade = int(input('Idade: '))
    nome = str(input('Nome: '))

    # enquanto nao digitar uma opcao valida.
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 20)

    while opcao not in 'SN':
        opcao = str(input('Quer continuar?: [S/N]: ')).strip().upper()[0]
    # Flag.
    if opcao == 'N':
        break

    # Vendo os maiores de idades e quais nomes
    if idade >= 18:
        maior_idade += 1
        nome_maior.append(nome)
        
    # Quantos Homens cadrastrado
    if sexo == 'M':
        total_homens += 1
        if idade < 18:
            total_adolecentes += 1
    # quantas mulheres tem e quantas menos de 20 anos.
    if sexo == 'F':
        total_mulher += 1
        if idade <= 20:
            total_mulher_menos_20 += 1


print(f'Total de pessoas maior de idade: {maior_idade}, cujo nome é {nome_maior}')
print(f'Ao todo temos {total_homens} Homens acima de 18 e {total_adolecentes} Adolecentes(menores de 18)')
print(f'Ao todo temos {total_mulher} mulheres, sendo {total_mulher_menos_20} menos de 20 anos')