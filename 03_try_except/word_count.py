def count_words(filename):
    """" Подсчет приблизительного количества строк в файле """
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        with open('missing_files.txt', 'a', encoding='utf-8') as m:
            m.write(filename + '\n')
        # pass
        # print(f'Sorry, the file {filename} does not exist.')
    else:
        num_words = len(content.split())
        oft_count = content.count('the')
        print(f'The file {filename} has about {num_words} words.')
        print(f'Количество вхождений слова "the" в этом файле - '
              f'{oft_count}.\n')


for file in ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']:
    count_words(file)
