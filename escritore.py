import tkinter as tk
from tkinter import messagebox
import random
import datetime

# Lista de exercícios de escrita criativa
exercicios = [
    "Escreva uma história sobre um estranho que entra em uma cidade pequena.",
    "Descreva um momento de epifania de um personagem.",
    "Crie um diálogo entre dois personagens que estão em lados opostos de um debate acalorado.",
    "Imagine um mundo onde as estações do ano acontecem em uma ordem completamente diferente.",
    "Descreva um objeto comum de uma perspectiva incomum.",
    "Escreva sobre um encontro inesperado em um lugar incomum.",
    "Crie um monólogo de um personagem que está perdido em seus próprios pensamentos.",
    "Imagine uma civilização avançada que descobriu a maneira de controlar o tempo.",
    "Descreva uma paisagem onde cada elemento é de uma cor diferente.",
    "Escreva sobre um personagem que possui um segredo profundo e sombrio."
]

# Função para selecionar um exercício aleatório do dia
def exercicio_do_dia():
    hoje = datetime.date.today()
    random.seed(hoje.year + hoje.month + hoje.day)
    return random.choice(exercicios)

 #opção de desenvolver personagem
def desenv_perso():
   nome = input("Qual o nome do seu personagem? ")
   idade = input("idade dele(a): ")
   olhos = input("cor dos olhos: ")
   cabelo = input("cor do cabelo: ")
   return random.choice(treinarpp)

# Função para exibir o exercício do dia
def exibir_exercicio():
    exercicio = exercicio_do_dia()
    messagebox.showinfo("Exercício de Escrita Criativa do Dia", exercicio)
    
    
def exibir_treinarpp():
    treinarpp = desenv_perso()
    messagebox.showinfo("Treinar desenvolvimento de personagem", treinarpp)
    
   
# Criar janela principal
root = tk.Tk()
root.title("Exercícios de Escrita Criativa")

# Botão para exibir o exercício do dia e desnvolver personagem
botao_exercicio = tk.Button(root, text="Exercício de escrita do Dia", command=exibir_exercicio)
botao_exercicio.pack(pady=20)
botao_exercicio = tk.Button(root, text="Criação de personagem", command=exibir_treinarpp)
botao_exercicio.pack(pady=20)

# Iniciar a interface gráfica
root.mainloop()
