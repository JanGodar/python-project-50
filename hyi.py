def generate_diff(json1, json2):
    ls = []
    json2_copy = copy.copy(json2)
    for k, val in json1.items():
        if k not in json2:
            ls.append(('- ' + k, val))
        else:
            if val == json2[k]:
                ls.append(('  ' + k, val))
                del json2_copy[k]
            else:
                ls.append(('- ' + k, val))
                ls.append(('+ ' + k, json2_copy[k]))
                del json2_copy[k]
    for k, val in json2_copy.items():
        ls.append(('+ ' + k, val))

    ls = sorted(ls, key=lambda elem: elem[0][2])
    end_dict = {}
    for k, val in ls:
        if k[0] == ' ':
            k = k[2:]
        end_dict[k] = val
    return json.dumps(end_dict, indent=2)