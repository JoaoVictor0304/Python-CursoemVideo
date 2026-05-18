
cont = 1
soma = 0

while 0 < cont:
  num = int(input('Digite um número (999 - sair): '))
  soma += num
  cont += 1

  if num == 999:
    total = soma - 999
    print(f'A soma de todos números é: {total}')
    cont = 0
