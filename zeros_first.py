print('How many numbers do you want to add?')
N = int(input())
s = []
for i in range(N):
    z = int(input())
    if z == 0:
        s.insert(0, 0)
    else:
        s.append(z)
print('Zeros were moved in front of the other numbers.')
print(s)
