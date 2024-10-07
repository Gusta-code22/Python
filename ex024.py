cidade = str(input('\033[34mem que cidade voce nasceu: \033[m')).strip().capitalize()
if cidade[:5] == 'Santo':
    print('sua cidade \033[32mcomeça\033[m com Santo.')
else:
    print('sua cidade \033[31mnao\033[m começa com Santo.')