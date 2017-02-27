from collections import Iterable


def _construct_key(previous_key, separator, new_key):
    """
    Returns the new_key if no previous key exists, otherwise concatenates previous key, separator, and new_key
    :param previous_key:
    :param separator:
    :param new_key:
    :return: a string if previous_key exists and simply passes through the new_key otherwise
    """
    if previous_key:
        return "{}{}{}".format(previous_key, separator, new_key)
    else:
        return new_key


def flatten(nested_dict, separator="_"):
    """
    Flattens a dictionary with nested structure to a dictionary with no hierarchy
    :param nested_dict: dictionary we want to flatten
    :param separator: string to separate dictionary keys by
    :return: flattened dictionary
    """
    assert isinstance(nested_dict, dict), "flatten requires a dictionary input"
    assert isinstance(separator, str), "separator must be a string"

    # This global dictionary is recursively mutated and returned
    flattened_dict = dict()

    def _flatten(object_, key):
        """

        :param object_: object to flatten
        :param key: carries the concatenated key for the object_
        :return: None
        """
        if isinstance(object_, dict):
            for object_key in object_:
                _flatten(object_[object_key], _construct_key(key, separator, object_key))
        elif isinstance(object_, list) or isinstance(object_, set):
            for index, item in enumerate(object_):
                _flatten(item, _construct_key(key, separator, index))
        else:
            flattened_dict[key] = object_

    _flatten(nested_dict, None)
    return flattened_dict

flatten_json = flatten


def unflatten(flat_dict, separator='_'):
    """
    Creates a hierachical dictionary from a flattened dictionary
    Assumes that no lists are present in the
    :param flat_dict: a dictionary with no hierarchy
    :param separator: a string that separates keys
    :return: a dictionary with hierarchy
    """
    assert isinstance(flat_dict, dict), "un_flatten requires a dictionary input"
    assert isinstance(separator, str), "separator must be a string"
    assert all((not isinstance(value, Iterable) for value in flat_dict.values())), "provided dictionary is not flat"

    # This global dictionary is mutated and returned
    unflattened_dict = dict()

    def _unflatten(dic, keys, value):
        for key in keys[:-1]:
            dic = dic.setdefault(key, {})

        dic[keys[-1]] = value

    for item in flat_dict:
        _unflatten(unflattened_dict, item.split(separator), flat_dict[item])

    return unflattened_dict
