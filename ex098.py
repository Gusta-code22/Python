from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -14
            -4
            0
            
    if passo > 0:
        fim_ajustado = fim + 1
    else:
        fim_ajustado = fim - 1
    print('-=' * 20)

    print(f'Contagem de {inicio} ate {fim} de {abs(passo)} em {abs(passo)}')
    for i in range(inicio, fim_ajustado, passo):
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    


contador(1, 10, 1)
contador(10, 0, -2)
print(f'Agora é sua vez de personalizar')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)