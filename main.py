import random

cont = 1
nivel = 1
while (cont <= 7 and nivel < 9):
    print("Você está na sala: {0}." .format(nivel))
    print("Escolha seu caminho: ")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    escolha = int(input())
    cont = cont + 1
    nivel = nivel + escolha