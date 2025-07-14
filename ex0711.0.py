print(f'-=-' * 20)
print(f'{'Banco':-^60}')
print(f'-=-' * 20)

valor = int(input('Digite o valor: R$ '))
total = valor
totced = 0
cedatual = 50
while True:
    if total >= cedatual:
        total -= cedatual
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} de {cedatual}R$')
        if cedatual == 50:
            cedatual = 20
        elif cedatual == 20:
            cedatual = 10
        elif cedatual == 10:
            cedatual = 1
        totced = 0
        if total == 0:
            break
print(f'Banco encerrado volte sempre')
        
        