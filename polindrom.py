while True:
    print('Enter some text please. Or enter \'Q\' to finish')
    expr = input()
    if expr == 'Q':
        break
    rev_expr = expr[::-1]
    print(rev_expr)
    if expr == rev_expr:
        print('Wow, it` s a palindrome bro')
    else:
        print('Palindrome expected. Try again.')

