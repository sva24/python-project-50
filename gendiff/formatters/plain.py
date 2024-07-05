def normalize(val: dict) -> str:
    """
    Нормализует значение для вывода в виде строки.

    Args:
        val (dict): Значение для нормализации.

    Returns:
        str: Нормализованная строка.
    """
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, (dict, list)):
        return '[complex value]'
    return f"'{val}'" if isinstance(val, str) else str(val)


def process_diff(current_value: dict, path: str) -> str:
    """
    Обрабатывает разницу и возвращает строки с изменениями в формате plain.

    Args:
        current_value (dict): Текущий словарь значений.
        path (str): Путь для отслеживания изменений.

    Returns:
        str: Строки с изменениями в формате plain.
    """
    lines = []

    for key, val in sorted(current_value.items()):
        nested_path = f"{path}{key}"
        if isinstance(val, dict) and 'type' in val:
            process_type(val, lines, nested_path)
        else:
            value = normalize(val)
            lines.append(f"Property '{nested_path}'"
                         f" was added with value: {value}")

    return '\n'.join(line for line in lines if line)


def process_type(val, lines, nested_path):
    """
    Обрабатывает тип изменений и добавляет их в список строк.

    Args:
        val (dict): Словарь с типом изменений.
        lines (list): Список строк для добавления изменений.
        nested_path (str): Вложенный путь для отслеживания изменений.
    """

    type_ = val['type']
    if type_ == 'nested':
        lines.append(process_diff(val["value"], f"{nested_path}."))
    elif type_ == 'changed':
        value1 = normalize(val["value1"])
        value2 = normalize(val["value2"])
        lines.append(f"Property '{nested_path}' was updated."
                     f" From {value1} to {value2}")
    elif type_ == 'added':
        value = normalize(val["value"])
        lines.append(f"Property '{nested_path}'"
                     f" was added with value: {value}")
    elif type_ == 'deleted':
        lines.append(f"Property '{nested_path}' was removed")
    return lines


def make_plain(diff: dict) -> str:
    """
    Преобразует словарь с различиями в строку в формате plain
    Args:
        diff (dict): Словарь с различиями.

    Returns:
        str: Строка в формате plain.
    """

    return process_diff(diff, '')
