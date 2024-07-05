import json


def make_json(diff: dict) -> str:
    """
     Преобразует словарь с различиями в JSON
     Args:
        diff (dict): Словарь различий, для конвертации

    Returns:
        str: Отформатированный JSON
    """

    return json.dumps(diff, indent=4, separators=(',', ': '))
