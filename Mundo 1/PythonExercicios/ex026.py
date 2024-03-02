frase = str(input('Digite uma frase: ')).upper().strip()

letrasA = frase.count('A')

print(f'A letra A aparece {letrasA} vezes na frase.')

encontrar = frase.find('A') + 1

print(f'A primeira letra A apareceu na posição {encontrar}')

encontrar2 = frase.rfind('A') + 1 # tenta encontrar a letra 'a' da direita para a esquerda

print(f'A última letra A apareceu na posição {encontrar2}')
