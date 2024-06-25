import pytest
import json
from gendiff import generate_diff


def test_flat_json():
    with open('tests\\fixtures\\expectation.txt', "r") as file:
        expectation = file.read()
    file1 = 'tests\\fixtures\\file1.json'
    file2 = 'tests\\fixtures\\file2.json'

    assert generate_diff(file1, file2) == expectation
