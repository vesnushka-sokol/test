file = 'alice.txt'
try:
    with open(file) as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Файл с названием "{file}" не найден.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'В файле "{file}" {num_words} слов.')
