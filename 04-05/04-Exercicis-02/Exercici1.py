import random

numero_secret = random.randint(1, 100)
intent = 0
encertat = False

while not encertat:
    intent += 1
    usuari = int(input("Introduix un número: "))
    
    if usuari < numero_secret:
        print("el meu número és major")
    elif usuari > numero_secret:
        print("el meu número és menor")
    else:
        print("Felicitats!")
        print("Intents necesaris:", intent)
        encertat = True