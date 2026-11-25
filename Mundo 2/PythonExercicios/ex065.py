
menor = 0
maior = 0
cont = 0
soma = 0
continuar = 'S'

while continuar == 'S':
  n = int(input('Digite um número inteiro: '))
  soma += n
  cont += 1

  if cont == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n

  continuar = input('Quer continuar? [S/N]: ').strip().upper()
  while continuar not in ('S', 'N'):
    continuar = input('Resposta inválida. Quer continuar? [S/N]: ').strip().upper()

media = soma / cont
print(f'A média dos {cont} valores digitados é {media:.2f}.')
print(f'O maior valor lido foi {maior}.')
print(f'O menor valor lido foi {menor}.')
