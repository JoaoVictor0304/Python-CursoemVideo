n = float(input('Qual é o preço do produto: R$'))

preco = n - (n*0.05)

print(f'O produto que custava R${n:.2f}, na promoção com desconto de 5% vai custar R${preco:.2f}')