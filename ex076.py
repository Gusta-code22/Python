print('-' * 50)
print(f'{'Listagem de precos': ^50}')
print('-' * 50)
produtoss = (
    ('Lapis', 1.50),
    ('Caneta', 2.00),
    ('Caderno', 45.00 )
)
produtos = ('cADERNO', 70, 'OPS',90)
# for i in range(0,len(produtos),2):
#     print(f'{produtos[i]:.<40} R${produtos[i + 1]:>7.2f}')
# print('-' * 50)

for nome,preco in produtoss:
    print(f'{nome:.<40} R$ {preco:>7.2f}')

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<40}', end=' ')
    else:
        print(f'{produtos[posicao]:>7.2f}')