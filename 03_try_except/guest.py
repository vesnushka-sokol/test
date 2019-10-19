with open('guest_book.txt', 'w', encoding='utf-8') as g:
    stop = -1
    while stop != 0:
        new_name = input('Ihr Name: ')
        print(f'Hallo, {new_name.title()}!')
        g.write(new_name.title() + '\n')
        stop = int(input('Если стоит очередь, нажмите 1, если нет - 0: '))
