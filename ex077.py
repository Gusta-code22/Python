palavras_comuns = (
    "gafanhotoo", 
    "maninho", 
    "tamo", 
    "junto",  
    "Python", 
    "projeto", 
    "Streamlit", 
    "Minecraft", 
    "Fortnite", 
    "código", 
    "peça", 
    "flauta", 
    "produtos", 
    "redes"
)
for palavra in palavras_comuns:
    print(f'na palavra {palavra.upper()} temos',end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')
    print('')

    