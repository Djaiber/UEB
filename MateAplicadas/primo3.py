import time
from math import floor, sqrt

def es_primo_v3(n:int)->bool:
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = floor(sqrt(n))
    for i in range(3, max_divisor+1, 2):
        if n % i == 0:
            return False
    return True
ti=time.time()
for x in range(1, 100001):
    es_primo_v3(x)
tf=time.time()
print("Tiempo de ejecucción:", tf-ti)