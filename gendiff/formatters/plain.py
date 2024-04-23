def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, (bool, type(None))):
        correct_values = {None: 'null', True: 'true', False: 'false'}
        return correct_values[value]
    if isinstance(value, int):
        return value
    return f"'{value}'"


def get_key(diction, parent):
    if parent:
        return f"{parent}.{diction['key']}"
    return diction['key']


def get_str_added(diction, key):
    value = get_value(diction['value'])
    return f"Property '{key}' was added with value: {value}"


def get_str_removed(diction, key):
    return f"Property '{key}' was removed"


def get_str_nested(diction, key):
    return get_plain(diction['value'], key)


def get_str_change(diction, key):
    value = get_value(diction['value'])
    value_new = get_value(diction['value_new'])
    return f"Property '{key}' was updated. From {value} to {value_new}"


def get_value_for_list(diction, key, operation):
    all_dict = {
        'added': get_str_added,
        'removed': get_str_removed,
        'nested': get_str_nested,
        'change': get_str_change
    }
    if operation in all_dict:
        return all_dict[operation](diction, key)
    else:
        raise ValueError


def get_plain(diff_list, parent=''):
    end_list = []
    for diction in diff_list:
        operation = diction['operation']
        key = get_key(diction, parent)
        if operation == 'same':
            continue
        end_list.append(get_value_for_list(diction, key, operation))

    return '\n'.join(end_list)
