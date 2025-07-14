lista = list()
posicao_maior = list()
posicao_menor = list()

for i in range(5):
    lista.append(int(input(f'Digite um numero na posicao {i + 1 }: ')))

lista_ordenada = lista.copy()
lista_ordenada.sort()
maior = max(lista)
menor = min(lista)

for index,numero in enumerate(lista, start= 1):
    if numero == maior:
        posicao_maior.append(index)
    if numero == menor:
        posicao_menor.append(index)

print(f'Voce digitou os valores {lista_ordenada}')
print(f'maior: {maior}, nas posicoes {' .. '.join(map(str,posicao_maior))}')
print(f'menor: {menor}, nas posicoes {' .. '.join(map(str, posicao_menor))}')
