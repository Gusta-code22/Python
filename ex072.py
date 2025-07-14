numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", 
    "onze", "doze", "treze", "quatorze", "quinze", 
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    
    n = int(input('Digite um numero de zero a vinte: '))
    if n >= 0 and n <= 20:
        break
print(f'Voce digitou o Numero: {numeros_por_extenso[n]}')