import yaml
from yaml import BaseLoader


def load_yml(file1_path: str, file2_path: str) -> tuple:
    """
    Загружает данные из двух JSON-файлов и возвращает их в виде кортежа

    :param file1_path: Путь к первому файлу.
    :param file2_path: Путь ко второму файлу.
    :return: Кортеж с данными из первого и второго YAML-файлов

    """
    file1 = yaml.load(open(file1_path), Loader=BaseLoader)
    file2 = yaml.load(open(file2_path), Loader=BaseLoader)

    return file1, file2
