# Menu inicial
print('-=-' * 20)
print('Loja RLG Variedades')
print('-=-' * 20)

# Contadores para armazenar valores
total = 0  # Total da compra
maiores_de_1000 = 0  # Contador para produtos acima de R$1000
mais_barato = 0  # Armazena o valor do produto mais barato
nome_barato = ''  # Armazena o nome do produto mais barato
c = 0  # Contador para saber se é o primeiro produto

# Início do loop principal
while True:
    c += 1  # Incrementa o contador de produtos
    nome = ' '  # Inicializa a variável nome
    resp = ' '  # Inicializa a variável resposta
    
    # Verificando se o nome do produto contém apenas letras (string)
    while not nome.isalpha():
        nome = str(input('Nome do Produto: ')).strip()

    # Solicita o valor do produto
    valor = float(input('Preço: R$'))

    # Verifica se a resposta é válida (S ou N)
    while resp not in ('S', 'N'):
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    # Soma o valor ao total da compra
    total += valor

    # Se o produto custar mais de R$1000, incrementa o contador
    if valor >= 1000:
        maiores_de_1000 += 1

    # Verifica se o produto é o mais barato
    if c == 1:  # Se for o primeiro produto, ele é o mais barato automaticamente
        mais_barato = valor
        nome_barato = nome
    elif valor < mais_barato:  # Se não for o primeiro, compara o valor
        mais_barato = valor
        nome_barato = nome

    # Se o usuário quiser parar (responder 'N'), o loop é interrompido
    if resp == 'N':
        break

# Exibição dos resultados
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O total da compra foi de R${total:.2f}')  # Exibe o total formatado com 2 casas decimais
print(f'Temos {maiores_de_1000} produto(s) custando mais de R$1000')  # Exibe a quantidade de produtos acima de R$1000
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato:.2f}')  # Exibe o nome e valor do produto mais barato
