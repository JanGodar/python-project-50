def get_value(value):
    correct_values = {None: 'null', True: 'true', False: 'false'}
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, (bool, type(None))):
        return correct_values[value]
#    if isinstance(value, (int, float)):
#        return value
    return f"'{value}'"


def get_key(diction, parent):
    if parent:
        return f"{parent}.{diction['key']}"
    return diction['key']


def get_plain(diff_list, parent=''):
    end_list = []
    for diction in diff_list:
        operation = diction['operation']
        key = get_key(diction, parent)

        if operation == 'nested':
            end_list.append(get_plain(diction['value'], key))
        elif operation == 'added':
            value = get_value(diction['value'])
            end_list.append(f"Property '{key}' was added with value: {value}")
        elif operation == 'removed':
            end_list.append(f"Property '{key}' was removed")
        elif operation == 'change':
            value = get_value(diction['value'])
            value_new = get_value(diction['value_new'])
            end_list.append(
                f"Property '{key}' was updated. "
                f"From {value} to {value_new}")
    result = '\n'.join(end_list)
    return result
