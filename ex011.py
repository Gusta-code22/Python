cor = {'limpa': '\033[m',
       'amarelo': '\033[34m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'roxo': '\033[35m',
       'azul': '\033[36m',
       }

l = float(input('largura da parede: '))
a = float(input('altura da parede: '))
area = l * a
tinta = area / 2
print(f'sua parede tem a dimensão de {cor["azul"]}{l}{cor["limpa"]} X {cor["roxo"]}{a}{cor["limpa"]} e sua aréa é de {cor["vermelho"]}{area}{'\033[m'}m '
      f'e vai precisar de {cor["amarelo"]}{tinta}l{cor["limpa"]} de tinta para pintar ')