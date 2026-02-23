opcio = ""

while opcio != "9":
        print("\n--- MENÚ DE CADENES ---")
        print("1.- Longitud d’una cadena")
        print("2.- Comparar alfabèticament dos cadenes")
        print("3.- Concatenació de dos cadenes")
        print("4.- Obtindre subcadenes")
        print("5.- Invertir cadena")
        print("9.- Eixir")
        

        opcio = input("\nTria una opció: ")
        if opcio == "1":
            cadena = input("Introdueix una cadena: ")
            print(f"La longitud de la cadena és: {len(cadena)}")

        elif opcio == "2":
            cadena1 = input("Introdueix la primera cadena: ")
            cadena2 = input("Introdueix la segona cadena: ")
            if cadena1 > cadena2:
                print(f"'{cadena1}' és alfabèticament major que '{cadena2}'")
            elif cadena2 > cadena1:
                print(f"'{cadena2}' és alfabèticament major que '{cadena1}'")
            else:
                print("Les dos cadenes són iguals.")

        elif opcio == "3":
            cadena1 = input("Introdueix la primera cadena: ")
            cadena2 = input("Introdueix la segona cadena: ")
            print(f"Resultat: {cadena1 + cadena2}")

        elif opcio == "4":
            cadena = input("Introdueix una cadena: ")
            inici = int(input("Introdueix l'índex d'inici: "))
            fi = int(input("Introdueix l'índex final: "))
            print(f"La subcadena és: {cadena[inici:fi]}")

        elif opcio == "5":
            cadena = input("Introdueix una cadena: ")
            print(f"Cadena invertida: {cadena[::-1]}")

        elif opcio == "9":
            print("Gràcies per utilitzar el programa. Adeu!")
        
        else:
            print("Opció no vàlida, torna-ho a intentar.")
