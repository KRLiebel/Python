import math
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digiite o comprimento do cateto adjacente: '))
hip = math.hypot(oposto, adjacente)

print('Dados do triângulo retângulo:')
print(f'O comprimento do cateto oposto equivale a {oposto}')
print(f'O comprimento do cateto adjacente equivale a {adjacente}')
print(f'Sendo assim a hipotenusa do triângulo-retângulo será: {hip:.2f}')