
opcao = '0'

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

while opcao != '5':
  print('')
  print('[1] somar')
  print('[2] multiplicar')
  print('[3] maior')
  print('[4] novos números')
  print('[5] sair')
  opcao = input('Escolha a opção que deseja realizar: ').strip()

  if opcao == '1':
    resposta = v1 + v2
    print(f'A soma de {v1} e {v2} é {resposta}')

  elif opcao == '2':
    resposta = v1 * v2
    print(f'A multiplicação de {v1} e {v2} é {resposta}')

  elif opcao == '3':
    if v1 > v2:
      print(f'O {v1} é maior que {v2}')
    elif v2 > v1:
      print(f'O {v2} é maior que {v1}')
    else:
      print('Os dois valores são iguais.')

  elif opcao == '4':
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))

  elif opcao == '5':
    print('Programa encerrado.')
  else:
    print('Opção inválida. Escolha uma opção de 1 a 5.')
