print('How many numbers do you want to add?')
N = int(input())
z1 = 0
z2 = 0
for i in range(N):
    b = int(input())
    if b > z1:
        z2 = z1
        z1 = b
    elif z1 > b > z2:
        z2 = b
print(z1, z2)
