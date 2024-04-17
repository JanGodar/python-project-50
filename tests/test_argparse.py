import pytest
from gendiff.gendiff import generate_diff


shirt1_json = 'tests/fixtures/json/shirt1.json'
shirt2_json = 'tests/fixtures/json/shirt2.json'
shirt1_yml = 'tests/fixtures/yaml/shirt1.yml'
shirt2_yml = 'tests/fixtures/yaml/shirt2.yml'
long1_json = 'tests/fixtures/json/long1.json'
long2_json = 'tests/fixtures/json/long2.json'
long1_yml = 'tests/fixtures/yaml/long1.yml'
long2_yml = 'tests/fixtures/yaml/long2.yml'
res_json = 'tests/fixtures/correct/res_json.txt'
res_plain = 'tests/fixtures/correct/res_plain.txt'
res_stylish_big = 'tests/fixtures/correct/res_stylish_big.txt'
res_stylish_small = 'tests/fixtures/correct/res_stylish_small.txt'


@pytest.mark.parametrize('file1, file2, format, expected', 
                         [
                             pytest.param(shirt1_json, shirt2_json, 'stylish', res_stylish_small),
                             pytest.param(shirt1_yml, shirt2_yml, 'stylish', res_stylish_small),
                             pytest.param(long1_json, long2_json, 'stylish', res_stylish_big),
                             pytest.param(long1_yml, long2_yml, 'stylish', res_stylish_big),
                             pytest.param(long1_json, long2_json, 'plain', res_plain),
                             pytest.param(long1_yml, long2_yml, 'plain', res_plain),
                             pytest.param(long1_json, long2_json, 'json', res_json),
                             pytest.param(long1_yml, long2_yml, 'json', res_json)
                         ])
def test_generate_diff(file1, file2, format, expected):
    with open(expected, 'r') as file:
            result = file.read()
            assert generate_diff(file1, file2, format) == result
