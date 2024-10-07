import mtlibrary
ca = int(input('digite o cateto adjacente: '))
co = int(input('digite o cateto adjacente: '))
h = mtlibrary.hipotenusa(ca, co)
print(f'a hipotenusa de \033[1;31m{ca}\033[m e \033[1;32m{co}\033[m é \033[35m{h:.2f}\033[m')
