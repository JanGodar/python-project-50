from gendiff.parse_module import get_path
from gendiff.formatters import formatter


def get_sorted_key(dict1, dict2):
    return sorted(list(set(dict1.keys()) | set(dict2.keys())))


def is_dict(dict1, dict2, key):
    return isinstance(dict1[key], dict) and isinstance(dict2[key], dict)


def get_diff_dict(key, operation, value1):
    diff_dict = {
        'key': key,
        'operation': operation,
        'value': value1
    }
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
        diction = get_diff_dict(key, 'change', dict1[key])
        diction['value_new'] = dict2[key]
        return diction


def get_diff(dict1, dict2):
    key_sorted = get_sorted_key(dict1, dict2)
    diff_list = []

    for key in key_sorted:
        diff_list.append(get_diff_val(key, dict1, dict2))

    return diff_list


def generate_diff(filepath1, filepath2, get_format='stylish'):
    get_format = formatter(get_format)
    file1 = get_path(filepath1)
    file2 = get_path(filepath2)
    end_diff_str = get_format(get_diff(file1, file2))
    return end_diff_str
