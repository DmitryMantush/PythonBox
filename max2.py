print('How many numbers do you want to add?')
N = int(input())
s = []
for i in range(N):
    s.insert(0, int(input()))
#ss = sorted(s, reverse=True)
#print('These guys are the biggest:', ss[0], ',', ss[1], end='.')
#Выше первый рабочий вариант, но он содает копию исходного списка.
m1 = max(s)
if s[0] == m1:
    m2 = s[1]
else:
    m2 = s[0]
for z in s:
    if z == m1:
        continue
    if z > m2:
        m2 = z
print('These guys are the biggest:', m1, ',', m2, end='.')