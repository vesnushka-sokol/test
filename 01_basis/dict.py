men = {'first_name': 'Alex',
       'last_nme': 'Sokolov',
       'age': 37,
       'city': 'Bruchsal'}
print(men['first_name'])
print(men['last_nme'])
print(men['age'])
print(men['city'])

favorite_nums = {'Oleg': 5, 'Manya': 18, 'poli': 378, 'Daria': 4, 'Kolya': 7}
for name, num in favorite_nums.items():
    print(f'Любимое число {name.title()} - {num}')

scharik = {'vid': 'hund', 'name': 'alex'}
murzik = {'vid': 'katze', 'name': 'Marusya'}
pipi = {'vid': 'hamster', 'name': 'doroti'}
pets = [scharik, murzik, pipi]
for pet in pets:
    print(f'{pet["name"].title()} hat {pet["vid"]}')
