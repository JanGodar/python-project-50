import json
import yaml
from pathlib import Path


def get_json(file):
    return json.load(open(f'gendiff/{file}'))


def get_yaml(file):
    return yaml.load(open(f'gendiff/{file}'), Loader=yaml.FullLoader)


def get_file_python(file, path):
    if path == '.json':
        return get_json(file)
    return get_yaml(file)


def get_pars(file1, file2):

    file1 = get_file_python(file1, Path(file1).suffix)
    file2 = get_file_python(file2, Path(file2).suffix)

    return file1, file2
