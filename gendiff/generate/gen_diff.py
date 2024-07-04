from gendiff import build_diff
from gendiff.formatter import create_formate
from gendiff.files_loader import load_files


def generate_diff(file_path1: str, file_path2: str, formatter='stylish') -> str:
    """
    Функция для модуля gendiff.
    Возвращает разницу между содержимым двух файлов
    """

    file1, file2 = load_files(file_path1, file_path2)
    diff = build_diff(file1, file2)
    create_formate(formatter, diff)

    return create_formate(formatter, diff)
