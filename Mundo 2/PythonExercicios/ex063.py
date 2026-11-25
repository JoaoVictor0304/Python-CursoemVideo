
n = int(input('Quantos termos de Fibonacci você quer mostrar? '))

while n < 0:
  n = int(input('Digite uma quantidade maior ou igual a 0: '))

contador = 0
atual = 0
proximo = 1

if n == 0:
  print('Nenhum termo foi solicitado.')
else:
  print(f'Os {n} primeiros termos de Fibonacci são:')

  while contador < n:
    print(atual, end=' -> ' if contador < n - 1 else '\n')
    soma = atual + proximo
    atual = proximo
    proximo = soma
    contador += 1
