
n = int(input('Digite um número: '))

i = 0
penultimo = 1
ultimo = 2
soma = 3

while i < n:

  if i == 0:
    print(0)
    i += 1
  elif i == 1:
    print(1)
    i += 1
  elif i == 2:
    print (1)
    i += 1
  elif i == 3:
    print(2)
    i += 1
  else:
    print(soma)
    penultimo = ultimo
    ultimo = soma
    soma = penultimo + ultimo
    i += 1
