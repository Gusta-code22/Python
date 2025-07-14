cont = 0
times = (
    "Botafogo", 
    "Palmeiras", 
    "Flamengo", 
    "Fortaleza", 
    "Internacional", 
    "São Paulo", 
    "Corinthians", 
    "Bahia", 
    "Cruzeiro", 
    "Vasco da Gama", 
    "EC Vitória", 
    "Atlético-MG", 
    "Fluminense", 
    "Grêmio", 
    "Juventude", 
    "Bragantino", 
    "Athletico-PR", 
    "Criciúma", 
    "Atlético-GO", 
    "Cuiabá"
)

print(f'Times: {times}')
print('-=-' * 15)
print(f'Os 5 primeiros times: {times[:5]} ')
print('-=-' * 15)
print(f'Os 4 ultimos sao: {times[-4:]}')
print('-=-' * 15)
print(f'Times em ordem: {sorted(times)}')
print('-=-' * 15)
print(f'o Vasco da Gama esta na {times.index('Vasco da Gama') + 1} posicao')
print('-=-' * 15)