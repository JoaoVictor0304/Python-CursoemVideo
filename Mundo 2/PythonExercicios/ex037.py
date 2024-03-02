'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal'''

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
base = int(input('Sua opção: '))

if base == 1:
    print(f'O valor {n} em binário é {bin(n)[2:]}')
elif base == 2:
    print(f'O valor {n} em Octal é {oct(n)[2:]}')
elif base == 3:
    print(f'O valor {n} em Hexadecimal é {hex(n)[2:]}')
else:
    print('Digite um valor de base de conversão válido!')
