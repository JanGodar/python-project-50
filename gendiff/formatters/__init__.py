from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def formatter(form):
    if form == 'stylish':
        return get_stylish
    elif form == 'plain':
        return plain
    elif form == 'json':
        return json
