from json import dumps


def json(diff_list):
    return dumps(diff_list, indent=4)
