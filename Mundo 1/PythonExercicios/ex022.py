nome = str(input('Digite seu nome completo: ')).strip() # strip retira os espaços no inicio e no fim do que está sendo inserido

print('Analisando seu nome...')

print(f'Seu nome em maiúsculo é {nome.upper()}')

print(f'Seu nome em minúscula é {nome.lower()}')

novo = nome.replace(' ', '')

print(f'Seu nome tem ao todo {len(novo)} letras')

nome2 = nome.split()

print(f'Seu primeiro nome é {nome2[0]} e tem {len(nome2[0])} letras')