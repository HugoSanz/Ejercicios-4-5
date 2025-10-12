#Declarem les variables.
A = int(input("variable A: "))
B = int(input("variable B: "))
temp = 0

#Guardem cualquier variable en temp, este fa de backup, i podem canviar les altres
temp = A
A = B
B = temp

# Resultats dels números intercanviats.
print(f"El número A: {A} Número B: {B}")