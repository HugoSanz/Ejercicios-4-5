validal = False

while not valida:
    password = input("\nIntrodueix contrasenya: ")
    
    error = False
    
    if len(password) < 8:
        print("Error: Massa curta")
        error = True
        
    if "@" in password:
        print("Error: No pot tindre @")
        error = True
        
    majuscules = 0
    minuscules = 0
    digits = 0
    especials = 0
    
    for c in password:
        if c.isupper(): 
            majuscules += 1
        if c.islower(): 
            minuscules += 1
        if c.isdigit(): 
            digits += 1
        if c in "!+-*$%()": 
            especials += 1
            
    if majuscules < 2:
        print("Error: Falten majúscules")
        error = True
    if minuscules < 3:
        print("Error: Falten minúscules")
        error = True
    if digits < 1:
        print("Error: Falta un número")
        error = True
    if especials < 1:
        print("Error: Falta caràcter especial")
        error = True
        
    if error == False:
        print("Contrasenya vàlida")
        valida = True
        