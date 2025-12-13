
import math
all = []
for num in range(1,100):
    sqrNum = num**2
    all.append(sqrNum)
for x in range(1,100): 
    for y in range(1,100):
        x2 = x**2
        y2 = y**2
        c = x2 + y2
        sqrC =int( math.sqrt(c))
        if c in all:
            print(x,y,sqrC)