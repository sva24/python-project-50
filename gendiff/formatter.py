from gendiff import make_stylish
from gendiff import make_plain
from gendiff import make_json


def create_formate(formatter, diff):
    """
    Формирует итоговое представление,
    в зависимости от выбранного форматера
    """
    if formatter == 'stylish':
        return make_stylish(diff)
    elif formatter == 'plain':
        return make_plain(diff)
    elif formatter == 'json':
        return make_json(diff)
