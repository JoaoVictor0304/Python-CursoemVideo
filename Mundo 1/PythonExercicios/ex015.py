dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

prcDias = (dias * 60) + (km * 0.15)

print(f'O preço a pagar é de R${prcDias:.2f}')
