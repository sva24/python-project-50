def make_stylish(value):
    def format_value(val, depth):
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
                    lines.append(f'{current_indent}    {key}: {iter_(val["value"], depth + 1)}')
                elif type_ == 'changed':
                    lines.append(f'{current_indent}  - {key}: {format_value(val["value1"], depth)}')
                    lines.append(f'{current_indent}  + {key}: {format_value(val["value2"], depth)}')
                elif type_ == 'added':
                    lines.append(f'{current_indent}  + {key}: {format_value(val["value"], depth)}')
                elif type_ == 'deleted':
                    lines.append(f'{current_indent}  - {key}: {format_value(val["value"], depth)}')
                elif type_ == 'unchanged':
                    lines.append(f'{current_indent}    {key}: {format_value(val["value"], depth)}')
            else:
                lines.append(f'{current_indent}    {key}: {format_value(val, depth)}')

        lines.append(current_indent + "}")
        return '\n'.join(lines)

    return iter_(value, 0)
