numero = int(input("Introduix un número per a convertir a palotes: "))

num_str = str(numero)
resultat = ""


for i in range(len(num_str)):
    cifra = int(num_str[i])
    
    resultat += "|" * cifra
    
    if i < len(num_str) - 1:
        resultat += " - "

print(f"El {numero} en decimal és el {resultat} en palotes.")