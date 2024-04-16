import json
import yaml
from tests.fixtures.fixture import result_string_small, result_string_big
from tests.fixtures.fixture import result_string_json, result_string_plain
from gendiff.gendiff import generate_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json as get_json


def test_stylish(result_string_small, result_string_big):
    json1 = json.load(open('gendiff/file1.json'))
    json2 = json.load(open('gendiff/file2.json'))
    assert result_string_small == generate_diff(json1, json2, get_stylish)

    yaml1 = yaml.load(open('gendiff/filepath1.yml'), Loader=yaml.FullLoader)
    yaml2 = yaml.load(open('gendiff/filepath2.yml'), Loader=yaml.FullLoader)
    assert result_string_small == generate_diff(yaml1, yaml2, get_stylish)

    json11 = json.load(open('tests/fixtures/file1.json'))
    json22 = json.load(open('tests/fixtures/file2.json'))
    assert result_string_big == generate_diff(json11, json22, get_stylish)

def test_plain(result_string_plain):
    json1 = json.load(open('tests/fixtures/file1.json'))
    json2 = json.load(open('tests/fixtures/file2.json'))
    assert result_string_plain == generate_diff(json1, json2, plain)


def test_json(result_string_json):
    json1 = json.load(open('tests/fixtures/file1.json'))
    json2 = json.load(open('tests/fixtures/file2.json'))
    assert json.dumps(result_string_json, indent=4) == generate_diff(json1, json2, get_json)