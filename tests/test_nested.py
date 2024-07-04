import os
import json
import yaml
from yaml import SafeLoader
from gendiff import make_stylish
from gendiff import generate_diff


def test_nested_json():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_nested_json.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1_nested.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2_nested.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))

    diff = generate_diff(file1, file2)
    generated_output = make_stylish(diff)

    assert generated_output == expectation


def test_nested_yml():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_nested_yml.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1_nested.yml')
    file2_path = os.path.join('tests', 'fixtures', 'file2_nested.yml')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    file1 = yaml.load(open(file1_path), Loader=SafeLoader)
    file2 = yaml.load(open(file2_path), Loader=SafeLoader)

    diff = generate_diff(file1, file2)
    generated_output = make_stylish(diff)

    assert generated_output == expectation
