import os
import yaml
from yaml import SafeLoader
from gendiff import generate_diff
from gendiff import make_stylish


def test_yml():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_yaml.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1.yml')
    file2_path = os.path.join('tests', 'fixtures', 'file2.yml')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    file1 = yaml.load(open(file1_path), Loader=SafeLoader)
    file2 = yaml.load(open(file2_path), Loader=SafeLoader)

    diff = generate_diff(file1, file2)
    assert make_stylish(diff) == expectation
