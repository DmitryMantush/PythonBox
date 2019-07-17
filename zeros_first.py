print('How many numbers do you want to add?')
N = int(input())
s = []
for i in range(N):
    s.append(int(input()))
count = 0
for item in s:
    if item == 0:
        count += 1
if count > 0:
    for a in range(count):
        s.remove(0)
    for n in range(count):
        s.insert(0, 0)
    print('Zeros were moved in front of the other numbers.')
print(s)
