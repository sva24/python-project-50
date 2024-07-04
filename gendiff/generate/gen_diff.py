from gendiff import build_diff
from gendiff import load_files
from gendiff import create_formate


def generate_diff(file_path1: str, file_path2: str, formatter='stylish') -> str:
    """
    Функция для модуля gendiff.
    Возвращает разницу между содержимым двух файлов
    """

    file1, file2 = load_files(file_path1, file_path2)
    diff = build_diff(file1, file2)
    create_formate(formatter, diff)

    return create_formate(formatter, diff)
