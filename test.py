print('Enter expression. Use only + - * / and numbers. Enter "quit" to finish the program.')
while True:
    try:
        task = str(input())
        if task == 'quit':
            break
        import re

        mix = list(re.findall('[+-/*]|\d+', task))
        if mix[0] == '-':
            mix.insert(0, '0')
        while True:
            if '*' not in mix:
                break
            i = mix.index('*')
            num = float(mix[i - 1]) * float(mix[i + 1])
            mix[i - 1] = num
            del mix[i:i + 2]
        while True:
            if '/' not in mix:
                break
            i = mix.index('/')
            num = float(mix[i - 1]) / float(mix[i + 1])
            mix[i - 1] = num
            del mix[i:i + 2]
        while True:
            if '+' not in mix:
                break
            i = mix.index('+')
            num = float(mix[i - 1]) + float(mix[i + 1])
            mix[i - 1] = num
            del mix[i:i + 2]
        while True:
            if '-' not in mix:
                break
            i = mix.index('-')
            num = float(mix[i - 1]) - float(mix[i + 1])
            mix[i - 1] = num
            del mix[i:i + 2]
        result = round(mix[0], 2)
        print('The result is', result, sep=' ')
        print('Another expression?')
    except:
        print('Can`t calculate this. Check the requirements and compare with your expression.')
        print('Try again')
        continue
print('Masterpiece calculator turning off...')
