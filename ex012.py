c = {'azul': '\033[36m',
     'verde': '\033[32m',
     'vermelho': '\033[31m',
     'roxo': '\033[35m',
     'limpa': '\033[m'
     }

preco = float(input(f'{c["roxo"]}preço do produto:R$ {c["limpa"]}'))
novo_preco = preco - (preco * 5 / 100)
print(f'o produto que custava {c["vermelho"]}{preco}R${c["limpa"]} depois do desconto de 5% vai custar {c["verde"]}{novo_preco:.2f}R${c["limpa"]}')