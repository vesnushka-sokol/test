# file = 'C:/Users/Vesnushka/PycharmProjects/metiz/num.txt'
with open('pi_million_digits.txt') as f:
    new_line = ''
    for line in f:
        new_line += line.strip()
geburtstag = input('Ihr Geburtstag, in the form mmddyy: ')
if geburtstag in new_line:
    print('Ваше число др есть в числе Пи')
else:
    print('Вашего числа др нет в числе Пи')
