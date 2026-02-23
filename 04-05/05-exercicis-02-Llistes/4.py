import random

v_min = int(input("Introduix el valor mínim dels nombres aleatoris: "))
v_max = int(input("Introduix el valor màxim dels nombres aleatoris: "))

mida = random.randint(10, 20)

numeros = []
while len(numeros) < mida:
    candidat = random.randint(v_min, v_max)
    
    es_primer = True
    if candidat < 2:
        es_primer = False
    else:
        for i in range(2, candidat):
            if candidat % i == 0:
                es_primer = False
    
    if es_primer:
        numeros.append(candidat)

numeros.sort()

texto_pos = "Posició: "
for i in range(len(numeros)):
    texto_pos = texto_pos + str(i) + "   "
print(texto_pos)

texto_val = "Valor:   "
for x in numeros:
    texto_val = texto_val + str(x) + "   "
print(texto_val)