import random

z = random.randrange(1, 11)
print('Chose number from 1 to 10')
while int(input()) != z:
    print('Try again')
print('Exactly!')
