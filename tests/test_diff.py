import pytest
import json
from gendiff import generate_diff


@pytest.fixture
def files(tmpdir):
    file1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    file2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }

    file1_path = tmpdir.join("file1.json")
    file2_path = tmpdir.join("file2.json")

    with open(file1_path, "w") as f:
        json.dump(file1, f)

    with open(file2_path, "w") as f:
        json.dump(file2, f)

    return str(file1_path), str(file2_path)


def test_flat_json(files):
    assert generate_diff(*files) == (
        "{\n"
        "  - follow: False\n"
        "    host: hexlet.io\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: True\n"
        "}"
    )
    f1, f2 = files
    assert generate_diff(f1, f1) == ('{\n'
                                     '    follow: False\n'
                                     '    host: hexlet.io\n'
                                     '    proxy: 123.234.53.22\n'
                                     '    timeout: 50\n'
                                     '}')
