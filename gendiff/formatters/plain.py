def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    correct_values = {None: 'null', True: 'true', False: 'false'}
    if isinstance(value, (bool, type(None))):
        return correct_values[value]
    return f"'{value}'"


def plain(diff_list, parent=''):
    end_list = []
    for diction in diff_list:
        operation = diction['operation']
        key = f"{parent}.{diction['key']}" if parent != '' else diction['key']
        if operation == 'same':
            continue
        elif operation == 'nested':
            end_list.append(plain(diction['value'], key))
        elif operation == 'added':
            value = get_value(diction['value'])
            end_list.append(f"Property '{key}' was added with value: {value}")
        elif operation == 'removed':
            end_list.append(f"Property '{key}' was removed")
        elif operation == 'change':
            value = get_value(diction['value'])
            value_new = get_value(diction['value_new'])
            end_list.append(f"Property '{key}' was updated. From {value} to {value_new}")
    return '\n'.join(end_list)
