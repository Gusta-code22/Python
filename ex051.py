print('=' * 10)
print('10 PRIMEIROS TERMOS DA PA')
print('=' * 10)

primeiro_t = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

decimo = primeiro_t + (10 - 1) * razao

for c in range(primeiro_t, decimo + razao, razao):
    print(f'{c}', end = (' -> '))
    