import json
from tests.fixtures.fixture import result_string_small, result_string_big
from tests.fixtures.fixture import result_string_json, result_string_plain
from gendiff.gendiff import generate_diff


shirt1_json = 'tests/fixtures/shirt1.json'
shirt2_json = 'tests/fixtures/shirt2.json'
shirt1_yml = 'tests/fixtures/shirt1.yml'
shirt2_yml = 'tests/fixtures/shirt2.yml'
long1_json = 'tests/fixtures/long1.json'
long2_json = 'tests/fixtures/long2.json'
long1_yml = 'tests/fixtures/long1.yml'
long2_yml = 'tests/fixtures/long2.yml'


def test_stylish(result_string_small, result_string_big):
    assert result_string_small == generate_diff(shirt1_json, shirt2_json, 'stylish')
    assert result_string_small == generate_diff(shirt1_yml, shirt2_yml, 'stylish')
    assert result_string_big == generate_diff(long1_json, long2_json, 'stylish')
    assert result_string_big == generate_diff(long1_yml, long2_yml, 'stylish')


def test_plain(result_string_plain):
    assert result_string_plain == generate_diff(long1_json, long2_json, 'plain')
    assert result_string_plain == generate_diff(long1_yml, long2_yml, 'plain')



def test_json(result_string_json):
    assert json.dumps(result_string_json, indent=4) == generate_diff(long1_json, long2_json, 'json')
    assert json.dumps(result_string_json, indent=4) == generate_diff(long1_yml, long2_yml, 'json')