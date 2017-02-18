# flatten_json
Flattens JSON objects in Python. ```flatten_json``` destroys the hierarchy in your object which can be useful if you want to force your objects into a table.

### Installation
```
pip install flatten_json
```

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
{'a': '1',
 'b': '2',
 'c_0_d_0': '2',
 'c_0_d_1': '3',
 'c_0_d_2': '4',
 'c_0_e_0_f': '1',
 'c_0_e_0_g': '2'}
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
[{'a': '1', 'b': '2', 'c_d': '3', 'c_e': '4'},
 {'a': '0.5', 'c_d': '3.2'},
 {'a': '0.8', 'b': '1.8'}]
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

Thanks to @jvalhondo, @drajen, and @azaitsev for pointing this out.


### Unflatten
Reverses the flattening process. Example usage:
```python
dic = {
    'a': 1,
    'b_0': 1,
    'b_1': 2,
    'c_a': 'a',
    'c_b_0': 1,
    'c_b_1': 2
}
unflatten(dic)
```
returns:
```python
{
    'a': 1,
    'b': [1, 2],
    'c': {'a': 'a', 'b': [1, 2]}
}
```

**Note**
Currently this feature does not properly handle lists. `flatten` encodes key for list values with integer indices which makes it ambiguous for reversing the process. Consider this flattened dictionary:
```python
a = {'a': 1, 'b_0': 5}
```

Both `{'a': 1, 'b': [5]}` and `{'a': 1, 'b': {0: 5}` are legitimate answers. For now this function is going to output the latter. Feel free to take this. If you do make sure you can passs the `test_unflatten_with_list` test which is currently failing. 

Thanks to @nmaas87 for requesting this feature.