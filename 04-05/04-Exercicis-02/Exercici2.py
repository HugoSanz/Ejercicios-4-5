import random

opcions = ["pedra", "paper", "tisores"]
maquina = random.choice(opcions)

elecció_usuari = input("Pedra paper o tisores?")

if elecció_usuari not in opcions:
    print("Error, paraula desconeguda")
else:
    print("Máquina ha elegit:", maquina)
    
    if elecció_usuari == maquina:
        print("Empat")
    elif (elecció_usuari == "pedra" and maquina == "tisores") or (elecció_usuari == "paper" and maquina == "pedra") or (elecció_usuari == "tisores" and maquina == "paper"):
        print ("Has guanyat")
    else:
        print("Has perdut")
    