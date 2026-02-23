import random

mida = int(input("Introduix la grandària del vector: "))
val_min = int(input("Introduix el valor mínim: "))
val_max = int(input("Introduix el valor màxim: "))

numeros = []
for i in range(mida):
    numeros.append(random.randint(val_min, val_max))

texto_posiciones = "Posició: "
for i in range(len(numeros)):
    texto_posiciones = texto_posiciones + str(i) + "   "
print(texto_posiciones)

texto_valores = "Valor:   "
for x in numeros:
    texto_valores = texto_valores + str(x) + "   "
print(texto_valores)

print("Màxim:", max(numeros))
print("Mínim:", min(numeros))