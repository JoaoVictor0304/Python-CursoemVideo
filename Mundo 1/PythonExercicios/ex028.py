from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador gerar um número inteiro entre 0 à 5 aleatório

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Em qual número eu pensei? '))

print('PROCESSANDO...')
sleep(3) # faz uma pausa no programa de 3 segundos

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
