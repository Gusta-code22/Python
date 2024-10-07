frase = str(input('digite uma frase: '))
frase_sem_espaco = frase.lower().replace(' ','')
invertido = ''


for i in range(len(frase_sem_espaco)-1 ,-1 ,-1):
    invertido += frase_sem_espaco[i]

print(f'A frase original é {frase}')
print(f'A frase invertida é: {invertido}')

if frase_sem_espaco == invertido:
    print(f'UAU! Temos um Palíndromo')
else:
    print(f'NAO é Palíndromo')

