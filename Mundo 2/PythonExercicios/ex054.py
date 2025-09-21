from datetime import date

atual = date.today().year
menor = 0
maior = 0

for i in range(1, 8):
  ano = int(input("Qual é o ano de nascimento da {}ª pessoa: ".format(i)))
  idade = atual - ano

  if idade >= 21:
    maior += 1
  else:
    menor += 1

print("Das 7 pessoas, {} são maior e {} são menor de idade.".format(maior, menor))
