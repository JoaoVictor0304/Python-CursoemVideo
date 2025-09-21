
nomeVelho = ''
maiorIdade = 0
somaIdade = 0
somaSexo = 0

for i in range(1, 5):
  print(f'----- {i}ª PESSOA -----')
  nome = str(input(f'Qual é o nome da {i}ª pessoa: ')).strip()
  idade = int(input(f'Qual é a idade da {i}ª pesso: '))
  sexo = input(f'Qual é o sexo da {i}ª pessoa (M/F): ').strip().lower()

  somaIdade += idade

  if sexo == 'm':
    if idade > maiorIdade:
      nomeVelho = nome
      maiorIdade = idade

  if sexo == 'f':
    if idade < 20:
      somaSexo += 1

media = somaIdade / 4

print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {nomeVelho}')
print(f'Ao todo são {somaSexo} mulheres com menos de 20 anos')
