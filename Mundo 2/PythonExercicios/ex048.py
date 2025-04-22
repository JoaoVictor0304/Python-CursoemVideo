s = 0
for c in range(1, 500):
  if c % 2 != 0:   
    if c % 3 == 0:
      s += c
print('A soma de todos números impáres multiplos de três é: {}'.format(s))