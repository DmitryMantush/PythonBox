import math
a = int(input())
b = int(input())
c = int(input())
if a <= 0:
    print('Side must be more than 0')
elif b <= 0:
    print('Side must be more than 0')
elif c <= 0:
    print('Side must be more than 0')
elif a >= b + c or b >= a + c or c >= a + b:
    print('It`s not a triangle.')
ang_a = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
ang_b = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
ang_c = 180 - ang_a - ang_b
print(ang_a, ang_b, ang_c)
