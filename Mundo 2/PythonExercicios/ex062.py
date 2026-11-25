
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

termo = p
total = 0
mais = 10

print('Os 10 primeiros termos da PA são:')

while mais != 0:
  contador = 0

  while contador < mais:
    print(termo, end=' -> ' if contador < mais - 1 else '\n')
    termo += r
    contador += 1
    total += 1

  mais = int(input('Quantos termos a mais você quer mostrar? (0 para sair): '))
  while mais < 0:
    mais = int(input('Digite uma quantidade maior ou igual a 0: '))

print(f'Programa encerrado. Foram mostrados {total} termos.')
