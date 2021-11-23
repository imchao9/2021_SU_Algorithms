









# [`collections`](https://docs.python.org/3/library/collections.html#module-collections) — Container datatypes

| Dataypes                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple) | factory function for creating tuple subclasses with named fields |
| [`deque`](https://docs.python.org/3/library/collections.html#collections.deque) | list-like container with fast appends and pops on either end |
| [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap) | dict-like class for creating a single view of multiple mappings |
| [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) | dict subclass for counting hashable objects                  |
| [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict) | dict subclass that remembers the order entries were added    |
| [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) | dict subclass that calls a factory function to supply missing values |
| [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict) | wrapper around dictionary objects for easier dict subclassing |
| [`UserList`](https://docs.python.org/3/library/collections.html#collections.UserList) | wrapper around list objects for easier list subclassing      |
| [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString) | wrapper around string objects for easier string subclassing  |

## Deque

[`deque`](https://docs.python.org/3/library/collections.html#collections.deque): list-like container with fast appends and pops on either end



## Counter

[`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)dict subclass for counting hashable objects

Reference, https://www.geeksforgeeks.org/counters-in-python-set-1/?ref=lbp

```python
from collections import Counter
  
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
  
# with keyword arguments
print(Counter(A=3, B=5, C=2))

# Output of all the three lines is same :
# Counter({'B': 5, 'A': 3, 'C': 2})
# Counter({'B': 5, 'A': 3, 'C': 2})
# Counter({'B': 5, 'A': 3, 'C': 2})
```



## OrderedDict

[`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict)dict subclass that remembers the order entries were added

The only difference between [dict()](https://www.geeksforgeeks.org/python-set-4-dictionary-keywords-python/) and OrderedDict() is that: <u>OrderedDict **preserves the order** in which the keys are inserted.</u> A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.



## Defaultdict

[`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict)dict subclass that calls a factory function to supply missing values