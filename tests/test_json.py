import os
import json
from gendiff import generate_diff

def test_flat_json():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_json.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))

    assert generate_diff(file1, file2) == expectation
