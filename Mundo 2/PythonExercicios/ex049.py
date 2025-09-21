v = int(input('Digite o número que deja saber a tabuada: '))

for c in range(0, 11):
  t = v * c
  print('{} x {}: {}'.format(v, c, t))
  