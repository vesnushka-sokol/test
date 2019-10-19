n = int(input())
if n < 2:
    print('младенец')
elif 2 <= n < 4:
    print('малыш')
elif 4 <= n < 13:
    print('ребенок')
elif 13 <= n < 20:
    print('подросток')
elif 20 <= n < 65:
    print('взрослый')
else:
    if n >= 65:
        print('пожилой человек')
