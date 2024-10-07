tem = float(input('sua temperatura em °C '))
f = tem * 1.8 + 32
# if caso a temperatura for menor que 1 coloque em azul para simbolizar frio
if tem < 1:
    print('ta congelando ai')
    print(f'a temperatura \033[36m{tem}\033[m em Fahrenheit fica \033[32m{f:.1f}\033[m °F')
else:
    print(f'a temperatura {tem} em Fahrenheit fica \033[36m{f}\033[m')
