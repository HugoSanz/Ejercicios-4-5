codis_morse = [
    " _ _ _ _ _ ",
    " . _ _ _ _ ",
    " . . _ _ _ ",
    " . . . _ _ ",
    " . . . . _ ",
    " . . . . . ",
    " _ . . . . ",
    " _ _ . . . ",
    " _ _ _ . . ",
    " _ _ _ _ . " 
]


numero = int(input("Introdueix un número per a passar a Morse: "))
num_str = str(numero)
resultat = ""


for i in range(len(num_str)):

    xifra = int(num_str[i])
    

    resultat += codis_morse[xifra]
    

    if i < len(num_str) - 1:
        resultat += "   "

print(f"El número {numero} en Morse és:")
print(resultat)