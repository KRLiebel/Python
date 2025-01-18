import random

# Lista de dias da semana
diasusp = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# Informar folga semanal
folga = input("Qual a folga semanal do colaborador? ")  # Coleta a folga do usuário

# Função para sortear o dia de suspensão
def roletaSusp():
    sorteio = random.choice(diasusp)  # Escolhe um dia aleatório
    while sorteio == folga:  # Garante que o sorteio não seja no dia de folga
        sorteio = random.choice(diasusp)
    print(f"Dia escolhido para aplicar a suspensão do colaborador: {sorteio}")

# Chamar a função
roletaSusp()
