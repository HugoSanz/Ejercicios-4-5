# Sol·licitar les notes dels exàmens i la mitjana desitjada
nota_1r_examen = float(input("Introdueix la nota del primer examen: "))
nota_desitjada = float(input("Quina nota vols tindre este trimestre? "))

# Calcular la nota necessària al segon examen.
nota_1r_examen = (nota_1r_examen * 0.40)
nota_2n_examen_necessaria = (nota_desitjada - nota_1r_examen) / 0.60 

# Nota desitjada
print(f"Per a obtindre un {nota_desitjada} en el trimestre necessites un {nota_2n_examen_necessaria} al segon examen.")
