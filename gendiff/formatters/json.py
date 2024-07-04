import json


def make_json(value: dict) -> str:
    """
     Преобразует словарь с различиями в json
    """

    return json.dumps(value, indent=4, separators=(',', ': '))
