def get_diff(dict1, dict2):
    key_sorted = sorted(list(set(dict1.keys()) | set(dict2.keys())))
    diff_list = []

    for key in key_sorted:

        if key not in dict2:
            diff_list.append({
                'key': key,
                'operation': 'removed',
                'value': dict1[key]
            })

        elif key not in dict1:
            diff_list.append({
                'key': key,
                'operation': 'added',
                'value': dict2[key]
            })

        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            dict_child = get_diff(dict1[key], dict2[key])
            diff_list.append({
                'key': key,
                'operation': 'nested',
                'value': dict_child
            })

        elif dict1[key] == dict2[key]:
            diff_list.append({
                'key': key,
                'operation': 'same',
                'value': dict1[key]
            })

        elif dict1[key] != dict2[key]:
            diff_list.append({
                'key': key,
                'operation': 'change',
                'value': (dict1[key], dict2[key])
            })

    return diff_list


def generate_diff(dict1, dict2, get_format):
    end_diff_str = get_format(get_diff(dict1, dict2))
    return end_diff_str
