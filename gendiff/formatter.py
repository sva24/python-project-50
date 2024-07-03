from gendiff import make_stylish


def create_formate(formatter, diff):
    """
    Формирует итоговое представление,
    в зависимости от выбранного форматера
    """
    if formatter == 'stylish':
        return make_stylish(diff)
