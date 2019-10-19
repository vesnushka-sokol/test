d = 'Введите дополнение для пиццы (если готовы с заказом: напишите "quit"): '
message = ''
while message != 'quit':
    message = input(d)
    if message != 'quit':
        print(f'{message} включено в заказ')
