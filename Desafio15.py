nome = str(input('Qual o nome do locador? '))
marca = str(input('Qual a marca do carro que deseja aluga? '))
km = float(input('Digite o quanto um carro alugado percorreu em KM: '))
dias = int(input('Quantos dias alugado: '))

pagamento = (km * 0.15) + (dias * 60)

print('Dados do aluguel:')
print(f'O nome do locadador: {nome}')
print(f'Marca do carro alugado: {marca}')
print(f'O carro será alugado por {dias} dia(s)')
print(f'O total a ser pago pelo carro alugado por {dias} dia(s), rodando por {km}Km, será {pagamento:.2f}R$')
