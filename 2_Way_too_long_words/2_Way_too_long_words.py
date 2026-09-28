n = int(input(""))
a = 1
Lista_palabras = []
c = 0
if(0 < n < 101):
    while(a <= n):
        Palabra = input("")
        list(Palabra)
        if len(Palabra) > 10:
            Letra1 = Palabra[0]
            Letra2 = Palabra[-1]
            FraseFinal = Letra1 + str(len(Palabra) - 2) + Letra2
            Lista_palabras.append(FraseFinal)
            a += 1
        else:
            Lista_palabras.append(Palabra)
            a += 1      
    
    for i in range(n):
        print(Lista_palabras[c])              
        c += 1       
