import random

nome = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')

lista=[nome, nome2, nome3, nome4]

escolhido = random.choice(lista)

print(f'O aluno escolhido foi {escolhido}')
