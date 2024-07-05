from gendiff import make_stylish
from gendiff import make_plain
from gendiff import make_json


def create_formate(formatter, diff):
    """
    Формирует итоговое представление различий в зависимости от выбранного
    форматера.

    Args:
        formatter (str): Выбранный форматер. Может быть 'stylish', 'plain' или
            'json'.
        diff (dict): Различия между файлами в виде словаря.

    Returns:
        str: Итоговое представление различий в заданном формате.
    """
    if formatter == 'stylish':
        return make_stylish(diff)
    elif formatter == 'plain':
        return make_plain(diff)
    elif formatter == 'json':
        return make_json(diff)
