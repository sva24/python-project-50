def normalize(val: dict, depth: int) -> str:
    """
    Нормализует значение для вывода в виде строки.
    """
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, dict):
        return iter_(val, depth + 1)
    return str(val)


def iter_(current_value, depth):
    indent = '    '
    current_indent = indent * depth if depth else ''

    lines = ["{"]

    for key, val in sorted(current_value.items()):
        if isinstance(val, dict) and 'type' in val:
            type_ = val['type']
            if type_ == 'nested':
                value = iter_(val["value"], depth + 1)
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
        else:
            value = normalize(val, depth)
            lines.append(f'{current_indent}    {key}: {value}')

    lines.append(current_indent + "}")
    return '\n'.join(lines)


def make_stylish(value: dict) -> str:

    return iter_(value, 0)
