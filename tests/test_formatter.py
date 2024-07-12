import json
import os
from gendiff.formatter import create_formate
from gendiff import build_diff


def test_create_formate_json():
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_format_json.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1_nested.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2_nested.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    diff = build_diff(file1, file2)
    result = create_formate('json', diff)
    assert result == expectation
