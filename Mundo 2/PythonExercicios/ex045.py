'''Crie um programa que faça o computador jogar jokenpô com você.'''

from random import randint

print('-=' * 10)
print('Vamos jogar jokenpô!')
print('-=' * 10)

player = int(input('Você escolhe 1-(Pedra) 2-(Papel) 3-(Tesoura)? '))

pc = randint(1, 3)

if pc == 1:
    print('PC escolheu 1-(Pedra)')
    if player == 1:
        print('Ninguém ganhou! Os dois escolheram Pedra.')
    elif player == 2:
        print('Você ganhou! O PC escolheu Pedra e você Papel.')
    elif player == 3:
        print('Você perdeu! O PC escolheu Pedra e você Tesoura.')
    else:
        print('Escolha um valor válido!')
elif pc == 2:
    print('PC escolheu 2-(Papel)')
    if player == 1:
        print('Você perdeu! O PC escolheu Papel e você Pedra.')
    elif player == 2:
        print('Ninguém ganhou! Os dois escolheram Papel.')
    elif player == 3:
        print('Você ganhou! O PC escolheu Papel e você Tesoura.')
    else:
        print('Escolha um valor válido!')    
elif pc == 3:
    print('PC escolheu 3-(Tesoura)')
    if player == 1:
        print('Você ganhou! O PC escolheu Tesoura e você Pedra.')
    elif player == 2:
        print('Você perdeu! O PC escolheu Tesoura e você Papel')
    elif player == 3:
        print('Ninguém ganhou! Os dois escolheram Tesoura.')
    else:
        print('Escolha um valor válido!')
