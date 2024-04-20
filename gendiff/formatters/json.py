from json import dumps


def get_json(diff_list):
    return dumps(diff_list, indent=4)
