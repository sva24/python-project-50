import os
import json
from gendiff import build_diff
from gendiff import make_stylish


def test_flat_json():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_json.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    diff = build_diff(file1, file2)

    assert make_stylish(diff) == expectation
