
sexo = input('Digite o sexo [M/F]: ').strip().upper()

while sexo not in ('M', 'F'):
  sexo = input('Valor inválido. Digite apenas M ou F: ').strip().upper()

print(f'Sexo {sexo} registrado com sucesso.')

