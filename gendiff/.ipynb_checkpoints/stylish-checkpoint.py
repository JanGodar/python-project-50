def get_str(key, value, depth, sign):
    return f'{" "*(depth-2)}{sign}{key}: {value}'


def get_stylish(diff_list, depth=4):
    end_list = ['{']

    for diction in diff_list:
        if diction['operation'] == 'removed':
            end_list.append(get_str(diction['key'], diction['value'], depth, sign='- '))

        elif diction['operation'] == 'added':
            end_list.append(get_str(diction['key'], diction['value'], depth, sign='+ '))

        elif diction['operation'] == 'nested':
            local_list = get_stylish(diction, depth=+4)
            end_list.append(get_str(diction['key'], local_list, depth, sign=''))

        elif diction['operation'] == 'same':
            end_list.append(get_str(diction['key'], diction['value'], depth, sign='+ '))

        elif diction['operation'] == 'change':
            end_list.append(get_str(diction['key'], diction['value'][0], depth, sign='+ '))
            end_list.append(get_str(diction['key'], diction['value'][1], depth, sign='+ '))
    return end_list
