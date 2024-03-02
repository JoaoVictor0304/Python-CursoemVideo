'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
- A vista dinheiro/cheque: 10% de desconto.
- A vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.'''

produto = float(input('Preço das compras? R$ '))
print('''Formas de pagamento:
1-(A vista dinheiro/cheque) 
2-(A vista cartão) 
3-(Em até 2x no cartão) 
4-(3x ou mais no cartão)''')
pague = input('Qual é a opção? ')

if pague == '1':
    valor = produto - (produto * 0.1)
elif pague == '2':
    valor = produto - (produto * 0.05)
elif pague == '3':
    valor = produto
    parcela = produto / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif pague == '4':
    vezes = int(input('Em quantas vezes será parcelado? '))
    if vezes < 3:
        valor = produto
        print('O número de parcelas deve ser 3 ou superior!')
    else:
        valor = produto + (produto * 0.2)
        parcela = valor / vezes
        print(f'Sua compra será parcelada em {vezes}x de R${parcela:.2f} COM JUROS')
else:
    valor = produto
    print('Digite uma opção de pagamento válida!')
print(f'Sua compra de R${produto:.2f} vai custar R${valor:.2f} no final')
