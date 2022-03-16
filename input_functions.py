from utilities import TAGS


def check_pattern(pattern: list):
    for tag in pattern:
        if tag not in TAGS:
            raise ValueError(f"Ошибка! Тега {tag} не существует.\n")


def prepare_pattern(pattern_text: str) -> (str, int):
    pattern = [el.upper() for el in pattern_text.strip().split()]
    check_pattern(pattern)
    return pattern, len(pattern)


def manual_pattern_input() -> (str, int):
    flag = True
    while flag:
        flag = False
        pattern_text = input('Введите паттерн поиска:\n>>> ')
        try:
            pattern, pattern_len = prepare_pattern(pattern_text)
        except ValueError as ve:
            print(str(ve))
            flag = True
    print(f'Паттерн {" ".join(pattern)} распознан.\n')
    return pattern, pattern_len


def file_pattern_input(file_path: str) -> (str, int):
    try:
        with open(file_path, 'r') as file:
            pattern_text = file.read()
            pattern, pattern_len = prepare_pattern(pattern_text)
            print(f'Паттерн {" ".join(pattern)} распознан.\n')
    except ValueError as ve:
        print(str(ve), end='')
        print('Попробуйте ввести паттерн вручную!\n')
        pattern, pattern_len = manual_pattern_input()
    except FileNotFoundError:
        print('Файл не найден.\nПопробуйте ввести паттерн вручную!\n')
        pattern, pattern_len = manual_pattern_input()
    return pattern, pattern_len


def manual_text_input() -> str:
    print('Введите текст (можно использовать переносы строк).\n'
          'Пустая строка (\\n\\n) воспринимается как конец ввода:')
    flag = True
    text = ''
    while flag:
        try:
            input_text = input('>>> ').replace('\n', ' ')
            if input_text == '':
                flag = False
            else:
                text += ' ' + input_text
        except UnicodeDecodeError:
            print('Строчка не прочитана, ошибка юникода, повторите пожалуйста еще раз.')
    print('Текст прочитан.\n')
    return text


def file_text_input(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            text = file.read().replace('\n', ' ')
            print('Текст прочитан.\n')
    except FileNotFoundError:
        print('Файл не найден.\nПопробуйте ввести текст вручную!\n')
        text = manual_text_input()
    return text
