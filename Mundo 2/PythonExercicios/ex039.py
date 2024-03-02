'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou o tempo do alistamento.
Seu programa também deverá mostra o tempo que falta ou que passou do prazo.'''

from datetime import date

nasc = int(input('Ano de nascimento: '))

today = date.today().year

idade = today - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {today}.')

if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = saldo + today
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')
    ano = today - saldo
    print(f'Seu alistamento foi em {ano}')
