# Exibe uma linha de separação usando um padrão repetido
print('-=-' * 20)

# Centraliza o texto "Banco" em um espaço de 60 caracteres
print(f'{"Banco":^60}')

# Exibe outra linha de separação
print('-=-' * 20)

# Inicializa as variáveis que contarão as cédulas de cada valor
tot50 = tot20 = tot10 = tot1 = 0

# Solicita ao usuário o valor que ele deseja sacar e converte para inteiro (sem casas decimais)
valor = int(input('Quantos R$ você quer sacar?: '))

# Inicia o loop principal do programa
while True:
    # Conta quantas cédulas de R$50 podem ser usadas e subtrai do valor total
    while valor >= 50:
        tot50 += 1
        valor -= 50
    
    # Conta quantas cédulas de R$20 podem ser usadas e subtrai do valor total
    while valor >= 20:
        tot20 += 1
        valor -= 20
    
    # Conta quantas cédulas de R$10 podem ser usadas e subtrai do valor total
    while valor >= 10:
        tot10 += 1
        valor -= 10
    
    # Conta quantas cédulas de R$1 podem ser usadas e subtrai do valor total
    while valor >= 1:
        tot1 += 1
        valor -= 1
    
    # Sai do loop, pois o valor restante já foi totalmente processado
    break

# Exibe a quantidade de cédulas necessárias para o saque, divididas por valor
print(f'Total de cédulas:')
print(f'{tot50} cédula(s) de R$50')
print(f'{tot20} cédula(s) de R$20')
print(f'{tot10} cédula(s) de R$10')
print(f'{tot1} cédula(s) de R$1')

# Mensagem de finalização do programa
print('Programa Finalizado! Volte sempre!')
