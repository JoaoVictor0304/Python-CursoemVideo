
cont = 0

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

while cont != 5:
  print('')
  print('[1] somar')
  print('[2] multiplicar')
  print('[3] maior')
  print('[4] novos números')
  print('[5] sair')
  opcao = int(input('Escolha a opção que deseja realizar:'))

  if opcao == 1:
    resposta = v1 + v2
    print(f'A soma de {v1} e {v2} é {resposta}')

  if opcao == 2:
    resposta = v1 * v2
    print(f'A multiplicação de {v1} e {v2} é {resposta}')

  if opcao == 3:
    if v1 > v2:
      print(f'O {v1} é maior que {v2}')
    else:
      print(f'O {v2} é maior que {v1}')

  if opcao == 4:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))

  if opcao == 5:
    cont = 5
