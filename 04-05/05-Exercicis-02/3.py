frase = input("Escriu una paraula o frase: ")

frase = frase.lower().replace(" ", "")

text_invertit = frase[::-1]

if frase == text_invertit:
    print("És un palíndrom!")
else:
    print("No és un palíndrom.")

