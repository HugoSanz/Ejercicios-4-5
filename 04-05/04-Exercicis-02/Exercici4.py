import datetime

def opcio1():
    ara = datetime.datetime.now()
    print("Data actual:", ara.day, "/", ara.month, "/", ara.year)
    
def opcio2():
    ara = datetime.datetime.now()
    print("Hora actual:", ara.hour, ":", ara.minute, ":", ara.second)

def opcio3():
    dies = int(input("Quants dies vols sumar? "))
    resultat = datetime.datetime.now() + datetime.timedelta(days=dies)
    print("La nova data serà:", resultat.date())


def opcio4():
    d1_str = input("Data 1 (AAAA-MM-DD): ")
    d2_str = input("Data 2 (AAAA-MM-DD): ")

    d1 = datetime.date.fromisoformat(d1_str)
    d2 = datetime.date.fromisoformat(d2_str)
    
    diferencia = abs((d2 - d1).days)
    print("Data 1 | Data 2 | Diferència")
    print(d1, "|", d2, "|", diferencia)

def opcio5():
    data_text = input("Introduix una data (AAAA-MM-DD): ")
    data_usuari = datetime.date.fromisoformat(data_text)
    hui = datetime.date.today()
    
    if data_usuari < hui:
        print("És anterior a hui.")
    elif data_usuari > hui:
        print("És posterior a hui.")
    else:
        print("És hui mateix!")

opcio = "0"
while opcio != "9":
    print("\n--- MENÚ ---")
    print("1. Data actual | 2. Hora actual | 3. Sumar dies")
    print("4. Diferència  | 5. Comparar    | 9. Eixir")
    
    opcio = input("Tria una opció: ")

    if opcio == "1":
        opcio1()
    elif opcio == "2":
        opcio2()
    elif opcio == "3":
        opcio3()
    elif opcio == "4":
        opcio4()
    elif opcio == "5":
        opcio5()
    elif opcio == "9":
        print("Adéu!")