import os
import sys
import json
import yaml
from yaml.loader import SafeLoader


def load_file(file_path: str) -> str:
    """
    Загружает содержимое файла в зависимости от его расширения.

    Args:
        file_path (str): Путь к файлу, который требуется загрузить.

    Returns:
        dict: Содержимое файла в виде словаря, если файл является JSON или YAML.

    Raises:
        ValueError: Если расширение файла не поддерживается.
    """
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
    Загружает данные из двух файлов и возвращает их в виде кортежа.

    Args:
        file1_path (str): Путь к первому файлу.
        file2_path (str): Путь ко второму файлу.

    Returns:
        tuple: Кортеж с данными из первого и второго файлов.
    """

    try:
        file1 = load_file(file1_path)
        file2 = load_file(file2_path)
        return file1, file2
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
