from name_function import get_formatted_name
print("'q' to quit")
while True:
    first = input("\nFirst name: ")
    if first == 'q':
        break
    last = input("\nLast name: ")
    if last == 'q':
        break
    form_name = get_formatted_name(first, last)
    print(f'\tNeatly formatted name: {form_name}.')
