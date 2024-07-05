from gendiff import build_diff
from gendiff import load_files
from gendiff.parser import create_parser
from gendiff.formatter import create_formate


def main():
    """
    Основная функция для сравнения различий между двумя JSON файлами.
    """
    formatter, file1_path, file2_path = create_parser()
    file1, file2 = load_files(file1_path, file2_path)
    diff = build_diff(file1, file2)
    print(create_formate(formatter, diff))


if __name__ == "__main__":
    main()
