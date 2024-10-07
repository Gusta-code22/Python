try:
    v1 = int(input('primeiro valor: '))
    v2 = int(input('segundo valor: '))
    v3 = int(input('terceiro valor: '))
    # calculando o maior
    maior = v1
    if v2 > v1 and v2 > v3:
        maior = v2
    if v3 > v2 and v3 > v1:
        maior = v3
    # calculando o menor
    menor = v1
    if v2 < v1 and v2 < v3:
        menor = v2
    if v3 < v2 and v3 < v1:
        menor = v3 
    print(f'o maior é {maior}\no menor é {menor}')
except ValueError:
    print(f'por favor coloque valores corretos.')