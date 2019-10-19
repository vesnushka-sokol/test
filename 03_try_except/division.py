print('Введите 2 числа и я поделю их')
print('Нажмите "q" для выхода')
while True:
    first_num = input('\nFirst number: ')
    if first_num != 'q':
        second_num = input('Second number: ')
        if second_num != 'q':
            try:
                answer = int(first_num) / int(second_num)
                print(answer)
            except ZeroDivisionError:
                print('Делить на 0 нельзя!')
        else:
            break
    else:
        break
