import os
from gendiff import generate_diff


def test_flat_json():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    assert generate_diff(file1_path, file2_path) == expectation
