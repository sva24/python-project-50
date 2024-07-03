from gendiff import make_stylish


def create_formate(formatter, diff):

    if formatter == 'stylish':
        return make_stylish(diff)
