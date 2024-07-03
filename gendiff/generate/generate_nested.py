def build_diff(data1: dict, data2: dict) -> dict:
    keys = sorted(data1.keys() | data2.keys())
    result_diff = {}
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1:
            result_diff[key] = {'type': 'added', 'value': value2}
        elif key not in data2:
            result_diff[key] = {'type': 'deleted', 'value': value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            result_diff[key] = {'type': 'nested', 'value': build_diff(value1, value2)}
        elif data1[key] == data2[key]:
            result_diff[key] = {'type': 'unchanged', 'value': value1}
        else:
            result_diff[key] = {'type': 'changed', 'value1': value1, 'value2': value2}
    return result_diff
