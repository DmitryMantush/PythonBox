import math
x = float(input())
N = int(input())
cos = 1
count = 0
memS = 0
for m in range(2, N+1, 2):
    mem = x**m/math.factorial(m)
    count += 1
    if count % 2 != 0:
        memS -= mem
    elif count % 2 == 0:
        memS += mem
cos += memS

print(cos)
