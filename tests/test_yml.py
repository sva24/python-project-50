import os
import yaml
from yaml import BaseLoader
from gendiff import generate_diff


def test_yml():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_yaml.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1.yml')
    file2_path = os.path.join('tests', 'fixtures', 'file2.yml')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    file1 = yaml.load(open(file1_path), Loader=BaseLoader)
    file2 = yaml.load(open(file2_path), Loader=BaseLoader)
    assert generate_diff(file1, file2) == expectation
