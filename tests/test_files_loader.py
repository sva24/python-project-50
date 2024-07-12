from gendiff.files_loader import load_files
from pytest import raises


def test_load_files_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    file1, file2 = load_files(file1_path, file2_path)
    assert file1 == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    assert file2 == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_load_files_yaml():
    file1_path = 'tests/fixtures/file1.yml'
    file2_path = 'tests/fixtures/file2.yml'
    file1, file2 = load_files(file1_path, file2_path)
    assert file1 == {
        "hosts": "tests",
        "ftpserver": "8.8.8.8",
        "ftpuser": "user",
        "ftppass": "pass",
        "port": 21
    }
    assert file2 == {
        "hosts": "prod",
        "ftpserver": "1.1.1.1",
        "ftpuser": "user",
        "ftppass": "password",
        "port": 21
    }


def test_load_files_unsupported_format():
    with raises(ValueError):
        load_files('invalid_format.txt', 'invalid_format.txt')

