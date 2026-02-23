letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

numero_dni = int(input("Introduix el número de DNI: "))

resto = numero_dni % 23

letra_final = letras[resto]

print("DNI complet:", str(numero_dni) + letra_final)
print("Resto:", resto)
print("Lletra:", letra_final)