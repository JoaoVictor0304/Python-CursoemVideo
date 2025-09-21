p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = p + (10 - 1) * r

for c in range(p, decimo + r, r):
  print(f'{c} ', end='-> ')
print('Acabou')
