import json


def generate_diff(file_path1: str, file_path2: str) -> str:
    """
    Сравнивает содержимое двух файлов и генерирует отчет
     об изменениях во втором файле относительно первого.

    :param file_path1: Путь к первому файлу.
    :param file_path2: Путь ко второму файлу.
    :return: Строка, представляющая разницу между двумя файлами в формате:

          - key1: value1
            key2: value2
          + key3: value3

        где:
        Минус означает, что ключ существует только в первом файле
         или имеет другое значение
        Плюс означает, что ключ существует только во втором файле
         или имеет другое значение
        Отсутствие плюса или минуса говорит о том, что ключ есть в обоих файлах
         и его значения совпадают
    """
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    diff_str = "{\n"

    keys = file1.keys() | file2.keys()
    for key in sorted(keys):
        if key not in file1:
            diff_str += f"  + {key}: {file2[key]}\n"
        elif key not in file2:
            diff_str += f"  - {key}: {file1[key]}\n"
        elif file1[key] != file2[key]:
            diff_str += f"  - {key}: {file1[key]}\n  + {key}: {file2[key]}\n"
        else:
            diff_str += f"    {key}: {file1[key]}\n"

    diff_str += "}"
    return diff_str
