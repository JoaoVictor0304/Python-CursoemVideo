'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')'''


from math import hypot

oposto = float(input('Digite o cateto oposto do triangulo retangulo: '))
adjacente = float(input('Digite o cateto adjacente do triangulo retangulo: '))

print(f'A hypotenusa do triangulo retangulo é {hypot(oposto, adjacente):.2f}')
