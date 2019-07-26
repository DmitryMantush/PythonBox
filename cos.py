import math
x = float(input())
N = int(input())
cos = 0
for m in range(N):
    mem = (x**(2*m))/math.factorial(2*m)*(-1)**m
    cos += mem

print(cos)
