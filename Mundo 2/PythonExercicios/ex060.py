
n = int(input('Digite um número inteiro não negativo: '))

while n < 0:
  n = int(input('Valor inválido. Digite um número inteiro não negativo: '))

resultado = 1
contador = n

print(f'{n}!=', end='')

while contador > 0:
  resultado *= contador
  print(contador, end='')
  if contador > 1:
    print('x', end='')
  contador -= 1

if n == 0:
  print(resultado)
else:
  print(f'={resultado}')
