
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

i = 0
valor = 0
cont = 10

while i < cont:

  if i == 0:
    print(p)
    i += 1
    valor = p
  else:
    valor += r
    i += 1
    print(valor)

  if i == cont:
    resp = int(input('Deseja saber mais alguns termos? (0 - sair): '))
    if resp != 0:
      cont += resp
