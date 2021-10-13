import random
print('Sorteio das apresentações dos alunos.')
equip1 = str(input('Digite o nome do primeiro grupo: '))
equip2 = str(input('Digite o nome do segundo grupo: '))
equip3 = str(input('Digite o nome do terceiro grupo: '))
equip4 = str(input('Digite o nome do quarto grupo: '))
equip5 = str(input('Digite o nome do quinto grupo: '))
grupos = [equip1, equip2, equip3, equip4, equip5]
random.shuffle(grupos)
print(f'A ordem de apresentação do trabalho será:')
print(grupos)