from gendiff.formatters.stylish import get_end_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def formatter(form):
    if form == 'stylish':
        return get_end_stylish
    if form == 'plain':
        return get_plain
    elif form == 'json':
        return get_json
    else:
        raise ValueError
