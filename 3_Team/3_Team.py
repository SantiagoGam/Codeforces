Numero_problemas = int(input(" "))
Resultado = []
Desicion = 0

if 1 <= Numero_problemas <= 1000:
    for i in range (Numero_problemas):
        Aprobacion = [int(i) for i in input("").split()] 
        Resultado.append(Aprobacion)
    for j in Resultado:
        Contador = 0
        for k in j:
            if k == 1:
                Contador += 1
        if Contador >= 2:
            Desicion += 1



print(Desicion)