import os
import json
import yaml
from yaml.loader import SafeLoader


def load_file(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1]
    if ext == '.json':
        with open(file_path, 'r') as file:
            return json.load(file)
    elif ext in ('.yaml', '.yml'):
        with open(file_path, 'r') as file:
            return yaml.load(file, Loader=SafeLoader)
    else:
        raise ValueError(f"Invalid file format: {ext}")


def load_files(file1_path: str, file2_path: str) -> tuple:
    """
    Загружает данные из двух файлов (JSON или YAML) и возвращает их в виде кортежа.

    :param file1_path: Путь к первому файлу.
    :param file2_path: Путь ко второму файлу.
    :return: Кортеж с данными из первого и второго файлов.
    """

    file1 = load_file(file1_path)
    file2 = load_file(file2_path)

    return file1, file2
