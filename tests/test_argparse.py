import json
import yaml
from tests.fixtures.fixture import result_string_small, result_string_big
from tests.fixtures.fixture import result_string_json, result_string_plain
from gendiff.gendiff import generate_diff
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json as get_json


def test_stylish(result_string_small, result_string_big):
    assert result_string_small == generate_diff('shirt1.json', 'shirt2.json', 'stylish')
    assert result_string_small == generate_diff('shirt1.yml', 'shirt2.yml', 'stylish')
    assert result_string_big == generate_diff('long1.json', 'long2.json', 'stylish')
    assert result_string_big == generate_diff('long1.yml', 'long2.yml', 'stylish')


def test_plain(result_string_plain):
    assert result_string_plain == generate_diff('long1.json', 'long2.json', 'plain')
    assert result_string_plain == generate_diff('long1.yml', 'long2.yml', 'plain')


def test_json(result_string_json):
    assert json.dumps(result_string_json, indent=4) == generate_diff('long1.json', 'long2.json', 'json')
    assert json.dumps(result_string_json, indent=4) == generate_diff('long1.yml', 'long2.yml', 'json')