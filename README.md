[![Build Status](https://travis-ci.org/amirziai/flatten.svg?branch=master)](https://travis-ci.org/amirziai/flatten) [![PyPI version](https://badge.fury.io/py/flatten-json.svg)](https://badge.fury.io/py/flatten-json) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/7ae779ec4e99462f907c5afecfd5de48)](https://www.codacy.com/app/amirziai/flatten?utm_source=github.com&utm_medium=referral&utm_content=amirziai/flatten&utm_campaign=Badge_Coverage) 

# flatten_json
Flattens JSON objects in Python. ```flatten_json``` flattens the hierarchy in your object which can be useful if you want to force your objects into a table.

## Installation
```bash
pip install flatten_json
```

## flatten

### Usage
Let's say you have the following object:
```python
dic = {
    "a": 1,
    "b": 2,
    "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}]
}
```
which you want to flatten. Just apply ```flatten```:
```python
from flatten_json import flatten
flatten(dic)
```

Results:
```python
{'a': 1,
 'b': 2,
 'c_0_d_0': 2,
 'c_0_d_1': 3,
 'c_0_d_2': 4,
 'c_0_e_0_f': 1,
 'c_0_e_0_g': 2}
```

### Usage with Pandas
For the following object:
```python
dic = [
    {"a": 1, "b": 2, "c": {"d": 3, "e": 4}},
    {"a": 0.5, "c": {"d": 3.2}},
    {"a": 0.8, "b": 1.8},
]
```
We can apply `flatten` to each element in the array and then use pandas to capture the output as a dataframe:
```python
dic_flattened = [flatten(d) for d in dic]
```
which creates an array of flattened objects:
```python
[{'a': 1, 'b': 2, 'c_d': 3, 'c_e': 4},
 {'a': 0.5, 'c_d': 3.2},
 {'a': 0.8, 'b': 1.8}]
```
Finally you can use ```pd.DataFrame``` to capture the flattened array:
```python
import pandas as pd
df = pd.DataFrame(dic_flattened)
```
The final result as a Pandas dataframe:
```
	a	b	c_d	c_e
0	1	2	3	4
1	0.5	NaN	3.2	NaN
2	0.8	1.8	NaN	NaN
```

### Custom separator
By default `_` is used to separate nested element. You can change this by passing the desired character:
```python
flatten({"a": [1]}, '|')
```
returns:
```python
{'a|0': 1}
```

### Ignore root keys
By default `flatten` goes through all the keys in the object. If you are not interested in output from a set of keys you can pass this set as an argument to `root_keys_to_ignore`:
```python
dic = {
    'a': {'a': [1, 2, 3]},
    'b': {'b': 'foo', 'c': 'bar'},
    'c': {'c': [{'foo': 5, 'bar': 6, 'baz': [1, 2, 3]}]}
}
flatten(dic, root_keys_to_ignore={'b', 'c'})
```
returns:
```python
{
    'a_a_0': 1,
    'a_a_1': 2,
    'a_a_2': 3
}
```
This feature can prevent unnecessary processing which is a concern with deeply nested objects.

## unflatten
Reverses the flattening process. Example usage:
```python
from flatten_json import unflatten

dic = {
    'a': 1,
    'b_a': 2,
    'b_b': 3,
    'c_a_b': 5
}
unflatten(dic)
```
returns:
```python
{
    'a': 1,
    'b': {'a': 2, 'b': 3},
    'c': {'a': {'b': 5}}
}
```

### Unflatten with lists
`flatten` encodes key for list values with integer indices which makes it ambiguous for reversing the process. Consider this flattened dictionary:
```python
a = {'a': 1, 'b_0': 5}
```

Both `{'a': 1, 'b': [5]}` and `{'a': 1, 'b': {0: 5}}` are legitimate answers.
 
Calling `unflatten_list` the dictionary is first unflattened and then in a post-processing step the function looks for a list pattern (zero-indexed consecutive integer keys) and transforms the matched values into a list.
 
Here's an example:
```python
from flatten_json import unflatten_list
dic = {
    'a': 1,
    'b_0': 1,
    'b_1': 2,
    'c_a': 'a',
    'c_b_0': 1,
    'c_b_1': 2,
    'c_b_2': 3
}
unflatten_list(dic)
```
returns:
```python
{
    'a': 1,
    'b': [1, 2],
    'c': {'a': 'a', 'b': [1, 2, 3]}
}
```

## Command line invocation
```bash
>>> echo '{"a": {"b": 1}}' | flatten_json
{"a_b": 1}

>>> echo '{"a": {"b": 1}}' > test.json
>>> cat test.json | flatten_json
{"a_b": 1}
```
