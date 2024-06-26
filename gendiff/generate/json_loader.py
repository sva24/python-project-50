import json


def load_json(file1_path: str, file2_path: str) -> tuple:
    """
    Загружает данные из двух JSON-файлов и возвращает их в виде кортежа

    :param file1_path: Путь к первому файлу.
    :param file2_path: Путь ко второму файлу.
    :return: Кортеж с данными из первого и второго JSON-файлов
    """
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))

    return file1, file2
