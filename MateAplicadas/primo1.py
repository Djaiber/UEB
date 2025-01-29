import time
def es_primo_v1(n:int)->bool:
	if n == 1:
		return False
	for i in range(2,n):
		if n % i==0:
			return False
	return True

ti = time.time()
for x in range(1, 100001):
    es_primo_v1(x)
tf=time.time()
print("Tiempo de ejecucción:", tf-ti)