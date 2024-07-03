from gendiff.parser import create_parser


def test_create_parser():
    format_arg, first_file_arg, second_file_arg = create_parser(['-f', "plain", "file1", "file2"])

    assert format_arg == "plain"
    assert first_file_arg == "file1"
    assert second_file_arg == "file2"
