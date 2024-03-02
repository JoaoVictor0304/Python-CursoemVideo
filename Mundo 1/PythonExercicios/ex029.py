vel = int(input('Qual a velocidade atual do carro? '))

if vel > 80:
    multa = (vel - 80) * 7
    print('Você está acima do limite de 80km/h, você será multado!')
    print(f'A multa irá custar R${multa:.2f}')
else:
    print('Você está no limite, boa viagem!')
