usuari = (input("Introduix una frase: "))
longitud = len(usuari) + 4

print("*" * longitud)
# El print(f "{x}") serveix per dir-li al codi que ixa variable es calcula, sino no funcionaría el codi.
print(f"* {usuari} *")
print("*" * longitud)