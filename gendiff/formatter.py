from gendiff import make_stylish
from gendiff import make_plain


def create_formate(formatter, diff):
    """
    Формирует итоговое представление,
    в зависимости от выбранного форматера
    """
    if formatter == 'stylish':
        return make_stylish(diff)
    elif formatter == 'plain':
        return make_plain(diff)
