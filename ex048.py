s = 0 
soma = 0
for cont in range(3, 501, 2): # decidindo apenas os impares
    if cont % 3 == 0: # definindo apenas os multiplos de 3
        s += cont
        soma += 1
total = soma #Atualizando o total depois do loop
print(f'a soma de todos os {total} valores solicitados é {s}')   
