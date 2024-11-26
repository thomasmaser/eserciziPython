import random

maxMax = 500
minMax = 500
avgMax = 0

maxMin = 500
minMin = 500
avgMin = 500

maxAvg = 100
minAvg = 100
avgAvg = 100

for i in range (1, 100):
    max = 15
    min = 15
    avg = 0

    for i in range (1, 1000):
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
        maxAvg = avg
    elif avg < minAvg:
        minAvg = avg
    avgAvg += avg
print("maxMax = ", maxMax)
print("minMax = ", minMax)
print("avgMax = ", avgMax/100)
print("maxMin = ", maxMin)
print("minMin = ", minMin)
print("avgMin = ", avgMin/100)
print("maxAvg = ", maxAvg)
print("minAvg = ", minAvg)
print("avgAvg = ", avgAvg/100)
            


"""
numInput = int(input("numeross??"))
numRan = random.randint(1, 6969)
if numInput > numRan:
    print(numInput, ">", numRan)
else:
    print(numInput, "<", numRan)
"""