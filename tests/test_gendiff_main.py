import os
import sys
from gendiff.scripts.gendiff import main
from pytest import raises


def test_formatter_functions_stylish(capsys):
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_nested_json.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1_nested.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2_nested.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    sys.argv = ['gendiff', '--format', 'stylish', file1_path, file2_path]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == expectation.strip()


def test_formatter_functions_json(capsys):
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_format_json.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1_nested.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2_nested.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()
    sys.argv = ['gendiff', '--format', 'json', file1_path, file2_path]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == expectation.strip()


def test_formatter_functions_plain(capsys):
    expectation_path = os.path.join('tests', 'fixtures', 'expectation_plain.txt')
    file1_path = os.path.join('tests', 'fixtures', 'file1_nested.json')
    file2_path = os.path.join('tests', 'fixtures', 'file2_nested.json')

    with open(expectation_path, "r") as file:
        expectation = file.read()

    sys.argv = ['gendiff', '--format', 'plain', file1_path, file2_path]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == expectation.strip()


def test_main_handles_invalid_arguments(capsys):
    sys.argv = ['gendiff', '--invalid-option', 'file1.json', 'file2.json']
    with raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "error: unrecognized arguments" in captured.err


def test_main_handles_nonexistent_files(capsys):
    sys.argv = ['gendiff', '--format', 'stylish', 'nonexistent_file1.json', 'nonexistent_file2.json']
    with raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "No such file or directory" in captured.out
