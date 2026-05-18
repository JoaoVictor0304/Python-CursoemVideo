from random import randint

computador = randint(0, 10) # faz o computador gerar um número inteiro entre 0 à 10 aleatório
resposta = 50
contjogada = 1

print('Tente adivinhar o número que estou pensando!')

while resposta != computador:
  resposta = int(input('Digite o número: '))

  if resposta != computador:
    print('Não foi dessa vez, tente novamente!')
    contjogada += 1

print('Parabéns!! Você adivinhou o número que eu estava pensando!')
print(f'Você acertou em {contjogada} jogadas')
