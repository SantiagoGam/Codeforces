#Entrada de datos
K = int(input(""))
 
if(0 < K < 101):
    if (K == 2):  
        print("NO")
    elif(K % 2 == 0):
        print("YES" )
    else:
        print("NO") #Condicional si es par y si K debe estar entre el rango 1-100