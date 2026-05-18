
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

i = 0
valor = 0

while i < 10:

  if i == 0:
    print(p)
    i += 1
    valor = p
  else:
    valor += r
    i += 1
    print(valor)
