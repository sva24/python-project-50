import argparse


def create_parser(argv=None):
    """
    Создает парсер аргументов командной строки

    :return:
     Кортеж из трех элементов:
        - str: Формат вывода результатов сравнения файлов
        - str: Путь к первому файлу конфигурации.
        - str: Путь ко второму файлу конфигурации.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output',
                        required=False, default='stylish')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    args = parser.parse_args(argv)
    return args.format, args.first_file, args.second_file
