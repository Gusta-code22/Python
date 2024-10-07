s1 = float(input('SEGMENTO 1: '))
s2 = float(input('SEGMENTO 2: '))
s3 = float(input('SEGMENTO 3: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print(f'os segmentos {s1}, {s2} e {s3}, Podem formar um triangulo ', end = (''))
    if s1 == s2 == s3:
        print(f'EQUILATERO.')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print(f'ISOCELES')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print(f'escaleno')
else:
    print(f'os segmentos acima nao podem formar um triangulo!.')
