names = []
if len(names) == 0:
    print('We need to find some users!')
for name in names:
    if name == 'admin':
        print(f'Hello {name}, would you like to see a status report?')
    else:
        print(f'Hello {name.title()}, thank you for logging in again')

current_users = ['Eric', 'Maria', 'Alex', 'Sveta', 'Oleg']
new_users = ['lena', 'OLEG', 'Pavel', 'sveta', 'irina']
for user in new_users:
    if user.title() in current_users:
        print('Выберите новое имя')
    else:
        print('Имя доступно!')
