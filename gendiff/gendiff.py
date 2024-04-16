def get_sorted_key(dict1, dict2):
    return sorted(list(set(dict1.keys()) | set(dict2.keys())))


def is_dict(dict1, dict2, key):
    return isinstance(dict1[key], dict) and isinstance(dict2[key], dict)


def get_diff_dict(key, operation, value1, value2='None'):
    diff_dict = {
        'key': key,
        'operation': operation,
        'value': value1
    }
    if value2 != 'None':
        diff_dict['value_new'] = value2
    return diff_dict


def get_diff_val(key, dict1, dict2):
    if key not in dict2:
        return get_diff_dict(key, 'removed', dict1[key])

    elif key not in dict1:
        return get_diff_dict(key, 'added', dict2[key])

    elif is_dict(dict1, dict2, key):
        dict_child = get_diff(dict1[key], dict2[key])
        return get_diff_dict(key, 'nested', dict_child)

    elif dict1[key] == dict2[key]:
        return get_diff_dict(key, 'same', dict1[key])

    elif dict1[key] != dict2[key]:
        return get_diff_dict(key, 'change', dict1[key], dict2[key])


def get_diff(dict1, dict2):
    key_sorted = get_sorted_key(dict1, dict2)
    diff_list = []

    for key in key_sorted:
        diff_list.append(get_diff_val(key, dict1, dict2))

    return diff_list


def generate_diff(dict1, dict2, get_format):
    end_diff_str = get_format(get_diff(dict1, dict2))
    return end_diff_str
