
n = int(input('Digite o número que deseja saber o fatorial: '))

resultado = 1

while n > 0:
  resultado = resultado * n
  n -= 1

print(f'O fatorial é {resultado}')
