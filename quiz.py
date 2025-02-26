print("Seja muito bem vindo ao quiz!")
answer_user = input("Deseja iniciar? (S/N)").lower()

if answer_user != "s":
    quit()

score = 0

print("Começando...")

print("Em que ano o homem pisou na Lua pela primeira vez? \n (a) 1959 \n (b) 1939 \n (c) 1969")
answer_1 = input("Resposta: ")

if answer_1 == "c":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é a capital da Austrália? \n (a) Sydney \n (b) Canberra \n (c) Perth")
answer_2 = input("Resposta: ")

if answer_2 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o maior oceano do mundo? \n (a) Pacífico \n (b) Atlântico \n (c) Índico")
answer_3 = input("Resposta: ")

if answer_3 == "a":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é a maior espécie de felino do mundo? \n (a) Leão \n (b) Tigre siberiano \n (c) Pantera negra")
answer_4 = input("Resposta: ")

if answer_4 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o nome científico do ser humano? \n (a) Homo habilis \n (b) Homo sapiens \n (c) Homo floresiensis")
answer_5 = input("Resposta: ")

if answer_5 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/5") #ao aumentar o número de perguntas, mudar a quantidade
