nome_completo = str(input('digite seu nome completo: ')).strip().title()
if 'Silva' in nome_completo:
    print('sem nome \033[32mTEM\033[m Silva.')
else:
    print('seu nome \033[31mNAO\033[m tem Silva.')