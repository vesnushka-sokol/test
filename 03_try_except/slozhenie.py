try:
    num_1 = input('First number: ')
    num_2 = input('Second number: ')
    answer = int(num_1) + int(num_2)
    print(answer)
except ValueError:
    print('какое-то из входных значений не является числом')
