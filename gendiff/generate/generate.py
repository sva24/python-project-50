def build_diff(file1: dict, file2: dict) -> dict:
    """
    Сравнивает содержимое двух файлов и генерирует отчет об изменениях во втором
    файле относительно первого.

    Args:
        file1 (dict): Первый файл.
        file2 (dict): Второй файл.

    Returns:
        dict: Словарь представляющий разницу между двумя файлами, содержащий тип
        изменений и значения.

        Минус означает, что ключ существует только в первом файле или имеет
        другое значение.

        Плюс означает, что ключ существует только во втором файле или имеет
        другое значение.

        Отсутствие плюса или минуса говорит о том, что ключ есть в обоих файлах
        и его значения совпадают.
    """
    keys = sorted(file1.keys() | file2.keys())
    result_diff = {}
    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key not in file1:
            result_diff[key] = {'type': 'added', 'value': value2}
        elif key not in file2:
            result_diff[key] = {'type': 'deleted', 'value': value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            result_diff[key] = {'type': 'nested',
                                'value': build_diff(value1, value2)}
        elif file1[key] == file2[key]:
            result_diff[key] = {'type': 'unchanged', 'value': value1}
        else:
            result_diff[key] = {'type': 'changed',
                                'value1': value1, 'value2': value2}
    return result_diff
