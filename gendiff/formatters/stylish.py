def normalize(val: dict, depth: int) -> str:
    """
    Нормализует значение для вывода в виде строки.

    Args:
        val (dict): Значение для нормализации.
        depth (int): Текущая глубина вложенности.

    Returns:
        str: Нормализованная строка.
    """
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, dict):
        return process_diff(val, depth + 1)
    return str(val)


def process_diff(current_value: dict, depth: int) -> str:
    """
    Обрабатывает разницу и возвращает строки с изменениями в формате stylish.

    Args:
        current_value (dict): Текущий словарь значений.
        depth (int): Текущая глубина вложенности.

    Returns:
        str: Строки с изменениями в формате stylish.
    """
    indent = '    '
    current_indent = indent * depth if depth else ''

    lines = ["{"]

    for key, val in sorted(current_value.items()):
        if isinstance(val, dict) and 'type' in val:
            process_type(key, val, lines, current_indent, depth)
        else:
            value = normalize(val, depth)
            lines.append(f'{current_indent}    {key}: {value}')

    lines.append(current_indent + "}")
    return '\n'.join(lines)


def process_type(key, val, lines, current_indent, depth) -> list:
    """
    Обрабатывает тип изменений и добавляет их в список строк.

    Args:
        key (str): Ключ текущего значения.
        val (dict): Словарь с типом изменений.
        lines (list): Список строк для добавления изменений.
        current_indent (str): Текущий отступ для форматирования.
        depth (int): Текущая глубина вложенности.

    Returns:
        list: Строки с изменениями в формате stylish.
    """
    type_ = val['type']
    if type_ == 'nested':
        value = process_diff(val["value"], depth + 1)
        lines.append(f'{current_indent}    {key}: {value}')
    elif type_ == 'changed':
        value1 = normalize(val["value1"], depth)
        value2 = normalize(val["value2"], depth)
        lines.append(f'{current_indent}  - {key}: {value1}')
        lines.append(f'{current_indent}  + {key}: {value2}')
    elif type_ == 'added':
        value = normalize(val["value"], depth)
        lines.append(f'{current_indent}  + {key}: {value}')
    elif type_ == 'deleted':
        value = normalize(val["value"], depth)
        lines.append(f'{current_indent}  - {key}: {value}')
    elif type_ == 'unchanged':
        value = normalize(val["value"], depth)
        lines.append(f'{current_indent}    {key}: {value}')
    return lines


def make_stylish(diff: dict) -> str:
    """
    Преобразует словарь с различиями в строку в формате stylish.

    Args:
        diff (dict): Словарь с различиями.

    Returns:
        str: Строка в формате stylish.
    """
    return process_diff(diff, 0)
