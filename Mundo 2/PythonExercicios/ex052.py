n = int(input('Digite um número: '))

if n <= 1:
    print('{} Não é primo'.format(n))
elif n == 2:
    print('{} É primo'.format(n))
elif n % 2 == 0:
    print('{} Não é primo'.format(n))
else:
    primo = True  # Assumimos que é primo até provar o contrário
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            primo = False
            break  # Sai do loop se encontrar um divisor
    
    if primo:
        print('{} É primo'.format(n))
    else:
        print('{} Não é primo'.format(n))
