noms_numeros = ["zero", "un", "dos", "tres", "quatre", "cinc", "sis", "set", "huit", "nou"]


numero = int(input("Introdueix un número: "))
num_str = str(numero)
resultat = ""


for i in range(len(num_str)):

    xifra = int(num_str[i])

    paraula = noms_numeros[xifra]
    

    resultat += paraula
    

    if i < len(num_str) - 1:
        resultat += ", "


print(f"El {numero} convertit a paraules seria:")
print(resultat)