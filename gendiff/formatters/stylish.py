SYMBOLS = {'removed': '-', 'added': '+', 'same': ' '}


def converse(data):
    correct_values = {None: 'null', True: 'true', False: 'false'}
    if isinstance(data, (bool, type(None))):
        return correct_values[data]
    return data


def get_value(data, depth=4):
    res = ['{']
    if not isinstance(data, (list, dict)):
        return converse(data)
    elif isinstance(data, dict):
        for key, val in data.items():
            val = converse(val)
            res.append(f"{' ' * depth}{key}: {get_value(val, depth + 4)}")
        res.append(f"{' ' * (depth-4)}}}")
    return '\n'.join(res)


def stylish(diff_list, depth=4):
    end_list = []
    for diction in diff_list:
        operation = diction['operation']
        key = diction['key']
        value = diction['value']
        if operation == 'nested':
            end_list.append(f"{' ' * depth}{key}: {{\n"
                            f"{stylish(value, depth + 4)}")
            end_list.append(f"{' ' * depth}}}\n")

        elif operation == 'change':
            end_list.append(f"{' ' * (depth-2)}- {key}: "
                            f"{get_value(value[0], depth + 4)}\n")
            end_list.append(f"{' ' * (depth-2)}+ {key}: "
                            f"{get_value(value[1], depth + 4)}\n")

        else:
            end_list.append(f"{' ' * (depth-2)}{SYMBOLS[operation]} {key}: "
                            f"{get_value(value, depth + 4)}\n")
    return ''.join(end_list)


def get_stylish(diff):
    return f"{{\n{stylish(diff)}}}"