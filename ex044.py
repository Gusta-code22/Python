print('======LOJA RLG VARIEDADES======')
preco = float(input('Preço das compras: R$ ').replace(',', '.'))
print("""FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão 
[ 4 ] 3x ou mais no cartão""")
opcao = int(input('Digite sua opcao: '))
if opcao == 1:
    preco_novo = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai ficar por R${preco_novo:.2f} no final.')
elif opcao == 2:
    preco_novo = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai ficar por R${preco_novo}')
elif opcao == 3:
    print(f'sua compra de R${preco:.2f} em 2x, a parcela vai ficar de R${(preco / 2):.2f}')
elif opcao == 4:
    quantidade_parcela = int(input('Quantas parcelas? '))
    juros = (preco * 20 / 100)
    preco_final = preco + juros
    parcela = preco_final / quantidade_parcela
    print(f'Sua compra vai ser parcelada em {quantidade_parcela}X de R${(parcela):.2f} com juros.')
    print(f'Sua compra de {preco:.2f} vai ficar de R${preco_final:.2f}')
else:
    print(f'opcao de pagamento Inválida. Tente novamente.')
