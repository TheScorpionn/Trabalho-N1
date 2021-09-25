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
    if(nivel == 10):
        print("Você entrou em um portal dimensional que te levará a uma sala aleatória de 1 a 5")
        nivel = random.randrange(1, 6)
    elif(nivel == 6):
        print("Você está na sala: {0}." .format(nivel))
        print("Você será redirecionado para a sala: 8 ")
        nivel = 8