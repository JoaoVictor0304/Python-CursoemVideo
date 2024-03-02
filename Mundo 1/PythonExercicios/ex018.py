import math

angulo = float(input('Digite o ângulo que você deseja: '))

conversao = math.radians(angulo)

print(f'O ângulo de {angulo}° tem o SENO de {math.sin(conversao):.2f}')
print(f'O ângulo de {angulo}° tem o COSSENO de {math.cos(conversao):.2f}')
print(f'O ângulo de {angulo}° tem a TANGENTE de {math.tan(conversao):.2f}')
