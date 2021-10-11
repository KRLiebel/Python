print('Transformando celsius em fahrenheit e em Kelvin.')
gc = float(input('Informe a temperatura em °Celsius: '))
gf = (1.8 * gc) + 32
print(f'A temperatura em {gc}°C convertido corresponde a {gf}°F')
gk = gc + 273
print(f'{gc}°C convertido para Kelvin corresponde a {gk}°K')