def _join_all(*x):
    return "".join(map(str, x)) if x[0] else x[-1]


def flatten_json(input_, separator="_"):
    output = {}

    def flatten(object_, name):
        if isinstance(object_, dict):
            [flatten(object_[key], _join_all(name, separator, key)) for key in object_]
        elif isinstance(object_, list):
            [flatten(item, _join_all(name, separator, index)) for index, item in enumerate(object_)]
        else:
            output[name] = object_

    flatten(input_, None)
    return output
