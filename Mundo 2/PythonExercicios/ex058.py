from random import randint

computador = randint(0, 10)
resposta = -1
contjogada = 0

print('Pensei em um número entre 0 e 10. Tente adivinhar!')

while resposta != computador:
  resposta = int(input('Digite seu palpite: '))
  contjogada += 1

  if resposta != computador:
    print('Não foi dessa vez, tente novamente!')

print('Parabéns!! Você adivinhou o número que eu estava pensando!')
print(f'Você precisou de {contjogada} palpite(s) para vencer.')
