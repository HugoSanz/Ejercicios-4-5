def omplir_vector(n):
    v = []
    for i in range(n):
        v.append(int(input("Introduix un número: ")))
        return v

def imprimir_vector(v):
    print(v)

def sumar_elements(v):
    total = 0
    for x in v:
        total += xw
    return total

def maxim_vector(v):
    m = v[0]
    for x in v:
        if x > m:
            m = x
    return m

def invertir_vector(v):
    return v[::-1]


n = int(input("Introduix la mida del vector: "))
numeros = omplir_vector(n)
imprimir_vector(numeros)

suma = sumar_elements(numeros)
print(f"La suma dels elements del vector és: {suma}")

maxim = maxim_vector(numeros)
print(f"El valor màxim dels elements del vector és: {maxim}")

numeros_invertits = invertir_vector(numeros)
print("El vector invertit és: ")
imprimir_vector(numeros_invertits)