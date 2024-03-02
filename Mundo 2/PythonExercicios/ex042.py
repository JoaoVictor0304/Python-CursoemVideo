'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: Todos os lados diferentes.'''

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('O triângulo formado é Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é Isósceles.')
    else:
        print('O triângulo formado é Escaleno.')
else:
    print('Não é possível formar um triângulo!')
