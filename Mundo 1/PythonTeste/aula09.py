frase = 'Curso em Vídeo Python'

frase2 = '   Aprendendo Python  '

frase3 = ['Curso', 'Em', 'Vídeo', 'Python']

print(frase)

print(frase[3]) # pega apenas o caracter 3 da frase

print(frase[3:13]) # pega a frase do caracter 3 ao 12

print(frase[:13]) # começa do primeiro caracter até o caracter 12

print(frase[13:]) # vai do caracter 13 até o final da string

print(frase[1:15:2]) # vai do caracter 1 ao 14 pulando de 2 em 2 casas

print(len(frase)) # conta quantos caracteres tem na frase

print(frase.count('o')) # conta quantas vezes tem a letra 'o' na frase

print(frase.find('deo')) # localiza a palavra e mostra em qual caracter começa

print(frase.find('android')) # se não houver a palavra ele retorna -1

print('Curso' in frase) # verifica se a palavra 'Curso' está dentro da frase, se estiver ele retorna True

print(frase.replace('Python', 'Android')) # substitui a palavra 'Python' na frase por 'Android'

print(frase.upper()) # coloca a frase toda em caixa alta

print(frase.lower()) # coloca toda frase em caixa baixa

print(frase.capitalize()) # coloca letra maiúscula apenas na primeira letra da frase e o restante deixa em minúsculo

print(frase.title()) # coloca em maiúsculo a primeira letra de cada palavra

print(frase2.strip()) # remove espaços no começo e fim das strings

print(frase2.rstrip()) # remove espaços da direita da frase

print(frase2.lstrip()) # remove espaços da esquerda da frase

print(frase.split()) # cria uma lista e coloca as palavras separadas dentro dessa lista

print('-'.join(frase3)) # coloca um caracter no meio de cada elemento da lista e cria uma frase
