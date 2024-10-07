# Solicita ao usuário quantos termos da sequência de Fibonacci ele deseja mostrar
numero = int(input('quantos termos queres mostrar? '))

# Inicializa o contador e os primeiros dois números da sequência
c = 0
f = 0      # Primeiro número da sequência
f2 = 1     # Segundo número da sequência
n = 0      # Variável para armazenar o próximo número da sequência

# Imprime os dois primeiros números
print(f, end=(' -> '))
print(f2, end=(' ->' ))

# Loop para gerar os próximos termos da sequência
while c < numero - 2:  # O loop continua até atingir o número desejado de termos
    n = f + f2        # Calcula o próximo número como a soma dos dois anteriores
    f = f2           # Atualiza f para o valor atual de f2 (avança para o próximo)
    f2 = n           # Atualiza f2 para o novo número calculado
    print(n, end=(' -> '))  # Imprime o próximo número

    c += 1           # Incrementa o contador para controlar o número de termos gerados

# Imprime "fim" ao final da sequência
print('FIM')
