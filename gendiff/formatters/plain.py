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


def get_value_for_list(diction, key, operation):
    value = get_value(diction['value'])
    all_dict = {
        'added': f"Property '{key}' was added with value: {value}",
        'removed': f"Property '{key}' was removed",
    }
    if operation in all_dict:
        return all_dict[operation]
    else:
        raise ValueError


def get_plain(diff_list, parent=''):
    end_list = []
    for diction in diff_list:
        operation = diction['operation']
        key = get_key(diction, parent)

        if operation == 'same':
            continue
        elif operation == 'nested':
            end_list.append(get_plain(diction['value'], key))
        elif operation == 'change':
            value = get_value(diction['value'])
            value_new = get_value(diction['value_new'])
            end_list.append(
                f"Property '{key}' was updated. "
                f"From {value} to {value_new}"
            )
        else:
            end_list.append(get_value_for_list(diction, key, operation))
    result = '\n'.join(end_list)
    return result
