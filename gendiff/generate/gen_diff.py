from gendiff import build_diff
from gendiff import load_files


def generate_diff(file_path1: str, file_path2: str) -> dict:
    """
    Функция для модуля gendiff.
    Возвращает разницу между содержимым двух файлов
    """

    file1, file2 = load_files(file_path1, file_path2)
    return build_diff(file1, file2)
