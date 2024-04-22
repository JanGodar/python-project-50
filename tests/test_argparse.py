import pytest
from tests import get_path
from gendiff.gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, format, expected',
                         [
                             ('shirt1.json', 'shirt2.json', 'stylish', 'res_stylish_small.txt'),
                             ('shirt1.yml', 'shirt2.yml', 'stylish', 'res_stylish_small.txt'),
                             ('long1.json', 'long2.json', 'stylish', 'res_stylish_big.txt'),
                             ('long1.yml', 'long2.yml', 'stylish', 'res_stylish_big.txt'),
                             ('long1.json', 'long2.json', 'plain', 'res_plain.txt'),
                             ('long1.yml', 'long2.yml', 'plain', 'res_plain.txt'),
                             ('long1.json', 'long2.json', 'json', 'res_json.txt'),
                             ('long1.yml', 'long2.yml', 'json', 'res_json.txt')
                         ])
def test_generate_diff(file1, file2, format, expected):
    file1 = get_path(file1)
    file2 = get_path(file2)
    expected = get_path(expected)
    with open(expected, 'r') as file:
        result = file.read()
        assert generate_diff(file1, file2, format) == result
