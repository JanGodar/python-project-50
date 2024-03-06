import json


def get_list_diff(json1, json2):
    ls = []
    for key, val in json1.items():
        if key not in json2:
            ls.append(('- ' + key, val))
        else:
            if val == json2[key]:
                ls.append(('  ' + key, val))
                del json2[key]
            else:
                ls.append(('- ' + key, val))
                ls.append(('+ ' + key, json2[key]))
                del json2[key]
    return ls, json2


def get_list_append(ls, json2):
    for key, val in json2.items():
        ls.append(('+ ' + key, val))
    return ls


def get_list_dict(ls):
    end_dict = {}
    for key, val in ls:
        if key[:2] == '  ':
            key = key[2:]
        end_dict[key] = val
    return end_dict


def generate_diff(json1, json2):

    ls, json2 = get_list_diff(json1, json2)
    ls = get_list_append(ls, json2)
    ls = sorted(ls, key=lambda elem: elem[0][2])
    end_dict = get_list_dict(ls)
    return json.dumps(end_dict, indent=2)
