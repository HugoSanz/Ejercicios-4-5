import random


# A
def multiplicar_tram(vector, left, right):
    for i in range(left, right + 1):
        vector[i] = vector[i] * 2
# B
def invertir_tram(vector, left, right):
    l, r = left, right
    while l < r:
        temporal = vector[l]
        vector[l] = vector[r]
        vector[r] = temporal
        l, r = l + 1, r - 1
# C
def contar_imparells_pos_parelles(vector):
    contador = 0
    for i in range(0, len(vector), 2):
        if vector[i] % 2 != 0:
            contador = contador + 1
    return contador
# D
def contar_menors_que_x(vector, x, n):
    if n >= len(vector): n = len(vector) - 1
    contador = 0
    for i in range(n + 1):
        if vector[i] < x:
            contador = contador + 1
    return contador
# E
def esta_ordenat_ascendent(vector):
    for i in range(len(vector) - 1):
        if vector[i] > vector[i + 1]: return False
    return True
# F
def primera_subsequencia_tres_consecutius(vector):
    for i in range(len(vector) - 2):
        if vector[i+1] == vector[i] + 1 and vector[i+2] == vector[i] + 2:
            return i
    return -1
# G
def suma_major_que_x_minim_elements(vector, x):
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]
        if suma > x: return True
    return False
# H
def contar_n_majors_que_x(vector, n, x):
    comptador = 0
    for i in range(len(vector)):
        if vector[i] > x:
            comptador += 1
            if comptador == n: return i - n + 1
        else:
            comptador = 0
    return -1
# I
def posicio_ultim_imparell(vector):
    for i in range(len(vector) - 1, -1, -1):
        if vector[i] % 2 != 0: return i
    return -1
# J
def suma_despres_primer_imparell(vector):
    trobat = False
    suma = 0
    for num in vector:
        if trobat: suma += num
        elif num % 2 != 0: trobat = True
    return suma if trobat else 0



n_elements = int(input("Quants números tindrà el vector?: "))
v = []
for i in range(n_elements):
    v.append(int(input("Número posició " + str(i) + ": ")))

opcio = ""
while opcio != "eixir":
    print("\nVector actual:", v)
    print("Opcions: a, b, c, d, e, f, g, h, i, j (o 'eixir')")
    opcio = input("Tria una opció: ").lower()

    if opcio == "a":
        multiplicar_tram(v, 0, 1 if len(v)>1 else 0)
        print("Tram 0-1 multiplicat.")
    elif opcio == "b":
        invertir_tram(v, 0, 1 if len(v)>1 else 0)
        print("Tram 0-1 invertit.")
    elif opcio == "c":
        print("Imparells en posicions parelles:", contar_imparells_pos_parelles(v))
    elif opcio == "d":
        print("Menors que 10 fins posició 2:", contar_menors_que_x(v, 10, 2))
    elif opcio == "e":
        print("Està ordenat?:", esta_ordenat_ascendent(v))
    elif opcio == "f":
        print("Posició 3 consecutius:", primera_subsequencia_tres_consecutius(v))
    elif opcio == "g":
        print("Suma > 20?:", suma_major_que_x_minim_elements(v, 20))
    elif opcio == "h":
        print("Inici de 2 números > 10:", contar_n_majors_que_x(v, 2, 10))
    elif opcio == "i":
        print("Posició últim imparell:", posicio_ultim_imparell(v))
    elif opcio == "j":
        print("Suma darrere primer imparell:", suma_despres_primer_imparell(v))