# Sol·licitar a l'usuari la quantitat en euros, possem el float ja que ens interessen els centims.
euros = float(input("Introdueix la quantitat en euros (EUR): "))

# Tipus de canvi actual.
tipus_de_canvi = 1.16

# Calcular la quantitat en dolars.
dollars = euros * tipus_de_canvi

# Mostrar conversió.
print(f"{euros} EUR són {dollars} USD.")