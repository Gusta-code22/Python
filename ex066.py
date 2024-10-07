n = cont = soma = 0
lista = []
while True:
    try:
        n = int(input('Digite um numero: [999 para parar]: '))
        if n == 999:
            break
        soma += n
        lista.append(n)
        cont += 1
    except ValueError:
        print(f'Erro. digite uma entrada válida')
print(f'Foram digitados {cont} Numeros cujo eles sao {lista} e sua soma é {soma}')