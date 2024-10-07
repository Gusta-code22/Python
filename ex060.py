from time import sleep

numero = int(input('Digite um número: '))


# Curiosidade para o número 52
if numero == 52:
    print(f'Aqui vai uma curiosidade. O fatorial de 52 é a quantidade que se pode embaralhar o baralho.')
    sleep(2)

# Resolvendo casos especiais
if numero < 0:
    print('Erro. nao existe Fatorial de numeros negativos.')
elif numero == 0:
    print('O fatorial de 0 é 1')
elif numero == 1:
    print(f'o Fatorial de 1 é 1, pois 1 X 1 é = 1')
else:
    # Cálculo do fatorial para números maiores que 1
    inicio = numero
    fatorial = numero

    while inicio != 1:
        inicio -= 1
        fatorial *= inicio

    # Construção da sequência de multiplicação
    sequencia = ' X '.join(str(i) for i in range(numero, 0, -1))
    
    # Exibição do resultado final
    print(f'{numero}! = {sequencia} = {fatorial}')
