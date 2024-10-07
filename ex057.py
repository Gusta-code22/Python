sexo = str(input('informe o Sexo [M/F]: ')).strip().upper()[0]
while sexo not in ['M','F']:
    print(f'Entrada Invalida. coloque apenas M(Msculino) ou F(Feminino)')
    sexo = str(input('informe o sexo novamente [M/F]: ')).strip().upper()[0]
print(f'Sucesso!. Sexo {sexo} cadastrado com sucesso.')

