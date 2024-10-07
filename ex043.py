try: 
    peso_kg = float(input('diga seu peso: KG ').replace(',' , '.'))
    altura_metro = float(input('diga sua altura em metros: M ').replace(',' , '.'))
    imc = peso_kg / (altura_metro ** 2)
    print(f'o IMC dessa pessoa é {imc:.1f}')
    if imc < 18.5:
        print(f'o paciente esta \033[35mABAIXO DO PESO\033[m')
    elif imc > 18.5 and imc <= 24.9:
        print(f'\033[32mPESO NORMAL\033[m')
    elif imc > 25 and imc <= 29.9:
        print(f'\033[36mSOBREPESO.\033[m')
    elif imc > 30 and imc <= 34.9:
        print('\033[34mObesidade Grau I\033[m')
    elif imc > 35 and imc <= 40:
        print('\033[33mObesidade Grau II\033[m')
    elif imc > 40:
        print('\033[2;31mObesidade Grau III (ou Mórbida)\033[m')
except WindowsError:
    print(f'por favor. caso tenha colocado sua altura com uma ", "coloque com um "."')