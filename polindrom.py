while True:
    print('Enter some text please. Or enter \'Q\' to finish')
    expr = input()
    if expr == 'Q':
        break
    counter = 0
    for z in range(len(expr)//2):
        if expr[z] == expr[-z-1]:
            counter += 1
    if counter == len(expr)//2:
        print('palindrome')
    else:
        print('random')
