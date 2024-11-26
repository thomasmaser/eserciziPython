#esercizio while: randomizzatore
#non funziona minAvg, non capisco come mai, sembra che avg non sia mai minore di maxAvg ma questo non è possibile anche perchè avgAvg è minore di maxAvg

import random
numCicli1 = 100 #regola il numero di iterazioni del ciclo più interno, quindi anche le avg intermedie
numcicli2 = 100 #regola il numero di iterazioni del ciclo più estermo, quindi anche le avg finali

maxMax = 0
minMax = 10000
avgMax = 0

maxMin = 0
minMin = 10000
avgMin = 0

maxAvg = 0
minAvg = 10000
avgAvg = 0

for i in range (1, numcicli2):
    max = 0
    min = 10000
    avg = 0

    for i in range (1, numCicli1):
        a = 0
        num1 = 6
        num2 = 8
        while num1 != num2:
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            a += 1
        if a > max:
            max = a
        elif a < min:
            min = a
        avg += a
    
    if max > maxMax:
        maxMax = max
    elif max < minMax:
        minMax = max
    avgMax += max

    if min > maxMin:
        maxMin = min
    elif min < minMin:
        minMin = min
    avgMin += min

    if avg > maxAvg:
        maxAvg = (avg/numCicli1)
    elif avg < minAvg:
        minAvg = (avg/numCicli1)
    avgAvg += (avg/numCicli1)
print("maxMax = ", maxMax)
print("minMax = ", minMax)
print("avgMax = ", avgMax/numcicli2)
print("maxMin = ", maxMin)
print("minMin = ", minMin)
print("avgMin = ", avgMin/numcicli2)
print("maxAvg = ", maxAvg)
print("minAvg = ", minAvg)
print("avgAvg = ", avgAvg/numcicli2)


            


