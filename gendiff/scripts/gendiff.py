import argparse
from gendiff.generate import generate_diff


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', metavar='first file', type=str)
    parser.add_argument('second_file', metavar='second file', type=str)
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
    return args


if __name__ == "__main__":
    main()
