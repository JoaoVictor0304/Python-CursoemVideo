nome = str(input('Digite seu nome completo: ')).strip()

print('Muito prazer em te conhecer!')

lista = nome.split()

print(f'Seu primeiro nome é {lista[0]}')

lista.reverse()

print(f'Seu último nome é {lista[0]}')
