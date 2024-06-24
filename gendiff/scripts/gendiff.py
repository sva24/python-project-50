import argparse


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('str', metavar='first file', type=str)
    parser.add_argument('str', metavar='second file', type=str)
    args = parser.parse_args()


if __name__ == "__main__":
    main()
