print("Ingrese su voto (1,2,3 o 4)")
print("Para salir use 0")
voto = input()
totalVotos = 0
votosA = 0
votosB = 0
votosC = 0
votosD = 0

while voto != "0":
    print("Ingrese su voto (1,2,3 o 4)")
    print("Para salir use 0")
    voto = input()
    if voto == "1":
        print("Usted ha votado por el candidato 1")
        votosA += 1
        totalVotos += 1 
    elif voto == "2":
        print("Usted ha votado por el candidato 2")
        votosB += 1
        totalVotos += 1 
    elif voto == "3":
        print("Usted ha votado por el candidato 3")
        votosC += 1 
        totalVotos += 1 
    elif voto == "4":
        print("Usted ha votado por el candidato 4")
        votosD += 1
        totalVotos += 1 
    elif voto != "0":
        print("Opcion no valida")

porcentajeA = (votosA/totalVotos)*100
porcentajeB = (votosB/totalVotos)*100
porcentajeC = (votosC/totalVotos)*100
porcentajeD = (votosD/totalVotos)*100
   
print("Resultados de la votacion")
print("Candidato 1: ", votosA)
print("Porcentaje Candidato 1: ", porcentajeA, "%")
print("Candidato 2: ", votosB)
print("Porcentaje Candidato 2: ", porcentajeB, "%")
print("Candidato 3: ", votosC)
print("Porcentaje Candidato 3: ", porcentajeC, "%")
print("Candidato 4: ", votosD)
print("Porcentaje Candidato 4: ", porcentajeD, "%")
print("Total de votos: ", totalVotos)1
