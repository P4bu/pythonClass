import random

def player():
    print("PIEDRA-PAPEL-TIJERAS")
    play = input("Ingrese su jugada ==> ")
    play = play.lower()
    return play

def player_computer():
    computer = random.choice(["PIEDRA","PAPEL","TIJERAS"])
    computer = computer.lower() 
    print(computer)
    return computer

def game(play, computer):
    if(play == computer):
        print("EMPATE")
    elif(play == "tijeras" and computer == "papel"):
        print("GANASTE")
    elif(play == "piedra" and computer == "tijeras"):
        print("GANASTE")   
    elif(play == "papel" and computer == "piedra"):
        print("GANASTE")
    else:
        print("PIERDES")
        print(computer)

game(player_computer(), player())