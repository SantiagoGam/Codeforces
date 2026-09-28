#Result of scores that advance
score_final = 0
#Saved scores
puntaje_repetidos = 0
score = 1

#Numbers of scores of participants and minimum score required to advance
n, k = [int(i) for i in input().split()] 
if n >= k:
    if (1 <= k <= n <= 50):    
        scores = [int(j) for j in input().split()] 
        
        #PRIMER CAMBIO
        puntaje_repetidos = scores.count(k) #Count of same scores in variable 'puntaje_repetidos'

        if len(scores) == puntaje_repetidos:
            pass

        #CORREGIR
        if score == scores[-1]:
            score_final = 1

        else:
            for score in scores[:k-1]:
                if score != 0:
                    if (0 <= score <= 100 ):
                        score_final += 1
            score +=1
        

print(score_final+puntaje_repetidos)





