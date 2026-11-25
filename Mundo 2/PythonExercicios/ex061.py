
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

contador = 0
termo = p

print('Os 10 primeiros termos da PA são:')

while contador < 10:
  print(termo, end=' -> ' if contador < 9 else '\n')
  termo += r
  contador += 1
