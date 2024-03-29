import json
import yaml
from tests.fixtures.fixture import result_string
from gendiff.gendiff import generate_diff

def test_argparse(result_string):
    json1 = json.load(open('gendiff/file1.json'))
    json2 = json.load(open('gendiff/file2.json'))
    assert result_string == generate_diff(json1, json2)

    yaml1 = yaml.load(open('gendiff/filepath1.yml'), Loader=yaml.FullLoader)
    yaml2 = yaml.load(open('gendiff/filepath2.yml'), Loader=yaml.FullLoader)
    assert result_string == generate_diff(yaml1, yaml2)
