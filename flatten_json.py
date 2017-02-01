def _join_all(*x):
    return "".join(map(str, x)) if x[0] else x[-1]


def flatten_json(input_, separator="_"):
    output = {}

    def _flatten(object_, name):
        if isinstance(object_, dict):
            [_flatten(object_[key], _join_all(name, separator, key)) for key in object_]
        elif isinstance(object_, list):
            [_flatten(item, _join_all(name, separator, index)) for index, item in enumerate(object_)]
        else:
            output[name] = object_

    _flatten(input_, None)
    return output

flatten = flatten_json
