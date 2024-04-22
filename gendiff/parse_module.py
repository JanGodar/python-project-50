import json
import yaml


def get_pars_str(file, extension):
    if extension == 'json':
        return json.load(file)
    elif extension in ('yaml', 'yml'):
        return yaml.safe_load(file)
    else:
        raise ValueError


def get_path(file):
    file1 = get_pars_str(open(file), file.split('.')[1])
    return file1
