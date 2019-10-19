name = 'Eric'
message_1 = 'Hello'
message_2 = 'would you like to learn some Python today?'
print(message_1, name + ', ' + message_2)
print(message_1, name.lower() + ', ' + message_2)
print(message_1, name.upper() + ', ' + message_2)
print(message_1.title(), name.title() + ', ' + message_2.title())

famous_person = '   Albert Einstein  '
message = 'A person who never made a \n mistake never tried anything new.'
print(famous_person.strip(), 'once said, ' + '"' + message + '"')
