import argparse
from gendiff.generate import generate_diff
from gendiff.generate import load_json
from gendiff.generate import load_yml
import os


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output',
                        required=False)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    args = parser.parse_args()

    if os.path.splitext(args.first_file)[1] == '.json':
        file1, file2 = load_json(args.first_file, args.second_file)
    else:
        file1, file2 = load_yml(args.first_file, args.second_file)
    print(generate_diff(file1, file2))


if __name__ == "__main__":
    main()
