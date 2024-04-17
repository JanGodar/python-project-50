import json
import yaml


def get_json(file):
    return json.load(open(f"tests/fixtures/{file}"))


def get_yaml(file):
    return yaml.safe_load(open(f"tests/fixtures/{file}"))


def get_file_python(file, path):
    if path == '.json':
        return get_json(file)
    return get_yaml(file)


def get_path(file1, file2):
    file1 = get_file_python(file1, file1.split('.')[1])
    file2 = get_file_python(file2, file2.split('.')[1])

    return file1, file2
