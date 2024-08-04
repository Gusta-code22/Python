import math
from datetime import date
from time import sleep
import random

while True:
    print('Menu de operacoes')
    print('1/adicao')
    print('2/subtracao')
    print('3/multiplicacao')
    print('4/divisao')
    print('5/raiz')
    print('6/potencia')
    print('7/quebrar numero')
    print('8/hipotenusa')
    print('9/cateto,seno...')
    print('10/calcular desconto')
    print('11/calcular aumento')
    print('12/Converter Real em Dolár')
    print('13/tabuada')
    print('14/Converter °C em °F ')
    print('15/verificar se é par ou impar')
    print('16/verificar se o ano é bissexto')
    print('17/ Verificar a aréa de formas geometricas')
    print('18/verificar se é palíndromo')
    print('19/verificar o primeiro e ultimo nome.')
    print('20/calcular fatorial.')
    print('21/gerar um numero aleatorio')
    print('0/Sair.')

    try:
        operacao = int(input('digite um numero correspondente ao que voce deseja: '))
        if operacao == 1:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            soma = n + n2
            print(f'{n} + {n2} = {soma}')
            sleep(3)

        elif operacao == 2:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            subtracao = n - n2
            print(f'{n} - {n2} = {subtracao}')
            sleep(3)

        elif operacao == 3:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            multiplicacao = n * n2
            print(f'{n} X {n2} = {multiplicacao}')
            sleep(3)

        elif operacao == 4:
            n = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            if n2 == 0:
                print('erro. 0 nao é uma entrada valida.')
                sleep(3)
            else:
                divisao = n / n2
                print(f'{n} ÷ {n2} = {divisao}')
                sleep(3)

        elif operacao == 5:
            n = float(input('Primeiro valor: '))
            if operacao < 0:
                print('erro. nao existe raiz quadrada negativa')
                sleep(3)
            else:
                raiz = math.sqrt(n)
                print(f'√{raiz}')
                sleep(3)


        elif operacao == 6:
            n = float(input('primeiro valor: '))
            n2 = float(input('Segundo valor: '))
            potencia = math.pow(n, n2)
            print(f'{n} ^ {n2} = {potencia}')
            sleep(3)

        elif operacao == 7:
            n = float(input('Primeiro valor: '))
            quebrar = math.trunc(n)
            decimal = n - quebrar
            print(f'numero quebrado = {n}\nnumero decimal = {decimal}')
            sleep(3)

        elif operacao == 8:
            ca = float(input('Cateto adjacente: '))
            co = float(input('Cateto oposto: '))
            hipotenusa = math.hypot(ca, co)
            print(f'hipotenusa = {hipotenusa:.2f}')
            sleep(3)

        elif operacao == 9:
            angulo = float(input('Ângulo: '))
            anguloradian = math.radians(angulo)
            seno = math.sin(anguloradian)
            tangente = math.tan(anguloradian)
            cosseno = math.cos(anguloradian)
            print(f'Cosseno = {cosseno}.\nSeno = {seno}.\nTangente = {tangente}.')
            sleep(3)

        elif operacao == 10:
            n = float(input('Valor inicial: '))
            desconto = float(input('porcetagem do desconto:% '))
            novo_n = n - (n * desconto / 100)
            print(f'com o desconto fica {novo_n:.2f}')
            sleep(3)

        elif operacao == 11:
            n = float(input('Valor inicial: '))
            aumento = float(input('porcentagem do aumento: % '))
            novo_n = n + (n * aumento / 100)
            print(f'com o aumento fica {novo_n:.2f}')
            sleep(3)

        elif operacao == 12:
            real = float(input('quantidade em reais: R$ '))
            dólar = real * 5.62
            print(f'{real:.2f}R$ sao {dólar:.2f}US')
            sleep(3)

        elif operacao == 13:
            n = float(input('Digite o numero que voce quer a tabela: '))
            a = n * 1
            b = n * 2
            c = n * 3
            d = n * 4
            e = n * 5
            f = n * 6
            g = n * 7
            h = n * 8
            i = n * 9
            j = n * 10
            print(
                f'{n} X 1 = {a}\n{n} X 2 = {b}\n{n} X 3 = {c}\n{n} X 4 = {d}\n{n} X 5 = {e}\n{n} X 6 = {f}\n{n} X 7 = {g}\n{n} X 8 = {h}\n{n} X 9 = {i}\n{n} X 10 = {j}')
            sleep(5)

        elif operacao == 14:
            celsius = float(input('Digite a temperatura em °C: '))
            fharei = celsius * 1.8 + 32
            print(f'{celsius:.2f}°C em °F fica {fharei:.2f}°F')
            sleep(3)

        elif operacao == 15:
            numero = float(input('Digite o numero: '))
            if numero % 2 == 0:
                print(f'o numero {numero} é PAR!!')
            else:
                print(f'o numero {numero} é IMPAR!!')
            sleep(5)

        elif operacao == 16:
            ano = int(input('Digite o ano ou digite 0 para verificar o ano atual: '))
            if ano == 0:
                ano = date.today().year
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                print(f'o ano {ano} é bissexto')
            else:
                print(f'o ano {ano} nao é bissexto')
            sleep(5)

        elif operacao == 17:
            print(f'menu de forma geometricas')
            print('1/Circulo')
            print('2/triângulo')
            print('3/retângulo')
            forma = int(input('digite a operacao desejada: '))
            if forma == 1:
                raio = float(input('digite o raio do Circulo: '))
                area = 3.14 * (raio ** 2)
                print(f'a area do circulo cujo raio é {raio} é de {area}m²')
            elif forma == 2:
                base = float(input('Base do triângulo: '))
                altura = float(input('Altura do triângulo: '))
                area = (base * altura) / 2
                print(f'a area do triângulo cuja base é {base} e altura é {altura} é de {area}m²')
            elif forma == 3:
                altura = float(input('Digite a altura do Retângulo: '))
                largura = float(input('Digite a largura do retângulo: '))
                area = altura * largura
                print(f'a aréa do retângulo cuja altura é {altura} e largura é {largura} é de {area}m²')
            else:
                print('erro. coloque numeros de 1 a 3.')
            sleep(7)

        elif operacao == 18:
            palavra = str(input('Digite uma palavra: ')).replace(' ', '').lower()
            if palavra == palavra[::-1]:
                print(f'a palavra {palavra} é Palídromo(igual de tráz para frente.)')
            else:
                print(f'a palavra {palavra} nao é Palíndromo.')
            sleep(6)

        elif operacao == 19:
            nome = str(input('Digite seu nome completo: ')).strip().title()
            print(f'seu primeiro nome é {(nome.split()[0])}')
            print(f'seu ultimo nome é {(nome.split()[-1])}')
            sleep(7)

        elif operacao == 20:
            numero = int(input('Diga um numero inteiro para ver seu fatorial: '))
            if numero < 0:
                print('erro. nao existe numero fatorial negativo!')
            else:
                fatorial = math.factorial(numero)
                print(f'o numero {numero} fatorial fica {fatorial}')
            sleep(7)

        elif operacao == 21:
            n1 = int(input('digite o numero minimo: '))
            n2 = int(input('digite o numero máximo: '))
            numero_aleatorio = random.randint(n1, n2)
            print(f'o numero aleatorio entre {n1} e {n2} é {numero_aleatorio}')
            sleep(5)

        elif operacao == 0:
            print('Saindo...')
            sleep(4)
            break

        else:
            print('erro. coloque uma entrada de 0 a 25')


    except ValueError:
        print('erro')
