import json
# import copy


def generate_diff(json1, json2):
    return json.dumps(json1, indent=2)
