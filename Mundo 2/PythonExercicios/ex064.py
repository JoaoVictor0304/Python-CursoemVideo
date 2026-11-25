
cont = 0
soma = 0
num = int(input('Digite um número inteiro (999 para sair): '))

while num != 999:
  soma += num
  cont += 1
  num = int(input('Digite um número inteiro (999 para sair): '))

print(f'Você digitou {cont} números.')
print(f'A soma entre eles foi {soma}.')
