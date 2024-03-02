distancia = int(input('Digite qual é a distância da viagem em Km: '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'O preço da passagem é R${valor}')
else:
    valor = distancia * 0.45
    print(f'O preço da passagem é R${valor}')
