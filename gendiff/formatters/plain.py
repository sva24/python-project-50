def normalize(val: dict) -> str:
    """
    Нормализует значение для вывода в виде строки.
    """
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, (dict, list)):
        return '[complex value]'
    return f"'{val}'" if isinstance(val, str) else str(val)


def iter_(current_value, path):
    lines = []

    for key, val in sorted(current_value.items()):
        nested_path = f"{path}{key}"
        if isinstance(val, dict) and 'type' in val:
            type_ = val['type']
            if type_ == 'nested':
                lines.append(iter_(val["value"], f"{nested_path}."))
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
        else:
            value = normalize(val)
            lines.append(f"Property '{nested_path}'"
                         f" was added with value: {value}")

    return '\n'.join(line for line in lines if line)


def make_plain(value: dict) -> str:

    return iter_(value, '')
