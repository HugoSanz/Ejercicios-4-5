email = input("Introduix el teu email: ")

if "@" not in email:
    print("ERROR1: L’email deu contindre una '@'")

elif email.find("@") == 0:
    print("ERROR2: L'email no pot començar amb '@'")

else:
    part_esquerra = email.split("@")[0]
    la_resta = email.split("@")[1]

    if len(part_esquerra) < 4:
        print("ERROR3: L’identificador1 deu tindre una longitud mínima de 4 caràcters")

    elif "." not in la_resta:
        print("ERROR4: Darrere de l’@ deu d'haver un punt")

    else:
        part_domini = la_resta.split(".")
        identificador2 = part_domini[0]
        domini = "." + part_domini[-1]

        if len(identificador2) < 3:
            print("ERROR5: L’identificador2 deu tindre una longitud mínima de 3 caràcters")

        elif domini not in [".com", ".es", ".org", ".gov"]:
            print("ERROR6: El domini no és vàlid")

        else:
            print("Enhorabona, email correcte!")