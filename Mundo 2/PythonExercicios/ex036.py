'''Escreve um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. 
Calcule o valor da prestação mensal, sabendo que ele não vai poder exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))

mensal = casa / (anos * 12)

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${mensal}')

if mensal <= salario*0.30:
    print('Seu empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
